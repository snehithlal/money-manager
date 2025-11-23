/**
 * React Query Hooks for Analytics
 *
 * Custom hooks for fetching analytics data.
 */

import { useQuery } from '@tanstack/react-query';
import { analyticsApi } from '@/lib/api';

// Query keys
export const analyticsKeys = {
  all: ['analytics'] as const,
  monthly: (year: number, month: number) => [...analyticsKeys.all, 'monthly', { year, month }] as const,
  categories: (type?: 'income' | 'expense') => [...analyticsKeys.all, 'categories', { type }] as const,
};

// ============================================================================
// Queries
// ============================================================================

/**
 * Get monthly summary
 */
export const useMonthlySummary = (year: number, month: number) => {
  return useQuery({
    queryKey: analyticsKeys.monthly(year, month),
    queryFn: () => analyticsApi.getMonthlySummary(year, month),
  });
};

/**
 * Get category summary
 */
export const useCategorySummary = (type?: 'income' | 'expense') => {
  return useQuery({
    queryKey: analyticsKeys.categories(type),
    queryFn: () => analyticsApi.getCategorySummary(type),
  });
};
