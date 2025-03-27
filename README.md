# ShopKart - E-commerce Website 🛒

Welcome to **ShopKart**, an online shopping platform built using Django. This repository contains the source code for a shopping cart system with features like user authentication, product listing, and order management.

## 🌟 Features
- User authentication (Register/Login/Logout)
- Product browsing & search functionality
- Shopping cart & favorite items functionality
- Checkout & order summary
- Responsive UI with Bootstrap
- Dynamic pricing & quantity updates

## 🚀 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default) / PostgreSQL (for production)

## 📌 Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/shopkart.git
   cd shopkart
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin panel):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
   Visit **http://127.0.0.1:8000/** in your browser.

## 📂 Project Structure
```
shopkart/
│── shop/           # Main Django app
│── static/         # Static assets (CSS, JS, images, videos)
│── templates/      # HTML templates
│── db.sqlite3      # Database file (default)
│── manage.py       # Django management script
│── requirements.txt # Project dependencies
```

## 🛠 Configuration
- **Static Files:** Ensure static files are correctly set up for production.
- **Database:** Update `settings.py` if using PostgreSQL or another database.

## 📜 Contribution Guidelines
1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request 🚀

## 📞 Contact
For any issues or feature requests, open an **issue** on this repository. 😊

Happy Coding! 🎉

