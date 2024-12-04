
# CSV to XLSX Django Project

This project provides an API for user registration, login, and file upload functionality to convert CSV files to XLSX format. It uses Django as the backend framework and provides a simple interface for users to upload CSV files, which are then converted into Excel files.

## Features

- **User Registration**: Users can create an account by providing a unique username and password.
- **User Login**: Users can log in by providing their username and password.
- **File Upload**: Authenticated users can upload CSV files, which are converted to XLSX files.
- **File Conversion**: Converts uploaded CSV files into XLSX format and provides them as a downloadable file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate into the project directory**:
   ```bash
   cd csvtoxlsx
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (optional, for accessing Django admin):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the API** at `http://127.0.0.1:8000`.

## API Endpoints

### 1. **User Registration**
- **URL**: `/register`
- **Method**: `POST`
- **Data**:
  - `username`: The username for the new user.
  - `password`: The password for the new user.
- **Response**:
  - Success: `{ "message": "User registered successfully", "user_id": <user_id> }`
  - Error: `{ "error": "Username and password are required" }` or `{ "error": "Username already exists" }`

### 2. **User Login**
- **URL**: `/login`
- **Method**: `POST`
- **Data**:
  - `username`: The username of the user.
  - `password`: The password of the user.
- **Response**:
  - Success: `{ "message": "Login successful" }`
  - Error: `{ "error": "Invalid credentials" }` or `{ "error": "User does not exist" }`

### 3. **File Upload and Conversion**
- **URL**: `/upload`
- **Method**: `POST`
- **Data**:
  - `file`: A CSV file to be uploaded and converted to XLSX.
- **Response**:
  - Success: A file download response with the converted XLSX file.
  - Error: `{ "error": "No file provided." }`, `{ "error": "Only CSV files are allowed." }`, or `{ "error": "File processing error: <error_message>" }`

## Folder Structure

```
csvtoxlsx/
│
├── main/                        # Main Django app
│   ├── migrations/              # Migration files
│   ├── models.py                # Models for user and document information
│   ├── views.py                 # Views handling the logic for registration, login, and file upload
│   └── urls.py                  # URLs for the application
│
├── csvtoxlsx/                   # Project settings
│   ├── settings.py              # Project settings file
│   ├── urls.py                  # URL routing for the whole project
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── manage.py                    # Django management script
├── requirements.txt             # List of dependencies
└── README.md                    # This README file
```

## Database

This project uses Django's default SQLite database to store user and document information. The models for `UserModel` and `DocumentsModel` are defined in `main/models.py`.

- **UserModel**: Contains user information like username and password.
- **DocumentsModel**: Stores information about uploaded CSV files and their conversion to XLSX.

## Settings

- **MEDIA_ROOT**: The directory where files (CSV and XLSX) are stored and served from is defined in the `settings.py` file under `MEDIA_ROOT`.
- **CSRF Exemptions**: CSRF protection is exempted for the register, login, and upload views using the `@csrf_exempt` decorator.

## Known Issues
- Passwords are stored in plain text. It is recommended to implement proper password hashing before using this in a production environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

