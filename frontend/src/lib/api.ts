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
    const response = await apiClient.get('/api/v1/categories', { params });
    return response.data;
  },

  // Get single category
  getById: async (id: number): Promise<Category> => {
    const response = await apiClient.get(`/api/v1/categories/${id}`);
    return response.data;
  },

  // Create category
  create: async (data: CategoryCreate): Promise<Category> => {
    const response = await apiClient.post('/api/v1/categories', data);
    return response.data;
  },

  // Update category
  update: async (id: number, data: CategoryUpdate): Promise<Category> => {
    const response = await apiClient.put(`/api/v1/categories/${id}`, data);
    return response.data;
  },

  // Delete category
  delete: async (id: number): Promise<Category> => {
    const response = await apiClient.delete(`/api/v1/categories/${id}`);
    return response.data;
  },
};

// ============================================================================
// Transactions API
// ============================================================================

export const transactionsApi = {
  // Get all transactions with filters
  getAll: async (filters?: TransactionFilters): Promise<Transaction[]> => {
    const response = await apiClient.get('/api/v1/transactions', {
      params: filters,
    });
    return response.data;
  },

  // Get single transaction
  getById: async (id: number): Promise<Transaction> => {
    const response = await apiClient.get(`/api/v1/transactions/${id}`);
    return response.data;
  },

  // Create transaction
  create: async (data: TransactionCreate): Promise<Transaction> => {
    const response = await apiClient.post('/api/v1/transactions', data);
    return response.data;
  },

  // Update transaction
  update: async (id: number, data: TransactionUpdate): Promise<Transaction> => {
    const response = await apiClient.put(`/api/v1/transactions/${id}`, data);
    return response.data;
  },

  // Delete transaction
  delete: async (id: number): Promise<Transaction> => {
    const response = await apiClient.delete(`/api/v1/transactions/${id}`);
    return response.data;
  },
};

// ============================================================================
// Analytics API (placeholder for future implementation)
// ============================================================================

export const analyticsApi = {
  // Get monthly summary
  getMonthlySummary: async (year: number, month: number): Promise<MonthlySummary> => {
    const response = await apiClient.get(`/api/v1/analytics/monthly/${year}/${month}`);
    return response.data;
  },

  // Get category summary
  getCategorySummary: async (type?: 'income' | 'expense'): Promise<CategorySummary[]> => {
    const params = type ? { type } : {};
    const response = await apiClient.get('/api/v1/analytics/categories', { params });
    return response.data;
  },
};
