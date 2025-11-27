#!/usr/bin/env python3
"""
Test the new backend structure.
"""
import sys
import os

# Simulate Vercel execution from root
# Vercel runs from root, but api/index.py adds backend to path
# Let's try to import api.index
try:
    # Add root to path so we can import api.index
    sys.path.insert(0, os.getcwd())

    from api.index import app
    print("✅ SUCCESS: Imported app from api/index.py")
    print(f"   Type: {type(app).__name__}")

except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
