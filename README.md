# 💰 Money Manager

A modern, full-stack personal finance management application built with Next.js and FastAPI.

![Money Manager](https://img.shields.io/badge/Status-Production%20Ready-success)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)

## ✨ Features

- 🔐 **Secure Authentication** - JWT-based user authentication
- 💸 **Transaction Management** - Track income and expenses with categories
- 📊 **Analytics Dashboard** - Visual insights with charts and summaries
- 🏷️ **Category Management** - Organize transactions with custom categories
- 🔍 **Advanced Filtering** - Filter by type, category, and date range
- ✏️ **Quick Entry** - Fast transaction entry with "Today" button
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile
- 🌐 **Multi-currency Support** - Default INR (₹), supports USD, EUR, GBP

## 🚀 Tech Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: TanStack Query (React Query)
- **Charts**: Recharts
- **Forms**: React Hook Form
- **UI Components**: Shadcn UI

### Backend
- **Framework**: FastAPI
- **Database**: SQLite (dev) / PostgreSQL (production)
- **ORM**: SQLAlchemy
- **Authentication**: JWT with passlib
- **Validation**: Pydantic v2

## 📦 Project Structure

```
money-manager/
├── frontend/              # Next.js frontend application
│   ├── src/
│   │   ├── app/          # App router pages
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── lib/          # Utilities and API client
│   │   ├── stores/       # Zustand stores
│   │   └── types/        # TypeScript types
│   └── package.json
│
├── api/                   # FastAPI backend application
│   ├── app/
│   │   ├── api/          # API versioning
│   │   ├── core/         # Security and config
│   │   ├── crud/         # Database operations
│   │   ├── models/       # SQLAlchemy models
│   │   ├── routers/      # API endpoints
│   │   └── schemas/      # Pydantic schemas
│   ├── seed.py           # Database seeding script
│   └── requirements.txt
│
└── README.md
```

## 🛠️ Local Development Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- Git

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd money-manager
```

### 2. Backend Setup
```bash
cd api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database seed (optional - creates admin user and sample data)
python seed.py

# Start development server
fastapi dev app/main.py
```

Backend will run on `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will run on `http://localhost:3000`

## 👤 Default Users

### Admin User
- **Email**: `admin@moneymanager.com`
- **Password**: `admin123`
- Includes sample categories and transactions

### Test User
- **Email**: `test@example.com`
- **Password**: `password123`

## 🌐 Deployment to Vercel (Free Tier)

### Prerequisites
1. [Vercel Account](https://vercel.com/signup) (free)
2. [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres) database (free tier)

### Step 1: Prepare Your Repository
Ensure your code is pushed to GitHub/GitLab/Bitbucket.

### Step 2: Deploy Backend (API)
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Add New" → "Project"
3. Import your repository
4. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `api`
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

5. Add Environment Variables:
   ```
   DATABASE_URL=<your-vercel-postgres-url>
   SECRET_KEY=<generate-a-secure-random-key>
   ```

6. Deploy!

### Step 3: Set Up Vercel Postgres
1. In your Vercel project, go to "Storage"
2. Create a new Postgres database
3. Copy the `DATABASE_URL` connection string
4. Add it to your project's environment variables

### Step 4: Deploy Frontend
1. Create a new Vercel project for frontend
2. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

3. Add Environment Variable:
   ```
   NEXT_PUBLIC_API_URL=<your-backend-vercel-url>
   ```

4. Deploy!

### Step 5: Initialize Production Database
After deploying the backend, run the seed script:
```bash
# SSH into your Vercel deployment or use Vercel CLI
vercel env pull
python seed.py
```

## 📝 API Documentation

Once deployed, visit `https://your-api-url.vercel.app/docs` for interactive API documentation.

### Key Endpoints

#### Authentication
- `POST /api/v1/auth/users` - Register new user
- `POST /api/v1/auth/token` - Login and get JWT token

#### Categories
- `GET /api/v1/categories/` - List all categories
- `POST /api/v1/categories/` - Create category
- `PUT /api/v1/categories/{id}` - Update category
- `DELETE /api/v1/categories/{id}` - Delete category

#### Transactions
- `GET /api/v1/transactions/` - List transactions (with filters)
- `POST /api/v1/transactions/` - Create transaction
- `PUT /api/v1/transactions/{id}` - Update transaction
- `DELETE /api/v1/transactions/{id}` - Delete transaction

#### Analytics
- `GET /api/v1/analytics/monthly/{year}/{month}` - Monthly summary
- `GET /api/v1/analytics/categories` - Category breakdown

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- User-scoped data isolation
- CORS protection
- SQL injection prevention via ORM

## 🎨 UI Features

- Modern, clean interface with Tailwind CSS
- Dark mode support (coming soon)
- Responsive design for all screen sizes
- Loading states and error handling
- Smooth animations and transitions

## 📊 Analytics & Insights

- Monthly income vs expense summary
- Category-wise spending breakdown
- Visual charts with Recharts
- Date range filtering
- Transaction type filtering

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🐛 Known Issues

- Logout redirect requires manual localStorage clear in some cases (persistence middleware)
- Date filter UI may need adjustment on very small screens

## 🚧 Roadmap

- [ ] Dark mode support
- [ ] Budget tracking and alerts
- [ ] Recurring transactions
- [ ] Export to CSV/PDF
- [ ] Multi-user household accounts
- [ ] Mobile app (React Native)

## 💬 Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ using Next.js and FastAPI**
