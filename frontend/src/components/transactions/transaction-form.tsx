"use client";

import { useForm } from "react-hook-form";
import { useCreateTransaction, useUpdateTransaction } from "@/hooks/use-transactions";
import { useCategories } from "@/hooks/use-categories";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { useUIStore } from "@/stores/ui-store";
import { Transaction, TransactionCreate } from "@/types/api";
import { useEffect } from "react";

interface TransactionFormProps {
  transactionToEdit?: Transaction | null;
  onSuccess?: () => void;
}

export const TransactionForm = ({ transactionToEdit, onSuccess }: TransactionFormProps) => {
  const { closeModal } = useUIStore();
  const createTransaction = useCreateTransaction();
  const updateTransaction = useUpdateTransaction();

  // Fetch categories for the dropdown
  const { data: categories } = useCategories();

  const { register, handleSubmit, reset, setValue, watch, formState: { errors } } = useForm<TransactionCreate>({
    defaultValues: {
      amount: 0,
      description: "",
      date: new Date().toISOString().split('T')[0],
      type: "expense",
      category_id: 0,
    },
  });

  const selectedType = watch("type");

  // Filter categories based on selected transaction type
  const filteredCategories = categories?.filter(c => c.type === selectedType) || [];

  // Populate form if editing
  useEffect(() => {
    if (transactionToEdit) {
      setValue("amount", transactionToEdit.amount);
      setValue("description", transactionToEdit.description || "");
      setValue("date", transactionToEdit.date);
      setValue("type", transactionToEdit.type);
      setValue("category_id", transactionToEdit.category_id);
    }
  }, [transactionToEdit, setValue]);

  const onSubmit = (data: TransactionCreate) => {
    // Ensure amount is a number
    const formattedData = {
      ...data,
      amount: Number(data.amount),
      category_id: Number(data.category_id),
    };

    if (transactionToEdit) {
      updateTransaction.mutate(
        { id: transactionToEdit.id, data: formattedData },
        {
          onSuccess: () => {
            reset();
            if (onSuccess) onSuccess();
            closeModal();
          },
        }
      );
    } else {
      createTransaction.mutate(formattedData, {
        onSuccess: () => {
          reset();
          if (onSuccess) onSuccess();
          closeModal();
        },
      });
    }
  };

  const isLoading = createTransaction.isPending || updateTransaction.isPending;

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="type">Type</Label>
          <Select
            id="type"
            {...register("type", { required: "Type is required" })}
            onChange={(e) => {
              setValue("type", e.target.value as "income" | "expense");
              // Reset category when type changes
              setValue("category_id", 0);
            }}
          >
            <option value="expense">Expense</option>
            <option value="income">Income</option>
          </Select>
        </div>

        <div className="space-y-2">
          <Label htmlFor="amount">Amount</Label>
          <Input
            id="amount"
            type="number"
            step="0.01"
            placeholder="0.00"
            {...register("amount", {
              required: "Amount is required",
              min: { value: 0.01, message: "Amount must be greater than 0" }
            })}
          />
          {errors.amount && (
            <p className="text-sm text-red-500">{errors.amount.message}</p>
          )}
        </div>
      </div>

      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <Label htmlFor="date">Date</Label>
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={() => setValue("date", new Date().toISOString().split('T')[0])}
            className="h-7 text-xs text-blue-600 hover:text-blue-700"
          >
            Today
          </Button>
        </div>
        <Input
          id="date"
          type="date"
          {...register("date", { required: "Date is required" })}
        />
        {errors.date && (
          <p className="text-sm text-red-500">{errors.date.message}</p>
        )}
      </div>

      <div className="space-y-2">
        <Label htmlFor="category_id">Category</Label>
        <Select
          id="category_id"
          {...register("category_id", {
            required: "Category is required",
            validate: (value) => value !== 0 || "Please select a category"
          })}
        >
          <option value={0}>Select a category</option>
          {filteredCategories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.icon} {category.name}
            </option>
          ))}
        </Select>
        {errors.category_id && (
          <p className="text-sm text-red-500">{errors.category_id.message}</p>
        )}
      </div>

      <div className="space-y-2">
        <Label htmlFor="description">Description (Optional)</Label>
        <Textarea
          id="description"
          placeholder="What was this for?"
          {...register("description")}
        />
      </div>

      <div className="flex justify-end gap-2 pt-4">
        <Button type="button" variant="outline" onClick={closeModal}>
          Cancel
        </Button>
        <Button type="submit" disabled={isLoading}>
          {isLoading ? "Saving..." : transactionToEdit ? "Update" : "Create"}
        </Button>
      </div>
    </form>
  );
};
