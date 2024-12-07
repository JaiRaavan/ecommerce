# Django eCommerce Platform

This is a fully-featured eCommerce web application built with Django. The project includes functionalities such as user authentication, item categories, shopping cart, ordering, template tags, and secure payment integration.

---

## Features

### User Features
- **Authentication**: User registration, login, and logout with secure password management.
- **Profile Management**: Users can manage their profiles.
- **Order Tracking**: Users can track their cart items in cart.

### Product and Categories
- **Item Categories**: Products are organized into categories for easier navigation.
- **Item Management**: List, view, and search for items.
- **Item Details**: Each product will be displaying images, price, and description.

### Shopping Cart
- Add, remove, and update item quantities in the cart.
- View the total price of all items in the cart.

### Ordering and Payments
- **Order Placement**: Place orders directly from the shopping cart.
- **Payment Integration**: Secure payment gateway integration (e.g., SSLCommerz-python).

### Template Tags and Filters
- Custom Django template tags for displaying categories, cart items, and user-friendly formatting.
- Template filters for price formatting and category-specific features.

### Admin Features
- Manage products, categories, and orders through the Django Admin panel.
- View sales analytics.
- Here we defined custom User model for more features.

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.0+
- Virtualenv (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/My_Ecom_Project.git
   cd My_Ecom_Project
   
2. **Set Up Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run Database Migrations**
   ```bash
   python manage.py migrate

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser

6. **Run the Development Server**
   ```bash
   python manage.py runserver

7. **Access the Application**
   
   Open your browser and navigate to http://127.0.0.1:8000.


---

## Project Structure

```plaintext
My_Ecom_Project/
│
├── My_Ecom_Project/         # Core Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py
│   └── __pycache__/
│
├── App_Login/               # Handles user authentication
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # Custom forms for login/registration
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py            # User models
│   ├── tests.py
│   ├── urls.py              # Authentication-related URLs
│   ├── views.py             # Authentication views
│   └── __pycache__/
│
├── App_Shop/                # Shopping functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py            # Product and category models
│   ├── tests.py
│   ├── urls.py              # URLs for shop-related views
│   ├── views.py             # Views for handling shop logic
│   └── __pycache__/
│
├── App_Order/               # Handles orders
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py            # Order-related models
│   ├── tests.py
│   ├── urls.py              # Order-related URLs
│   ├── views.py             # Views for order logic
│   └── __pycache__/
│
├── App_Payment/             # Payment gateway integration
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # Payment-related forms
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py            # Payment models
│   ├── tests.py
│   ├── urls.py              # Payment-related URLs
│   ├── views.py             # Views for payment processing
│   └── __pycache__/
├── template/                # Shared templates across apps
│   ├── App_Login/
│   │   └── ....
│   ├── App_Order/
│   │   └── ....
│   ├── App_Payment/
│   │   └── ....
│   ├── App_Shop/
│   │   └── ....
│   ├── base.html
│   ├── navbar.html
├── media/                   # Uploaded media files (e.g., product images)
│   └── product/
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── README.md                # Project documentation


---
