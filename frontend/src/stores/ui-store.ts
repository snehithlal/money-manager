/**
 * Zustand Store for UI State
 *
 * Client-side state management for UI-specific state.
 * Server state is managed by React Query.
 */

import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface UIState {
  // Sidebar state
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
  setSidebarOpen: (open: boolean) => void;

  // Modal state
  isModalOpen: boolean;
  modalType: 'category' | 'transaction' | null;
  modalData: any; // Data to pre-fill modal (for edit mode)
  openModal: (type: 'category' | 'transaction') => void;
  closeModal: () => void;
  setModalData: (data: any) => void;

  // Filter state
  selectedType: 'income' | 'expense' | 'all';
  setSelectedType: (type: 'income' | 'expense' | 'all') => void;

  // Date range
  dateRange: {
    start: string | null;
    end: string | null;
  };
  setDateRange: (start: string | null, end: string | null) => void;
}

export const useUIStore = create<UIState>()(
  devtools(
    persist(
      (set) => ({
        // Initial state
        isSidebarOpen: true,
        isModalOpen: false,
        modalType: null,
        modalData: null,
        selectedType: 'all',
        dateRange: {
          start: null,
          end: null,
        },

        // Actions
        toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
        setSidebarOpen: (open) => set({ isSidebarOpen: open }),

        openModal: (type) => set({ isModalOpen: true, modalType: type }),
        closeModal: () => set({ isModalOpen: false, modalType: null, modalData: null }),
        setModalData: (data) => set({ modalData: data }),

        setSelectedType: (type) => set({ selectedType: type }),

        setDateRange: (start, end) => set({ dateRange: { start, end } }),
      }),
      {
        name: 'money-manager-ui', // localStorage key
        partialize: (state) => ({
          // Only persist these fields
          isSidebarOpen: state.isSidebarOpen,
          selectedType: state.selectedType,
        }),
      }
    ),
    { name: 'UIStore' }
  )
);
