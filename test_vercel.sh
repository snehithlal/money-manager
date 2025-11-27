#!/usr/bin/env bash
# Test Vercel deployment locally
# This simulates how Vercel will import your FastAPI app

echo "🧪 Testing Vercel import locally..."
echo ""

cd api

python3 << 'EOF'
import sys
import os

# Add current directory to path (simulates Vercel environment)
sys.path.insert(0, os.getcwd())

try:
    # Import the handler (what Vercel does)
    from index import handler

    print("✅ SUCCESS: Handler imported successfully!")
    print(f"   Type: {type(handler).__name__}")
    print(f"   Title: {handler.title if hasattr(handler, 'title') else 'N/A'}")

    # Check routes
    if hasattr(handler, 'routes'):
        print(f"   Routes: {len(handler.routes)} endpoints found")

    print("\n🎉 Your app is ready for Vercel deployment!")

except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    print("\n💡 Fix: Make sure all dependencies are installed")
    print("   Run: pip install -r requirements.txt")
    sys.exit(1)

except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
EOF

echo ""
echo "📝 To test the API locally, run:"
echo "   cd api && fastapi dev app/main.py"
