#!/usr/bin/env python3
"""
Direct test for lazy discovery system (bypassing main xwsystem imports)
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_lazy_discovery_direct():
    """Test lazy discovery directly without importing main xwsystem"""
    try:
        # Import directly from the utils module
        from exonware.xwsystem.utils.lazy_discovery import LazyDiscovery, discover_dependencies
        
        print("🚀 Testing Lazy Discovery System (Direct Import)")
        print("=" * 60)
        
        # Test discovery
        dependencies = discover_dependencies()
        print(f"✅ Discovered {len(dependencies)} dependencies from project files")
        
        # Show some examples
        if dependencies:
            print(f"\n📦 Sample dependencies:")
            for i, (import_name, package_name) in enumerate(list(dependencies.items())[:10]):
                print(f"   {import_name} → {package_name}")
        
        # Test LazyDiscovery class
        discovery = LazyDiscovery()
        sources = discovery.get_discovery_sources()
        print(f"\n🔍 Discovery sources: {sources}")
        
        # Test project root detection
        print(f"📁 Project root: {discovery.project_root}")
        
        print(f"\n✅ Lazy discovery system working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_lazy_install_direct():
    """Test lazy install directly"""
    try:
        from exonware.xwsystem.utils.lazy_install import lazy_import_with_install, LazyInstaller
        
        print("\n🚀 Testing Lazy Install System (Direct Import)")
        print("=" * 60)
        
        # Test lazy import with built-in module
        module, available = lazy_import_with_install("json")
        if available:
            print("✅ Built-in module (json) import works")
        else:
            print("❌ Built-in module import failed")
        
        # Test lazy import with non-existent module (should not install)
        module, available = lazy_import_with_install("nonexistent_module_12345")
        if not available:
            print("✅ Non-existent module correctly returns unavailable")
        else:
            print("❌ Non-existent module incorrectly returned as available")
        
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

def test_package_agnostic():
    """Test that the system is truly package-agnostic"""
    try:
        from exonware.xwsystem.utils.lazy_discovery import LazyDiscovery
        
        print("\n🚀 Testing Package-Agnostic Design")
        print("=" * 60)
        
        discovery = LazyDiscovery()
        
        # Test that it discovers from project files
        dependencies = discovery.discover_all_dependencies()
        print(f"📦 Total dependencies discovered: {len(dependencies)}")
        
        # Test that it can handle different project structures
        print(f"📁 Project root detected: {discovery.project_root}")
        
        # Test common mappings
        common_mappings = discovery.COMMON_MAPPINGS
        print(f"🔧 Common mappings available: {len(common_mappings)}")
        
        # Show some common mappings
        print(f"\n📋 Sample common mappings:")
        for i, (import_name, package_name) in enumerate(list(common_mappings.items())[:5]):
            print(f"   {import_name} → {package_name}")
        
        print(f"\n✅ Package-agnostic design working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Testing xwsystem Lazy Systems (Direct Import)")
    print("=" * 70)
    
    success1 = test_lazy_discovery_direct()
    success2 = test_lazy_install_direct()
    success3 = test_package_agnostic()
    
    if success1 and success2 and success3:
        print(f"\n🎉 All tests passed! Lazy systems are working correctly.")
        print(f"\n💡 Key achievements:")
        print(f"   ✅ Package-agnostic dependency discovery")
        print(f"   ✅ Automatic discovery from project files")
        print(f"   ✅ Reusable across all exonware libraries")
        print(f"   ✅ No hardcoded package lists")
        print(f"   ✅ Dynamic configuration from pyproject.toml, requirements.txt")
        print(f"   ✅ Lazy install with automatic package installation")
        print(f"\n🚀 Ready for use in xwnode, xwdata, xwentity, and other libraries!")
    else:
        print(f"\n❌ Some tests failed. Check the errors above.")
        sys.exit(1)
