# 📚 BooksVault

BooksVault is a personal web-based book management system that allows users to digitally track and manage their own private book collection. Designed with simplicity and clarity in mind, it enables individuals to add, update, delete, and filter books by category or reading status, all in a clean and responsive interface.

This project was developed as the final capstone project for CS50’s Web Programming with Python and JavaScript.

---

## 📌 Distinctiveness and Complexity

BooksVault is distinct from previous CS50 projects in its focus on **single-user personal data management** rather than multi-user interaction. While many web apps involve social components like user profiles or messaging, this application is centered around **private library organization** — a less common use case that presents different challenges, particularly in data modeling, form handling, and UI design.

Complexity is demonstrated in several key areas:
- **Cloudinary image integration**, allowing for external image uploads linked to each book.
- **Full CRUD functionality** using Django models, forms, and views.
- **Category-based filtering and conditional rendering**.
- A clean and adaptive UI that supports both **light and dark themes**.
- Organized app structure with reusable components and clear routing.

These components work together to deliver a robust and polished single-user experience while offering opportunities for future scaling or authentication features.

---

## 🧠 Features

- 📘 Add new books with title, author, category, read status, and optional image.
- ✏️ Edit or delete books from your collection.
- 🗂 Filter books by custom categories.
- ☁️ Upload book cover images via Cloudinary.
- 🌙 Toggle-friendly light and dark UI.
- 🧹 Clear and simple UX with no login required.

---

## 🗂️ Project Structure
BooksVault/ ├── books/ # Core app files │ ├── templates/books/ # HTML templates │ ├── static/books/ # CSS styling │ ├── admin.py │ ├── forms.py │ ├── models.py │ ├── urls.py │ └── views.py ├── BooksVault/ # Django settings and project URLs ├── db.sqlite3 ├── manage.py ├── requirements.txt └──