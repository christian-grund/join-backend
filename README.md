# Join Backend

## About

Join backend is the server-side application that powers the Join frontend. Built using Python and Django, it handles user authentication, data storage, task management, and all backend-related logic required to support the Join frontend application.

## Features

-   **User Authentication**: Allows users to sign up, log in, and manage their sessions.
-   **Task Management**: API endpoints to create, edit, delete, and retrieve tasks.
-   **Contacts Management**: API endpoints to add, edit, and delete contacts.
-   **Kanban Board Support**: Backend logic to manage tasks in various categories like 'To-Do', 'In Progress', 'Awaiting Feedback', and 'Done'.
-   **Database Storage**: Tasks, users, and contacts are stored and managed in a relational database.
-   **API Endpoints**: RESTful API to handle task and user operations.

## Tech Stack

-   **Python**: The primary programming language.
-   **Django**: The web framework used to build the backend.
-   **SQLite**: The database used to store application data (ensure it's set up correctly).
-   **Django REST Framework**: For building RESTful APIs.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/christian-grund/join-backend.git
    ```
2. **Navigate to the project directory**:

    ```bash
    cd join-backend
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

6. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

8. The backend will be accessible at `http://localhost:8000/` or `http://127.0.0.1:8000/`.

## Usage

Once the backend is running, you can interact with the API using a tool like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), or by connecting the frontend.

## Contact

For questions or suggestions, contact mail@christian-grund.dev or create an issue on GitHub.

---

Enjoy exploring and using the Join Backend application!
