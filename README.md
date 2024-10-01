# University Information System

A simple GUI application built with Tkinter and SQLite3 to manage university instructor and department information. This application allows users to retrieve and add details about instructors and departments.

## Features

- **Get Instructor Info**: Retrieve information about instructors using their ID.
- **Get Department Info**: Retrieve information about departments using their name.
- **Add Instructor Info**: Add new instructors to the database.
- **Add Department Info**: Add new departments to the database.
- **Clear**: Clear input fields and results.
- **Quit**: Exit the application.

## Technologies Used

- Python
- Tkinter (for GUI)
- SQLite3 (for database management)
- Regular Expressions (for input validation)

## Database Schema

The application uses two tables: **Instructor** and **Department**.

### Instructor Table

| Field      | Type   | Constraints                  |
|------------|--------|------------------------------|
| `id`       | TEXT   | PRIMARY KEY                  |
| `name`     | TEXT   | NOT NULL                     |
| `department` | TEXT  | NOT NULL                     |

### Department Table

| Field      | Type   | Constraints                  |
|------------|--------|------------------------------|
| `name`     | TEXT   | PRIMARY KEY                  |
| `building` | TEXT   | NOT NULL                     |
| `budget`   | INTEGER| NOT NULL                     |


## Installation

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
   
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/university-information-system.git
   
3. Navigate to project directory:
   ```bash
   cd university-information-system

4. Run the application:
    ```bash
    python database.py


### Instructions
- Replace `your_script_name.py` with the actual name of your Python script.
- Replace `yourusername` with your GitHub username.
- Adjust any other information as necessary to suit your project details!

 
