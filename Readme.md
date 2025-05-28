# Data Submission & Redundancy Checker

A simple Flask web application for submitting data, which checks for redundancy using SHA-256 hashing and stores unique entries in a MongoDB database.

## Features

- Web form for data submission
- Prevents redundant (duplicate) data entries using hash comparison
- Stores data securely in MongoDB
- Clean, user-friendly interface

## Project Structure

```
app.py
db.py
redundancy_checker.py
requirements.txt
templates/
    index.html
.vscode/
    settings.json
```

## Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure MongoDB**:
    - Update the MongoDB URI and credentials in [`db.py`](db.py) if needed.

4. **Run the application**:
    ```sh
    python app.py
    ```

5. **Access the web app**:
    - Open your browser and go to `http://127.0.0.1:5000/`

## File Descriptions

- [`app.py`](app.py): Main Flask application with routes for home and data submission.
- [`db.py`](db.py): Handles MongoDB connection and data operations.
- [`redundancy_checker.py`](redundancy_checker.py): Provides hashing and redundancy checking logic.
- [`templates/index.html`](templates/index.html): HTML template for the data submission form.
- [`requirements.txt`](requirements.txt): Python dependencies.

## License

This project is for educational purposes.