"use client";

import { useCategories, useDeleteCategory } from "@/hooks/use-categories";
import { useUIStore } from "@/stores/ui-store";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Edit, Trash2, Plus } from "lucide-react";
import { Category } from "@/types/api";
import { useState } from "react";
import { CategoryForm } from "./category-form";

export const CategoryList = () => {
  const { data: categories, isLoading, error } = useCategories();
  const deleteCategory = useDeleteCategory();
  const { openModal } = useUIStore();

  // Local state for editing since we need to pass the category to the form
  // Ideally this would be in the store or we'd fetch by ID in the form
  const [editingCategory, setEditingCategory] = useState<Category | null>(null);

  const handleDelete = async (id: number) => {
    if (confirm("Are you sure you want to delete this category?")) {
      deleteCategory.mutate(id);
    }
  };

  const handleEdit = (category: Category) => {
    // For now, we'll just open the modal and let the form handle it
    // But the current Modal implementation doesn't support passing props to the form
    // We might need to update the store to hold the "editingId"
    // Or just render the form directly here if we want inline editing

    // For simplicity in this version, let's just log it
    console.log("Edit category", category);
    alert("Edit feature coming in next update! (Requires store update)");
  };

  if (isLoading) {
    return (
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="h-24 animate-pulse rounded-lg bg-gray-200" />
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-lg bg-red-50 p-4 text-red-600">
        Error loading categories. Please try again.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">All Categories</h2>
        <Button onClick={() => openModal("category")}>
          <Plus className="mr-2 h-4 w-4" />
          Add Category
        </Button>
      </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {categories?.map((category) => (
          <Card key={category.id} className="overflow-hidden transition-shadow hover:shadow-md">
            <CardContent className="p-0">
              <div className="flex items-center justify-between p-4">
                <div className="flex items-center gap-3">
                  <div
                    className="flex h-10 w-10 items-center justify-center rounded-full text-xl"
                    style={{ backgroundColor: `${category.color}20` }}
                  >
                    {category.icon}
                  </div>
                  <div>
                    <h3 className="font-medium">{category.name}</h3>
                    <p className="text-xs text-gray-500 capitalize">{category.type}</p>
                  </div>
                </div>
                <div className="flex gap-1">
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 text-gray-500 hover:text-blue-600"
                    onClick={() => handleEdit(category)}
                  >
                    <Edit className="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 text-gray-500 hover:text-red-600"
                    onClick={() => handleDelete(category.id)}
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </div>
              <div
                className="h-1 w-full"
                style={{ backgroundColor: category.color }}
              />
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};
