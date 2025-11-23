"use client";

import { AnalyticsDashboard } from "@/components/analytics/analytics-dashboard";

const AnalyticsPage = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Analytics</h1>
        <p className="text-gray-500">
          Detailed insights into your spending habits.
        </p>
      </div>
      <AnalyticsDashboard />
    </div>
  );
};

export default AnalyticsPage;
