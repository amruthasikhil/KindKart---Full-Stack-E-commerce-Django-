

🛍️ Shop & Donation Management System

📘 Overview

The **Shop & Donation Management System** is a web-based platform that allows users to **buy products**, **donate items**, and enables **admins** and **shopkeepers** to manage all operations efficiently.
It combines **e-commerce** and **donation management** in a single system with clear role-based access control.

---

## 👥 Roles and Responsibilities

### 1. **Admin**

The **Admin** controls and manages the entire system, including users, products, orders, and donations.

#### **Main Tasks**

* **Shop Management**

  * Create and manage product categories (e.g., Clothing, Furniture).
  * Add, edit, or delete products.
  * Update product details such as price, description, and availability.

* **User Management**

  * View all users (customers and admins).
  * Modify or delete user accounts when required.

* **Donation Management**

  * Approve or reject donated items.
  * Assign donations to appropriate categories or store them for later use.

* **Order Management**

  * View all orders and their statuses (e.g., shipped, delivered).
  * Update order statuses.
  * Generate reports for order tracking and accounting.

* **Analytics**

  * View donation and sales statistics.
  * Analyze sales performance and total revenue.

* **Access Control**

  * Manage access permissions for all roles.
  * Ensure only authorized users can use specific system features.

---

### 2. **User (Customer)**

Users can browse, buy, and review products through the platform.

#### **Main Tasks**

* **Account Management**

  * Register and log in.
  * Update profile information (address, contact, etc.).
  * Change or recover password.

* **Product Browsing**

  * Explore products by category.
  * Search for specific items.
  * View detailed product information.

* **Shopping Cart**

  * Add items to the cart.
  * Update item quantities or remove them.
  * Proceed to checkout for purchase.

* **Order Management**

  * View previous orders (completed, pending, canceled).
  * Track shipping and delivery status.
  * Leave reviews for purchased items.

* **Checkout**

  * Place orders as a guest or registered user.
  * Choose payment method (e.g., Cash on Delivery).
  * Enter shipping and billing details.

---

### 3. **Donor**

Donors can contribute items to the shop **without creating an account**.

#### **Main Tasks**

* **Donation Submission**

  * Fill out the donation form with item details (name, condition, description).
  * Optionally provide contact details.

* **Donation Confirmation**

  * Receive a confirmation message after successful donation.

* **Donation History**

  * View a record of donated items (if tracked).

* **Donation Guidelines**

  * Check which items are allowed or restricted for donation.

---

### 4. **Shop Keeper**

The **Shop Keeper** manages the shop’s products and donation processing but does not have full admin privileges.

#### **Main Tasks**

* **Inventory Management**

  * Add and update product details (name, price, stock, description).
  * Assign products to proper categories.

* **Donation Review**

  * Review donated items from users.
  * Approve or reject based on quality and necessity.
  * Move approved donations into inventory or hold for later use.

* **Order Fulfillment**

  * Review customer orders.
  * Mark orders as shipped upon confirmation.
  * Assist in packaging and preparing products for delivery.

* **Shop Maintenance**

  * Monitor product conditions.
  * Ensure sufficient stock availability.
  * Request restocking when inventory is low.

---

### 5. **General Features (All Roles)**

* **Role-Based Access Control**

  * Admin → Full system access.
  * Shop Keeper → Limited access (no admin settings).
  * Donor → Access to donation submission only.
  * User → Access to product browsing, purchasing, and reviewing.

---

## ⚙️ Technologies Used

* **Backend:** Python (Flask Framework)
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Database:** MySQL (via SQLyog or WAMP Server)
* **Server:** WAMP Server (Local Development)

---

## 🧩 Key Highlights

* Combines **shopping** and **donation** features in one platform.
* **Easy-to-use interface** for both buyers and donors.
* **Role-based access system** ensures secure management.
* Supports **real-time inventory and order tracking**.

---

## 📄 Future Enhancements

* Add online payment integration (e.g., PayPal, Stripe).
* Include user notifications and order tracking via email or SMS.
* Create an analytics dashboard for detailed reports.
* Enable multi-language support for accessibility.

---

Would you like me to make this look even more polished in **Markdown formatting** (with icons, color emojis, and better indentation) for GitHub’s `README.md` display?
