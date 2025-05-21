Careme - Your Personal Health and Wellness Companion
Abstract
Careme is a Django-based web application designed to empower users to lead healthier lives by tracking daily calorie intake, accessing curated health and wellness tips, and engaging with an AI chatbot for personalized health and mental wellness advice. Built with Docker for seamless deployment, Careme helps users set and achieve calorie goals, stay informed with practical health tips, and gain insights through AI-driven conversations. Whether you're managing your diet, seeking wellness inspiration, or exploring health-related questions, Careme offers an intuitive platform to support your wellness journey.
User Stories
Below are three user stories that illustrate how different users interact with Careme:

As a health-conscious individual, I want to track my daily calorie intake and monitor my progress toward my goals so that I can maintain a balanced diet.
As a user seeking wellness advice, I want to read health tips directly from the homepage so that I can quickly learn ways to improve my physical and mental health.
As someone exploring health questions, I want to chat with an AI on the chat page to get answers about nutrition and mental wellness so that I can make informed decisions.

Usage Steps Based on User Stories
User Story 1: Tracking Calorie Intake

Step 1: Navigate to localhost:8000 after starting the application.
Step 2: Log in or sign up for a user account on the homepage.
Step 3: Click the "Plan" link in the navigation menu to access the calorie tracking page.
Step 4: Enter details of the food consumed (e.g., "Grilled Salmon, 250 kcal") and submit the form.
Step 5: Return to the homepage to view your daily calorie intake and progress toward your goal displayed on the dashboard.

User Story 2: Accessing Health Tips

Step 1: Open the application by visiting localhost:8000.
Step 2: On the homepage, locate the "Health Tips" section.
Step 3: Browse tips, such as "Incorporate 30 minutes of exercise daily" or "Practice deep breathing to reduce anxiety."
Step 4: Click on a tip to read more details or save it for later reference (if logged in).
Step 5: Refresh the homepage to discover new tips updated periodically.

User Story 3: Chatting with the AI

Step 1: Access the application at localhost:8000.
Step 2: Click the "Chat" link in the navigation menu to visit the AI chat page.
Step 3: Type a question, such as "What foods boost energy levels?" or "How can I manage stress effectively?"
Step 4: Submit the question and view the AI’s response in the chat interface.
Step 5: Continue the conversation by asking follow-up questions or exploring new topics.

Installation and Usage
Prerequisites

Docker and Docker Compose installed on your system.
Git installed to clone the repository.
A web browser to access the application at localhost:8000.

Installation

Clone the Repository:Clone the Careme repository from GitHub:git clone https://github.com/username/careme.git
cd careme


Build and Run with Docker:Use Docker Compose to build and start the application:docker-compose up --build

This command sets up the Django application, database, and necessary services.
Access the Application:Open a web browser and navigate to:http://localhost:8000

The Careme application should now be running and accessible.

Usage

Homepage Navigation:
At localhost:8000, the homepage displays a dashboard with your calorie intake (if logged in) and a section for health tips.
Use the navigation menu to access the "Plan" page for calorie tracking or the "Chat" page for AI interactions.


Account Setup:
Sign up for a new account or log in to save your calorie data and preferences.
Guest users can access health tips and the AI chat without logging in.


Calorie Tracking:
On the "Plan" page, input food items and their calorie counts to track your intake.
The homepage dashboard updates automatically to show your progress.


Health Tips:
Browse tips on the homepage or click for detailed advice.


AI Chat:
Use the chat page to ask health-related questions and receive real-time AI responses.



Troubleshooting

Docker Issues: Ensure Docker is running and you have sufficient permissions to execute docker-compose. If the build fails, verify the docker-compose.yml file.
Port Conflicts: If localhost:8000 is unavailable, check if another service is using port 8000 or modify the port in docker-compose.yml.
Database Errors: If the app fails to load, run docker-compose down and then docker-compose up --build to reset the containers.
For additional support, visit the GitHub Issues page.

Contributing
We welcome contributions to Careme! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature/new-feature).
Open a pull request.

Please ensure your code follows Django’s best practices and includes relevant tests.
License
This project is licensed under the MIT License. See the LICENSE file for details.


youtube links for application videos: https://youtube.com/shorts/HfgeggrQhH8?feature=share