"use client";

import { SummaryCards } from "@/components/dashboard/summary-cards";
import { CategoryChart } from "@/components/dashboard/charts/category-chart";
import { TransactionList } from "@/components/transactions/transaction-list";

const DashboardPage = () => {
  return (
    <div className="space-y-8">
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-700 p-8 text-white shadow-lg">
        <div className="relative z-10">
          <h1 className="text-3xl font-bold tracking-tight">Welcome back!</h1>
          <p className="mt-2 text-blue-100">
            Here's what's happening with your finances today.
          </p>
        </div>
        <div className="absolute -right-10 -top-10 h-64 w-64 rounded-full bg-white/10 blur-3xl" />
        <div className="absolute -bottom-10 -left-10 h-64 w-64 rounded-full bg-blue-500/20 blur-3xl" />
      </div>

      <SummaryCards />

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-7">
        <div className="col-span-4">
          <div className="mb-4">
            <h2 className="text-lg font-semibold">Recent Activity</h2>
          </div>
          <TransactionList />
        </div>
        <div className="col-span-3">
          <CategoryChart />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
