Features

1. Leads Management

Create, read, update, and delete leads.

2. Contacts Management

Create, read, update, and delete contacts.

Link contacts to the appropriate leads for easy management.

3. Notes

Add notes for a specific lead to track updates or important information.

4. Reminders

Schedule reminders for leads to follow up or take necessary actions.

If needed, Celery is used to handle task scheduling.

Installation

Clone the repository:

git clone https://github.com/your-username/leads-management-system.git
cd leads-management-system

Set up a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up the database:

python manage.py makemigrations
python manage.py migrate

Run the development server:

python manage.py runserver

Usage

1. Leads

Navigate to /leads to view all leads.

Use the interface to create, edit, or delete a lead.

2. Contacts

Navigate to /contacts to view all contacts.

Use the interface to add contacts and link them to specific leads.

3. Notes

Open a lead's details page to view or add notes for the lead.

4. Reminders

Schedule reminders from a lead's details page.

Ensure Celery is running for scheduled reminders.

Scheduling with Celery

Install Celery and a message broker (e.g., Redis):

pip install celery redis

Start the Redis server:

redis-server

Configure Celery in the project settings.

Start the Celery worker:

celery -A project_name worker --loglevel=info

Contributing

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit your changes:

git commit -m 'Add new feature'

Push to your fork:

git push origin feature-name

Submit a pull request.

License

This project is licensed under the MIT License.

Contact

For questions or suggestions, please contact wekesabuyahi@gmail.com.
