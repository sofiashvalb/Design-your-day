# Design Your Day – Daily Task Manager Web App

**A personalized task management app that helps users organize their day with intuitive tools, visual inspiration, and flexible task tracking. Built with Flask, Python, JavaScript, and SQLite, the app features a dynamic front-end paired with an efficient back-end for a seamless experience.**

[▶️ **Video Demo**](https://youtu.be/qaoZ3I1CrKg)

---

## Features

- **Daily Task Tracker** – Add, view, and manage tasks with priority and optional time settings  
- **Random Quote Generator** – Get inspired by motivational quotes each time you visit the homepage  
- **Task Status Updates** – Mark tasks as done, in progress, or to-do using local storage  
- **Task Deletion** – Remove completed tasks directly from the database  
- **Life Tips Section** – Enjoy a relaxing section with helpful lifestyle suggestions  
- **Responsive UI** – Grid-based layout and mobile-ready design for all screen sizes

---

## Tech Stack

- **Backend:** Flask, Python, SQLite  
- **Frontend:** HTML, CSS (with Bootstrap), JavaScript  
- **Templating:** Jinja2 (Flask templating engine)  
- **Database:** SQLite (`tasks.db`, `quotes.db`)

---

## Highlights

- **Interactive Homepage with Quotes and Tasks:**  
  Pulls random quotes from `quotes.db` and updates the task list from `tasks.db` using Jinja templating

- **Modular File Structure:**  
  - `templates/`: Contains `layout.html` as the base with extendable pages like `home.html`, `tasks.html`, and `suggest.html`  
  - `static/`: Includes styling (`style.css`) and images (logo + lifestyle suggestions)  
  - `app.py`: Main Flask app handling routing and database logic

- **Asynchronous UI Enhancements:**  
  JavaScript updates task status in real time and provides feedback via alerts

- **Custom Styling with Bootstrap & CSS:**  
  Leveraging W3Schools and Bootstrap for foundational styles, with personalized enhancements in `style.css`, including responsive breakpoints and font/color choices

- **Flexible Grid Layout with Flask Templating:**  
  The base `layout.html` splits the UI into a three-column design with dynamic content areas using `{% block body %}`

- **User-Controlled Task Flow:**  
  Add tasks through `tasks.html`, view/update/delete from the main page, and interact via JavaScript-enhanced elements


