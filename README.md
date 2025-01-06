# Leads Management System

## Features

1. **Leads Management**
   - Create, read, update, and delete leads.

2. **Contacts Management**
   - Create, read, update, and delete contacts.
   - Link contacts to the appropriate leads for easy management.

3. **Notes**
   - Add notes for a specific lead to track updates or important information.

4. **Reminders**
   - Schedule reminders for leads to follow up or take necessary actions.
   - Celery can be used to handle task scheduling if needed.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/leads-management-system.git
   cd leads-management-system
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
