This is a full-stack web application for automating personal finance tracking. It allows users to upload receipt images, extract itemized expense data using OCR, and visualize their spending through an interactive dashboard.
Main structure:
- Upload receipt images and extract data using **Tesseract OCR**
- JWT-based authentication (login, register, secure user sessions)
- Visualize spending with React.js + Chart.js
- 🗄Store and manage expenses in a PostgreSQL database
- Fast backend API built with **FastAPI**
- Frontend developed with React, React Router, and styled with TailwindCSS

The project's main idea was to make tracking seamless and easy. When you get a receipt, simply take a photo and upload it. The app then parses the file and grabs key information, to then display from a database. 

Main technologies used are Python, fastAPI, SQLAlchemy, Tesseract OCR, React, Router, Tailwindcss, Chart.js, PostgreSQL, and JWT. 

Current project is an MVP that will be expanded on! 
