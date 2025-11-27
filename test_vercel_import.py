#!/usr/bin/env python3
"""
Test script to simulate Vercel's serverless function execution locally.
This helps verify that api/index.py works correctly before deploying.
"""

import sys
import os

# Simulate Vercel's execution environment
# Vercel runs from /var/task/, we simulate by changing to api/
os.chdir(os.path.join(os.path.dirname(__file__), 'api'))

# Now try to import the handler
try:
    from index import handler
    print("✅ SUCCESS: Handler imported successfully!")
    print(f"   Handler type: {type(handler)}")
    print(f"   Handler: {handler}")

    # Test if it's a valid FastAPI app
    if hasattr(handler, 'routes'):
        print(f"   Routes found: {len(handler.routes)}")
        print("\n📋 Available routes:")
        for route in handler.routes:
            if hasattr(route, 'path'):
                methods = getattr(route, 'methods', ['GET'])
                print(f"   - {list(methods)[0] if methods else 'GET'} {route.path}")

    print("\n🎉 Your api/index.py is ready for Vercel!")

except Exception as e:
    print(f"❌ ERROR: Failed to import handler")
    print(f"   Error: {e}")
    print(f"   Type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
