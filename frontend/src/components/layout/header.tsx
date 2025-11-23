"use client";

import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { useUIStore } from "@/stores/ui-store";

export const Header = () => {
  const { toggleSidebar } = useUIStore();

  return (
    <header className="sticky top-0 z-30 flex h-16 w-full items-center justify-between border-b border-gray-200 bg-white px-4 shadow-sm sm:px-6 lg:px-8 transition-all duration-200">
      <div className="flex items-center">
        <Button
          variant="ghost"
          size="icon"
          className="mr-4 lg:hidden"
          onClick={toggleSidebar}
        >
          <Menu className="h-5 w-5" />
          <span className="sr-only">Open sidebar</span>
        </Button>
        <h1 className="text-lg font-semibold text-gray-900">Dashboard</h1>
      </div>

      <div className="flex items-center gap-4">
        {/* Add user profile or other actions here */}
        <div className="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-medium text-sm">
          US
        </div>
      </div>
    </header>
  );
};
