# car-website
A web application for car listings. Users can filter, search, and save car ads. 
The project includes a custom user profile system, pagination, and search filters.

## Features

- User registration and authentication
- Profile management (custom user profile model)
- Filter cars by various criteria (brand, model, price, etc.)
- Save/unsave car ads
- Pagination for car listings

## Installation

1. Clone the repository:
   ```cmd
   git clone https://github.com/Kamen2001/car-website.git
   cd car-website
   ```

2. Set up a virtual environment and activate it:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```cmd
   python manage.py makemigrations
   python manage.py migrate
   ```

5. To use the custom management commands, run the following:
   ```cmd
   python manage.py load_cars
   ```

6. Start the development server:
   ```cmd
   python manage.py runserver
   ```