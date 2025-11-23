"use client";

import { usePathname } from "next/navigation";
import { Sidebar } from "./sidebar";
import { Header } from "./header";
import { Modal } from "@/components/ui/modal";
import ProtectedRoute from "@/components/auth/protected-route";

export const AppLayout = ({ children }: { children: React.ReactNode }) => {
  const pathname = usePathname();
  const isPublicPage = ["/login", "/register"].includes(pathname);

  return (
    <ProtectedRoute>
      <div className="flex h-screen bg-gray-50">
        {!isPublicPage && <Sidebar />}
        <div className="flex flex-1 flex-col overflow-hidden">
          {!isPublicPage && <Header />}
          <main className={isPublicPage ? "flex-1 overflow-y-auto" : "flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8"}>
            {children}
          </main>
        </div>
        <Modal />
      </div>
    </ProtectedRoute>
  );
};
