# Django Counter App

A real-time counter application built with Django, demonstrating the power of HTMX and Django Template Partials for dynamic content updates without full page refreshes.

## Features

- Real-time counter updates using HTMX
- Partial template rendering with Django Template Partials
- Custom loading button component with animation
- Bootstrap UI with Material Design theme
- No page refresh required for counter updates

## Technologies Used

- Django
- HTMX
- MDBootstrap
- Django Template Partials
- JavaScript
- CSS3

## How It Works

1. The counter value is stored in Django's database model
2. When increment/decrement buttons are clicked, HTMX makes a request to the server
3. Django processes the request and updates the counter value
4. Only the counter value section is updated in the DOM, without refreshing the entire page
5. Custom loading animations provide visual feedback during interactions

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a counter object in Django admin
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `templates/`: Contains all HTML templates
  - `home.html`: Main counter page
  - `base.html`: Base template with common assets
  - `compo/common/`: Reusable components
- `partials/`: Django app
  - `models.py`: Counter model
  - `views.py`: Counter logic
  - `urls.py`: URL routing

## Contributing

Feel free to submit issues and enhancement requests!
