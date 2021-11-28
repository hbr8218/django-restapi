Movie Backend API

## Installation steps

1. Ensure you have python3 installed

2. Install python virtual environment package using `python3 -m pip install --user virtualenv`
3. create a virtual environment using `virtualenv venv` Here venv is user defined environment name
4. Activate the virtual environment by running `source venv/bin/activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`
