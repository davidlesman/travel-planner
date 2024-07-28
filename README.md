# Travel Planner

## Overview

Travel Planner is a Flask-based web application created for the first Headstarter Hackathon. The application helps users to plan their travels by providing a simple and intuitive interface. This project was developed by @davidlesman and @shaiohaion.

## Project Structure

```
Travel Planner
├── app.py
├── static
│   └── bulma.min.css
└── templates
    └── home.html
```

### app.py

This is the main Python file where the Flask application is initialized and routes are defined. It handles the logic for rendering the home page and processing any user input.

### static

This directory contains static files used by the application. For this project, it includes:

- `bulma.min.css`: The Bulma CSS framework is used to style the application, providing a clean and modern look.

### templates

This directory contains the HTML templates used by the Flask application. For this project, it includes:

- `home.html`: The main HTML file rendered when users visit the home page. It uses Bulma for styling and contains the structure of the web interface.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/davidlesman/travel-planner.git
   cd travel-planner
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Open your web browser and navigate to** `http://127.0.0.1:5000` **to see the application in action**.

## Usage

1. **Home Page**: Upon opening the application, you will be greeted with the home page where you can start planning your travel.
2. **Plan Your Travel**: Use the dashboard to jot down your travel finds, which will be stored in localStorage.

## Authors

- **David Lesman** - [@davidlesman](https://github.com/davidlesman)
- **Shai Ohaion** - [@shai-david](https://github.com/shai-david)

## Acknowledgments

- Special thanks to Headstarter Hackathon for the opportunity to develop this project.
- Thanks to the creators of Flask and Bulma for their excellent frameworks and tools.
