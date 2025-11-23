"use client";

import { TransactionList } from "@/components/transactions/transaction-list";

const TransactionsPage = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Transactions</h1>
        <p className="text-gray-500">
          View and manage your financial transactions.
        </p>
      </div>
      <TransactionList />
    </div>
  );
};

export default TransactionsPage;
