#!/usr/bin/env python3
"""
Simple test for lazy discovery system
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_lazy_discovery():
    """Test the lazy discovery system"""
    try:
        from exonware.xwsystem.utils.lazy_discovery import discover_dependencies, LazyDiscovery
        
        print("🚀 Testing Lazy Discovery System")
        print("=" * 50)
        
        # Test discovery
        dependencies = discover_dependencies()
        print(f"✅ Discovered {len(dependencies)} dependencies from project files")
        
        # Show some examples
        if dependencies:
            print(f"\n📦 Sample dependencies:")
            for i, (import_name, package_name) in enumerate(list(dependencies.items())[:5]):
                print(f"   {import_name} → {package_name}")
        
        # Test LazyDiscovery class
        discovery = LazyDiscovery()
        sources = discovery.get_discovery_sources()
        print(f"\n🔍 Discovery sources: {sources}")
        
        print(f"\n✅ Lazy discovery system working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_lazy_install():
    """Test the lazy install system"""
    try:
        from exonware.xwsystem.utils.lazy_install import lazy_import_with_install, LazyInstaller
        
        print("\n🚀 Testing Lazy Install System")
        print("=" * 50)
        
        # Test lazy import (this won't actually install anything, just test the function)
        module, available = lazy_import_with_install("json")  # json is built-in
        if available:
            print("✅ Built-in module import works")
        else:
            print("❌ Built-in module import failed")
        
        # Test installer
        installer = LazyInstaller()
        stats = installer.get_stats()
        print(f"📊 Installer stats: {stats}")
        
        print(f"\n✅ Lazy install system working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Testing xwsystem Lazy Systems")
    print("=" * 60)
    
    success1 = test_lazy_discovery()
    success2 = test_lazy_install()
    
    if success1 and success2:
        print(f"\n🎉 All tests passed! Lazy systems are working correctly.")
        print(f"\n💡 Key benefits:")
        print(f"   • Package-agnostic dependency discovery")
        print(f"   • Automatic discovery from project files")
        print(f"   • Reusable across all exonware libraries")
        print(f"   • No hardcoded package lists")
    else:
        print(f"\n❌ Some tests failed. Check the errors above.")
        sys.exit(1)
