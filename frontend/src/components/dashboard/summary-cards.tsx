"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ArrowDownCircle, ArrowUpCircle, Wallet } from "lucide-react";
import { useMonthlySummary } from "@/hooks/use-analytics";

export const SummaryCards = () => {
  const date = new Date();
  const { data: summary, isLoading } = useMonthlySummary(
    date.getFullYear(),
    date.getMonth() + 1
  );

  if (isLoading) {
    return (
      <div className="grid gap-4 md:grid-cols-3">
        {[...Array(3)].map((_, i) => (
          <div key={i} className="h-32 animate-pulse rounded-xl bg-gray-200" />
        ))}
      </div>
    );
  }

  return (
    <div className="grid gap-4 md:grid-cols-3">
      <Card className="transition-all duration-200 hover:shadow-md hover:-translate-y-1">
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-500">Total Income</CardTitle>
          <div className="rounded-full bg-green-100 p-2">
            <ArrowUpCircle className="h-4 w-4 text-green-600" />
          </div>
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold text-green-600">
            +₹{summary?.total_income.toFixed(2) || "0.00"}
          </div>
          <p className="text-xs text-muted-foreground">
            For this month
          </p>
        </CardContent>
      </Card>
      <Card className="transition-all duration-200 hover:shadow-md hover:-translate-y-1">
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-500">Total Expenses</CardTitle>
          <div className="rounded-full bg-red-100 p-2">
            <ArrowDownCircle className="h-4 w-4 text-red-600" />
          </div>
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold text-red-600">
            -₹{summary?.total_expense.toFixed(2) || "0.00"}
          </div>
          <p className="text-xs text-muted-foreground">
            For this month
          </p>
        </CardContent>
      </Card>
      <Card className="transition-all duration-200 hover:shadow-md hover:-translate-y-1">
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-500">Net Balance</CardTitle>
          <div className="rounded-full bg-blue-100 p-2">
            <Wallet className="h-4 w-4 text-blue-600" />
          </div>
        </CardHeader>
        <CardContent>
          <div className={`text-2xl font-bold ${
            (summary?.balance || 0) >= 0 ? "text-blue-600" : "text-red-600"
          }`}>
            ₹{summary?.balance.toFixed(2) || "0.00"}
          </div>
          <p className="text-xs text-muted-foreground">
            Current balance
          </p>
        </CardContent>
      </Card>
    </div>
  );
};
