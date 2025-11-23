"use client";

import { useForm } from "react-hook-form";
import { useCreateCategory, useUpdateCategory } from "@/hooks/use-categories";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select } from "@/components/ui/select";
import { useUIStore } from "@/stores/ui-store";
import { Category, CategoryCreate } from "@/types/api";
import { useEffect } from "react";

interface CategoryFormProps {
  categoryToEdit?: Category | null;
  onSuccess?: () => void;
}

export const CategoryForm = ({ categoryToEdit, onSuccess }: CategoryFormProps) => {
  const { closeModal } = useUIStore();
  const createCategory = useCreateCategory();
  const updateCategory = useUpdateCategory();

  const { register, handleSubmit, reset, setValue, formState: { errors } } = useForm<CategoryCreate>({
    defaultValues: {
      name: "",
      type: "expense",
      color: "#6366f1",
      icon: "💰",
    },
  });

  // Populate form if editing
  useEffect(() => {
    if (categoryToEdit) {
      setValue("name", categoryToEdit.name);
      setValue("type", categoryToEdit.type);
      setValue("color", categoryToEdit.color);
      setValue("icon", categoryToEdit.icon);
    }
  }, [categoryToEdit, setValue]);

  const onSubmit = (data: CategoryCreate) => {
    if (categoryToEdit) {
      updateCategory.mutate(
        { id: categoryToEdit.id, data },
        {
          onSuccess: () => {
            reset();
            if (onSuccess) onSuccess();
            closeModal();
          },
        }
      );
    } else {
      createCategory.mutate(data, {
        onSuccess: () => {
          reset();
          if (onSuccess) onSuccess();
          closeModal();
        },
      });
    }
  };

  const isLoading = createCategory.isPending || updateCategory.isPending;

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="name">Name</Label>
        <Input
          id="name"
          placeholder="e.g. Groceries"
          {...register("name", { required: "Name is required" })}
        />
        {errors.name && (
          <p className="text-sm text-red-500">{errors.name.message}</p>
        )}
      </div>

      <div className="space-y-2">
        <Label htmlFor="type">Type</Label>
        <Select
          id="type"
          {...register("type", { required: "Type is required" })}
        >
          <option value="expense">Expense</option>
          <option value="income">Income</option>
        </Select>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="color">Color</Label>
          <div className="flex gap-2">
            <Input
              id="color"
              type="color"
              className="w-12 p-1 h-10"
              {...register("color")}
            />
            <Input
              type="text"
              placeholder="#000000"
              {...register("color")}
            />
          </div>
        </div>

        <div className="space-y-2">
          <Label htmlFor="icon">Icon</Label>
          <Input
            id="icon"
            placeholder="e.g. 🍔"
            {...register("icon")}
          />
        </div>
      </div>

      <div className="flex justify-end gap-2 pt-4">
        <Button type="button" variant="outline" onClick={closeModal}>
          Cancel
        </Button>
        <Button type="submit" disabled={isLoading}>
          {isLoading ? "Saving..." : categoryToEdit ? "Update" : "Create"}
        </Button>
      </div>
    </form>
  );
};
