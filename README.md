#django_chat

## URL
You can access the project on Render at:

[https://assignment-adq3.onrender.com/](https://assignment-adq3.onrender.com/)

Please Note - I am using free plan of Render.com so expect delays upto 50 secomnds(minimum)

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.x** (preferably the latest stable version)
- **Pip** (Python's package installer)
- **Django** (for the backend web framework)
- **Daphne** (for WebSocket handling)

If you're using virtual environments, make sure you're set up for it.

---

## Installation

1. **Clone the Repository**  
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/praneethattada/Assignment.git

2. **Install Dependencies**
  
    ```bash
   
   cd django-chat
   pip install -r requirements.txt

4. **Set Up Environment Variables**
   Create .env file
    ```bash
   
    SECRET_KEY=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=

5. **Deployment**
   Run below commands on differnt terminals
   ```bash
   
    python manage.py runserver
    python run_daphne.py

The project should now be running locally at http://127.0.0.1:8000.

