# README.md

# Calculator Web App

This project is a web application that implements a simple calculator using Django as the backend framework and React for the frontend. 

## Project Structure

The project is organized as follows:

```
calculator-web-app
├── backend                # Django backend
│   ├── calculator         # Calculator app
│   ├── manage.py          # Django management script
│   └── calculator_web_app  # Main Django project
├── frontend               # React frontend
│   ├── public             # Public assets
│   └── src                # Source code for React app
├── package.json           # NPM configuration
└── requirements.txt       # Python dependencies
```

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- User-friendly interface built with React.
- Responsive design for various devices.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd calculator-web-app
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install Python dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run migrations:
     ```
     python manage.py migrate
     ```
   - Start the Django server:
     ```
     python manage.py runserver
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install Node.js dependencies:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## Usage

- Access the application in your web browser at `http://localhost:3000`.
- Use the calculator interface to perform arithmetic operations.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.