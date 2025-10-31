Multi-Container Application with Docker Compose

Objective of the task:
The goal of this assignment was to design and implement a simple multi-container application using Docker Compose. The application consists of a Flask-based web API and a MySQL database, running in separate containers. The objective was to demonstrate how containerized services can communicate, share data, and persist state. This task was intended to build foundational DevOps skills, including container orchestration, service networking, and persistent storage. It also aimed to simulate a real-world microservice setup where a backend API interacts with a database. The final deliverable was a working application accessible via browser, displaying a message stored in MySQL.

How I Approached It:
I began by creating a basic Flask app (app.py) that connects to a MySQL database and fetches a message. I wrote a Dockerfile to containerize the Flask app with all required dependencies. Next, I created a docker-compose.yml file to define two services: web (Flask) and db (MySQL). I configured environment variables and mounted a volume to initialize the database using init.sql. I used Docker volumes to ensure MySQL data persisted across container restarts. I ran the application using docker compose up --build and validated the output at http://localhost:5000. I debugged issues related to container startup, database connection, and volume mounting. I documented each step in a detailed log and committed all files incrementally to GitHub. Finally, I pushed the Docker image to Docker Hub and added screenshots to the GitHub repo.

Technologies Used:
Python 3.9 - for writing the Flask API
Flask - lightweight web framework for the API
MySQL 5.7 - relational database for storing messages
Docker - to containerize the app and database
Docker Compose -to orchestrate multi-container setup
SQL - to create and populate the database
Git & GitHub - for version control and documentation
Markdown - for writing the README and logs
VS Code - as the development environment

Outcome:
Successfully built and ran a multi-container application using Docker Compose. The Flask app connected to MySQL and displayed a message from the database. Data persisted across container restarts using Docker volumes. The database was initialized automatically using a mounted SQL script. All code, logs, and screenshots were committed to GitHub with clear commit messages.  

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/6385e6bc-cdc0-4bcb-8367-e177f819d028" />

<img width="954" height="540" alt="Image" src="https://github.com/user-attachments/assets/7c5aa316-ef16-498b-9257-577141fa91e2" />
<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/9a7ca63d-3d12-408c-af32-8aea707c671d" />

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/a0aa567b-626b-46cb-b10e-bf695095d1f4" />

<img width="960" height="539" alt="Image" src="https://github.com/user-attachments/assets/338a0c89-3536-41cb-a4ab-bf2b9e5d7e25" />


 
