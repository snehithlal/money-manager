"use client";

import { useEffect } from "react";
import { useRouter, usePathname } from "next/navigation";
import { useAuthStore } from "@/stores/auth-store";

export default function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);
  const token = useAuthStore((state) => state.token);

  useEffect(() => {
    // If not authenticated and not on public pages, redirect to login
    const publicPaths = ["/login", "/register"];
    if (!isAuthenticated && !token && !publicPaths.includes(pathname)) {
      router.push("/login");
    }

    // REMOVED: Auto-redirect to dashboard if authenticated.
    // This was causing infinite loops when the token was invalid (401) but local state said authenticated.
    // Now, if a user lands on /login, they stay there, allowing them to re-login.
  }, [isAuthenticated, token, pathname, router]);

  // If not authenticated and on a protected route, don't render children (to prevent flash)
  const publicPaths = ["/login", "/register"];
  if (!isAuthenticated && !token && !publicPaths.includes(pathname)) {
    return null;
  }

  return <>{children}</>;
}
