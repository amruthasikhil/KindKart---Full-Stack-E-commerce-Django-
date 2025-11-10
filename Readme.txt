# 🛍️ Shop & Donation Management System (Django)

The **Shop & Donation Management System** is a robust, web-based platform that seamlessly integrates **e-commerce** and **charitable donation management** into a single centralized system. It provides distinct portals and access controls for four different user groups, ensuring efficient product sales, inventory tracking, and managed processing of donated items.

## ✨ Key Project Highlights

* **Complex Role-Based Access Control (RBAC):** Designed and implemented a secure, four-tiered authorization system for **Admin**, **Shop Keeper**, **User**, and **Donor** roles, ensuring data segregation and enforcing strict operational permissions.
* **Django ORM for Inventory:** Utilized the **Django ORM** to design and manage complex relational models for Products, Inventory, Sales Orders, and Donation Records, handling stock levels and order fulfillment logic.
* **Dual Workflow Management:** Engineered back-end logic in **Django** to manage two distinct workflows: a standard e-commerce pipeline (Cart, Checkout, Order Fulfillment) and a separate, anonymous **Donation Submission** and approval process.
* **RESTful API Design:** Implemented **Django REST Framework (DRF)** endpoints to handle data exchange for product listings, order processing, and administrative dashboards.

## ⚙️ Roles, Responsibilities, and Features

The platform's features are segmented to provide secure, tailored access for each stakeholder:

### 1. Admin (System Oversight) 🛠️

| Tasks | Description |
| :--- | :--- |
| **User & Access** | Full management control over all user accounts (including Shop Keepers) and system-wide access permissions. |
| **Data Analytics** | Generates reports on sales performance, total revenue, order tracking, and donation statistics. |
| **Product & Orders** | Global oversight of product categories, inventory levels, and ability to modify all order statuses. |

### 2. Shop Keeper (Inventory & Fulfillment) 📦

| Tasks | Description |
| :--- | :--- |
| **Inventory Management** | **Add, update, and manage** product details (price, stock, description) and assign products to categories. |
| **Donation Review** | Review incoming donation submissions, approve or reject items based on quality, and move approved items into shop inventory. |
| **Order Fulfillment** | Review new customer orders, mark orders as shipped, and manage the product delivery process. |

### 3. User (Customer) 🛒

| Tasks | Description |
| :--- | :--- |
| **Shopping Experience** | Register/Login, browse products via category, search, manage a persistent **Shopping Cart**, and proceed through Checkout (e.g., Cash on Delivery). |
| **Post-Purchase** | Track order status, view order history, and submit detailed **reviews** for purchased items. |

### 4. Donor (Anonymous Submission) 🙏

| Tasks | Description |
| :--- | :--- |
| **Donation Submission** | Submit items via a dedicated form (name, condition, description) without needing to create a user account. |
| **History & Guidelines** | Access donation guidelines and receive submission confirmation. |

## 💻 Technical Stack

| Component | Technology | Role in the Project |
| :--- | :--- | :--- |
| **Back-End Framework** | **Django (Python)** | Core application logic, routing, and handling of complex e-commerce and donation workflows. |
| **API** | **Django REST Framework (DRF)** | Used for robust API endpoint creation, enabling external and internal data communication. |
| **Data Management** | **Django ORM** | Managed all database interactions and complex query logic via Python models (SQLite assumed for dev setup). |
| **Front-End** | HTML, CSS, **Bootstrap**, JavaScript | Developed the responsive user interface for all four distinct portals. |

---

## 🏃 How to Run the Project Locally

Follow these steps to set up and run the Shop & Donation Management System on your local machine.

### Prerequisites
* Python 3.8+
* `pip` and `venv` (recommended)

### 1. Clone the Repository and Setup Environment
```bash
git clone [Your GitHub URL Here]
cd shop-donation-system-django # Replace with your actual folder name

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages (Django, DRF, etc.)
pip install -r requirements.txt
