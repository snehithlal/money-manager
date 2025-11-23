"use client";

import * as React from "react";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";
import { useUIStore } from "@/stores/ui-store";
import { Button } from "@/components/ui/button";
import { CategoryForm } from "@/components/categories/category-form";
// Import TransactionForm when created
import { TransactionForm } from "@/components/transactions/transaction-form";

export const Modal = () => {
  const { isModalOpen, modalType, closeModal } = useUIStore();

  if (!isModalOpen) return null;

  const title = modalType === "category" ? "Category" : "Transaction";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-sm">
      <div
        className={cn(
          "w-full max-w-md overflow-hidden rounded-lg bg-white shadow-xl transition-all",
          "animate-in fade-in zoom-in-95 duration-200"
        )}
      >
        <div className="flex items-center justify-between border-b px-6 py-4">
          <h2 className="text-lg font-semibold">{title}</h2>
          <Button
            variant="ghost"
            size="icon"
            className="h-8 w-8"
            onClick={closeModal}
          >
            <X className="h-4 w-4" />
            <span className="sr-only">Close</span>
          </Button>
        </div>

        <div className="p-6">
          {modalType === "category" && <CategoryForm />}
          {modalType === "transaction" && <TransactionForm />}
        </div>
      </div>
    </div>
  );
};
