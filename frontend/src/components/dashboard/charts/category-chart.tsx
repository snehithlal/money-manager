"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useCategorySummary } from "@/hooks/use-analytics";
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip, Legend } from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#8884d8", "#82ca9d"];

export const CategoryChart = () => {
  const { data: categoryData, isLoading } = useCategorySummary("expense");

  if (isLoading) {
    return <div className="h-[300px] animate-pulse rounded-xl bg-gray-200" />;
  }

  const data = categoryData?.map(item => ({
    name: item.category_name,
    value: item.total_amount
  })) || [];

  return (
    <Card className="col-span-3">
      <CardHeader>
        <CardTitle>Expenses by Category</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[300px]">
          {data.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={data}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  fill="#8884d8"
                  paddingAngle={5}
                  dataKey="value"
                >
                  {data.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip
                  formatter={(value: number) => `₹${value.toFixed(2)}`}
                />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex h-full items-center justify-center text-gray-500">
              No expense data available
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};
