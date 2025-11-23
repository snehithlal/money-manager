/**
 * TypeScript types for API responses
 *
 * These match the Pydantic schemas from the FastAPI backend.
 */

// Transaction types
export type TransactionType = 'income' | 'expense';

// User interface
export interface User {
  id: number;
  email: string;
  is_active: boolean;
}

// Category interfaces
export interface Category {
  id: number;
  name: string;
  type: 'income' | 'expense';
  color: string;
  icon: string;
}

export interface CategoryCreate {
  name: string;
  type: TransactionType;
  color?: string;
  icon?: string;
}

export interface CategoryUpdate {
  name?: string;
  type?: TransactionType;
  color?: string;
  icon?: string;
}

// Transaction interfaces
export interface Transaction {
  id: number;
  amount: number;
  description?: string;
  date: string; // ISO date string
  category_id: number;
  type: TransactionType;
  category: Category; // Nested category
}

export interface TransactionCreate {
  amount: number;
  description?: string;
  date: string; // ISO date string (YYYY-MM-DD)
  category_id: number;
  type: TransactionType;
}

export interface TransactionUpdate {
  amount?: number;
  description?: string;
  date?: string;
  category_id?: number;
  type?: TransactionType;
}

// Analytics interfaces
export interface MonthlySummary {
  month: string; // YYYY-MM format
  total_income: number;
  total_expense: number;
  balance: number;
}

export interface CategorySummary {
  category_id: number;
  category_name: string;
  category_color: string;
  category_icon: string;
  total_amount: number;
  transaction_count: number;
}

// API Query parameters
export interface TransactionFilters {
  type?: TransactionType;
  category_id?: number;
  start_date?: string;
  end_date?: string;
  skip?: number;
  limit?: number;
}
