
# 💰 SpendWise: Idempotent Expense Tracker

A production-grade expense management system built with **FastAPI** and **React**. This application is specifically engineered to handle unreliable network conditions and ensure 100% financial data integrity.

## 🔗 Live Links
* **Frontend:** [https://fenmo-assessment-frontend.onrender.com/](https://fenmo-assessment-frontend.onrender.com/)
* **API Documentation:** [https://fenmo-assessment.onrender.com/docs](https://fenmo-assessment.onrender.com/docs)

---

## 🛠 Tech Stack & Rationale

### **Backend: FastAPI & PostgreSQL**
* **FastAPI:** Chosen for its native support for **Asynchronous** operations and strict **Pydantic** validation. This ensures only valid financial data reaches the database.
* **PostgreSQL:** Used for its robust support of the `Numeric` type, which is critical for preventing floating-point errors in currency, via the Render PostgreSQL instance.
* **SQLAlchemy (ORM):** Provides a clean abstraction while enforcing unique constraints (like `request_id`) at the database engine level.

### **Frontend: React (Vite) & Tailwind CSS**
* **Vite:** Selected for near-instant HMR (Hot Module Replacement) and optimized production builds.
* **Axios:** Configured with a base instance to handle global API settings and environment-based URL switching.
* **React-Toastify:** Implemented to provide non-blocking, user-friendly feedback for both success and validation errors.

---

## 🏗 Key Engineering Implementations

### **1. 100% Financial Accuracy**
We avoid standard `Float` or `Double` types which suffer from binary rounding errors (e.g., `0.1 + 0.2 != 0.3`).
* **Database:** Utilizes `Numeric(10, 2)`.
* **Application:** Utilizes Python's `Decimal` class for all calculations.
* **Frontend:** Formatted to 2 decimal places using `.toFixed(2)` for consistent display.

### **2. Network-Resilient Idempotency**
To handle "Unreliable Networks" (where a user might double-click or a request might retry after a timeout):
* Every transaction is assigned a **Client-Side UUID** (`request_id`) upon form load.
* **Backend Logic:** 1. Checks if the `request_id` already exists in the database.
    2. If it exists, it returns the existing record (**HTTP 200 OK**).
    3. If it is new, it creates the record (**HTTP 201 Created**).
This ensures that even if the network fails *after* the server processes the request, the retry will not create a duplicate expense.



---

## 🧪 Testing & Validation
* **Schema Validation:** Pydantic models enforce that `amount > 0` and all fields are present before processing.
* **Integration Tests:** Located in `backend/app/tests`. These verify the idempotency flow and error handling for negative amounts.
* **CORS Security:** Configured via environment variables to ensure only authorized frontends can access the API in production.

---

## 🚀 Environment Setup

### **Backend Setup**
1. Create a `.env` file in the `backend/` directory:
```env
PROJECT_NAME=Fenmo Assessment API
VERSION=1.0.0
DATABASE_URL=postgresql://user:pass@localhost/db
BACKEND_CORS_ORIGINS=http://localhost:5173,[https://fenmo-assessment-frontend.onrender.com](https://fenmo-assessment-frontend.onrender.com)
```

2. Install & Run:
Bash
```
pip install -r requirements.txt
uvicorn app.main:app
```
3. Frontend Setup
Create a .env file in the frontend/ directory:
```
VITE_API_URL=[https://fenmo-assessment.onrender.com/api/v1](https://fenmo-assessment.onrender.com/api/v1)
```
5. Install & Run:
```
npm install
npm run dev
```
📝 Trade-offs & Future Scope
Authentication: Focus was placed on core idempotency and decimal precision; JWT auth would be the next logical step.

State Management: Used React Hooks for simplicity; for a larger application, Redux Toolkit would be implemented.
