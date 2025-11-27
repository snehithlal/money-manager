"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select } from "@/components/ui/select";
import { useCategories } from "@/hooks/use-categories";
import { TransactionFilters } from "@/types/api";
import { X } from "lucide-react";

interface TransactionFiltersProps {
  filters: TransactionFilters;
  onFilterChange: (filters: TransactionFilters) => void;
}

export const TransactionFiltersComponent = ({
  filters,
  onFilterChange,
}: TransactionFiltersProps) => {
  const { data: categories } = useCategories();

  const handleTypeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    onFilterChange({
      ...filters,
      type: value === "all" ? undefined : (value as "income" | "expense"),
    });
  };

  const handleCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    onFilterChange({
      ...filters,
      category_id: value === "all" ? undefined : Number(value),
    });
  };

  const handleDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onFilterChange({
      ...filters,
      [e.target.name]: e.target.value || undefined,
    });
  };

  const clearFilters = () => {
    onFilterChange({});
  };

  const hasFilters = Object.values(filters).some((v) => v !== undefined);

  return (
    <div className="rounded-lg border bg-white p-4 shadow-sm">
      <div className="flex flex-wrap items-center gap-3">
        <Select
          value={filters.type || "all"}
          onChange={handleTypeChange}
          className="w-32 text-gray-900 border-gray-300"
        >
          <option value="all">All Types</option>
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </Select>

        <Select
          value={filters.category_id?.toString() || "all"}
          onChange={handleCategoryChange}
          className="w-40 text-gray-900 border-gray-300"
        >
          <option value="all">All Categories</option>
          {categories?.map((category) => (
            <option key={category.id} value={category.id.toString()}>
              {category.icon} {category.name}
            </option>
          ))}
        </Select>

        <Input
          type="date"
          name="start_date"
          value={filters.start_date || ""}
          onChange={handleDateChange}
          className="w-36 text-gray-900 border-gray-300"
        />

        <span className="text-gray-500 font-medium">to</span>

        <Input
          type="date"
          name="end_date"
          value={filters.end_date || ""}
          onChange={handleDateChange}
          className="w-36 text-gray-900 border-gray-300"
        />

        {hasFilters && (
          <Button
            variant="ghost"
            size="icon"
            onClick={clearFilters}
            className="h-10 w-10 text-gray-500 hover:text-red-600"
            title="Clear all filters"
          >
            <X className="h-4 w-4" />
          </Button>
        )}
      </div>
    </div>
  );
};
