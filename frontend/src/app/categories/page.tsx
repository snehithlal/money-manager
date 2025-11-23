"use client";

import { CategoryList } from "@/components/categories/category-list";

const CategoriesPage = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Categories</h1>
        <p className="text-gray-500">
          Manage your income and expense categories.
        </p>
      </div>
      <CategoryList />
    </div>
  );
};

export default CategoriesPage;
