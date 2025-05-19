import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import base64

def generate_promptpay_qr(phone_number, amount):
    """
    สร้าง QR Code สำหรับ PromptPay
    :param phone_number: เบอร์โทรศัพท์ (เช่น '0812345678')
    :param amount: จำนวนเงิน (float หรือ int)
    :return: base64 ของ QR Code image
    """
    # ตรวจสอบและจัดรูปแบบเบอร์โทรศัพท์
    if not phone_number.startswith('0'):
        raise ValueError("หมายเลขโทรศัพท์ควรเริ่มต้นด้วย 0")
    
    # แปลงเบอร์โทรศัพท์เป็นรูปแบบ PromptPay (เพิ่ม 66 และลบ 0 หน้า)
    promptpay_id = '0066' + phone_number[1:]
    
    # สร้างข้อมูลสำหรับ QR Code ตามรูปแบบ PromptPay
    qr_data = f"00020101021129370016A00000067701011101130066{phone_number[1:]}530376454{amount:.2f}5802TH6304"
    
    # คำนวณ CRC16 checksum
    crc = crc16(qr_data.encode('utf-8'))
    qr_data += f"{crc:04X}"
    
    # สร้าง QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # แปลงภาพเป็น base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return img_str

def crc16(data: bytes):
    """
    คำนวณ CRC16 สำหรับข้อมูล QR Code
    """
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc