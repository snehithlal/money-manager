"use client";

import { useTransactions, useDeleteTransaction } from "@/hooks/use-transactions";
import { useUIStore } from "@/stores/ui-store";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Edit, Trash2, Plus, ArrowUpCircle, ArrowDownCircle } from "lucide-react";
import { Transaction } from "@/types/api";
import { useState } from "react";
import { cn } from "@/lib/utils";

export const TransactionList = () => {
  const { data: transactions, isLoading, error } = useTransactions();
  const deleteTransaction = useDeleteTransaction();
  const { openModal } = useUIStore();

  const handleDelete = async (id: number) => {
    if (confirm("Are you sure you want to delete this transaction?")) {
      deleteTransaction.mutate(id);
    }
  };

  const handleEdit = (transaction: Transaction) => {
    console.log("Edit transaction", transaction);
    alert("Edit feature coming in next update! (Requires store update)");
  };

  if (isLoading) {
    return (
      <div className="space-y-4">
        {[...Array(5)].map((_, i) => (
          <div key={i} className="h-20 animate-pulse rounded-lg bg-gray-200" />
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-lg bg-red-50 p-4 text-red-600">
        Error loading transactions. Please try again.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">Recent Transactions</h2>
        <Button onClick={() => openModal("transaction")}>
          <Plus className="mr-2 h-4 w-4" />
          Add Transaction
        </Button>
      </div>

      <div className="space-y-4">
        {transactions?.length === 0 && (
          <div className="text-center py-10 text-gray-500">
            No transactions found. Add one to get started!
          </div>
        )}

        {transactions?.map((transaction) => (
          <Card key={transaction.id} className="overflow-hidden transition-shadow hover:shadow-md">
            <CardContent className="p-4 flex items-center justify-between">
              <div className="flex items-center gap-4">
                <div
                  className={cn(
                    "flex h-12 w-12 items-center justify-center rounded-full",
                    transaction.type === "income" ? "bg-green-100 text-green-600" : "bg-red-100 text-red-600"
                  )}
                >
                  {transaction.type === "income" ? (
                    <ArrowUpCircle className="h-6 w-6" />
                  ) : (
                    <ArrowDownCircle className="h-6 w-6" />
                  )}
                </div>

                <div>
                  <div className="flex items-center gap-2">
                    <h3 className="font-medium">{transaction.category.icon} {transaction.category.name}</h3>
                    <span className="text-xs text-gray-400">• {new Date(transaction.date).toLocaleDateString()}</span>
                  </div>
                  <p className="text-sm text-gray-500">
                    {transaction.description || "No description"}
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <span
                  className={cn(
                    "font-bold text-lg",
                    transaction.type === "income" ? "text-green-600" : "text-red-600"
                  )}
                >
                  {transaction.type === "income" ? "+" : "-"}${transaction.amount.toFixed(2)}
                </span>

                <div className="flex gap-1">
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 text-gray-500 hover:text-blue-600"
                    onClick={() => handleEdit(transaction)}
                  >
                    <Edit className="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 text-gray-500 hover:text-red-600"
                    onClick={() => handleDelete(transaction.id)}
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};
