# 💰 Money Manager

A full-stack money management application built with **Next.js** and **FastAPI**, designed to help you track income, expenses, and analyze your financial habits.

## ✨ Features

- � **Track Transactions** - Record income and expenses with categories
- 🏷️ **Category Management** - Organize transactions with custom categories
- 📈 **Analytics** - View monthly summaries and spending patterns
- 🎨 **Modern UI** - Beautiful, responsive interface with Tailwind CSS
- 🚀 **Fast API** - High-performance backend with FastAPI
- 📱 **Mobile Responsive** - Works seamlessly on all devices

## 🛠️ Tech Stack

### **Frontend**
- **Next.js 14+** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **React** - UI components

### **Backend**
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation
- **SQLite** - Development database
- **PostgreSQL** - Production database (Vercel)

## 📁 Project Structure

```
money-manager/
│   ├── src/
│   │   ├── app/          # Next.js App Router pages
│   │   ├── components/   # React components
│   │   └── lib/          # Utilities and API client
│   └── package.json
│
├── api/                  # FastAPI backend
│   ├── app/
│   │   ├── routers/      # API route handlers
│   │   ├── models.py     # Database models (SQLAlchemy)
│   │   ├── schemas.py    # Data validation (Pydantic)
│   │   ├── database.py   # Database connection
│   │   └── main.py       # FastAPI app
│   ├── index.py          # Vercel entry point
│   └── requirements.txt  # Python dependencies
│
└── vercel.json           # Vercel deployment config
```

## 🚀 Getting Started

### Prerequisites
- **Python 3.9+** (for FastAPI backend)
- **Node.js 18+** (for Next.js frontend)
- **npm** or **yarn** (package manager)

### Backend Setup (FastAPI)

1. **Navigate to the api directory:**
   ```bash
   cd api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the development server:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Frontend Setup (Next.js)

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Access the app:**
   - Frontend: http://localhost:3000

## 📚 Learning Resources

### FastAPI Concepts
- **Models (models.py)**: Define database structure using SQLAlchemy ORM
- **Schemas (schemas.py)**: Validate request/response data using Pydantic
- **Routers**: Organize endpoints by feature (categories, transactions, analytics)
- **Dependency Injection**: `get_db()` provides database sessions to endpoints
- **CORS**: Allows frontend to communicate with backend

### Next.js Concepts
- **App Router**: File-based routing in `src/app/`
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **Server/Client Components**: React Server Components by default

## 🎯 Features (To Be Implemented)

- ✅ Project structure setup
- ⏳ Category management (CRUD)
- ⏳ Transaction tracking (income/expense)
- ⏳ Monthly analytics
- ⏳ Visual charts
- ⏳ Responsive UI

## 🚢 Deployment

This project is configured for **Vercel** deployment:
- Frontend and backend deploy together
- Uses Vercel Postgres for production database
- Automatic HTTPS and CDN

## 📖 Next Steps

1. Implement category CRUD endpoints
2. Implement transaction CRUD endpoints
3. Build frontend UI components
4. Add charts and analytics
5. Deploy to Vercel
