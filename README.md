Multi-Container Application with Docker Compose

The goal of this assignment is to build a simple multi-container application using Docker Compose, which helps manage and run multiple services together. 
This project introduces key DevOps concepts such as containerization, service networking, environment configuration, and persistent data storage.

Technologies Used

 1.Python  
 2.Flask  
 3.MySQL  
 4.Docker & Docker Compose  
 5.SQL

app.py - Flask app that connects to MySQL and returns a message  
Dockerfile - Builds the Flask container  
requirements.txt - Lists Python dependencies  
docker-compose.yml - Defines and connects Flask and MySQL services  
init.sql - Initializes the database with a table and message

For Building and running the containers: we use docker compose up --build command

finally we visit http://localhost:5000

we can see: "Hello from MySQL!"

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/6385e6bc-cdc0-4bcb-8367-e177f819d028" />

 
