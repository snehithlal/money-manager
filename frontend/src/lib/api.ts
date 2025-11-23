/**
 * API Service Functions
 *
 * All API calls using Axios.
 * These functions are used by React Query hooks.
 */

import apiClient from './api-client';
import type {
  Category,
  CategoryCreate,
  CategoryUpdate,
  Transaction,
  TransactionCreate,
  TransactionUpdate,
  TransactionFilters,
  MonthlySummary,
  CategorySummary,
} from '@/types/api';

// ============================================================================
// Categories API
// ============================================================================

export const categoriesApi = {
  // Get all categories
  getAll: async (type?: 'income' | 'expense'): Promise<Category[]> => {
    const params = type ? { type } : {};
    const response = await apiClient.get('/categories', { params });
    return response.data;
  },

  // Get single category
  getById: async (id: number): Promise<Category> => {
    const response = await apiClient.get(`/categories/${id}`);
    return response.data;
  },

  // Create category
  create: async (data: CategoryCreate): Promise<Category> => {
    const response = await apiClient.post('/categories', data);
    return response.data;
  },

  // Update category
  update: async (id: number, data: CategoryUpdate): Promise<Category> => {
    const response = await apiClient.put(`/categories/${id}`, data);
    return response.data;
  },

  // Delete category
  delete: async (id: number): Promise<Category> => {
    const response = await apiClient.delete(`/categories/${id}`);
    return response.data;
  },
};

// ============================================================================
// Transactions API
// ============================================================================

export const transactionsApi = {
  // Get all transactions with filters
  getAll: async (filters?: TransactionFilters): Promise<Transaction[]> => {
    const response = await apiClient.get('/transactions', {
      params: filters,
    });
    return response.data;
  },

  // Get single transaction
  getById: async (id: number): Promise<Transaction> => {
    const response = await apiClient.get(`/transactions/${id}`);
    return response.data;
  },

  // Create transaction
  create: async (data: TransactionCreate): Promise<Transaction> => {
    const response = await apiClient.post('/transactions', data);
    return response.data;
  },

  // Update transaction
  update: async (id: number, data: TransactionUpdate): Promise<Transaction> => {
    const response = await apiClient.put(`/transactions/${id}`, data);
    return response.data;
  },

  // Delete transaction
  delete: async (id: number): Promise<Transaction> => {
    const response = await apiClient.delete(`/transactions/${id}`);
    return response.data;
  },
};

// ============================================================================
// Analytics API (placeholder for future implementation)
// ============================================================================

export const analyticsApi = {
  // Get monthly summary
  getMonthlySummary: async (year: number, month: number): Promise<MonthlySummary> => {
    const response = await apiClient.get(`/analytics/monthly/${year}/${month}`);
    return response.data;
  },

  // Get category summary
  getCategorySummary: async (type?: 'income' | 'expense'): Promise<CategorySummary[]> => {
    const params = type ? { type } : {};
    const response = await apiClient.get('/analytics/categories', { params });
    return response.data;
  },
};
