"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1.360
Generation Date: September 18, 2025

Lazy Tools Demo - Demonstrates lazy_import and lazy_install functionality.
"""

import sys
import os

# Add src to path for local testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def demo_lazy_import():
    """Demonstrate lazy import functionality."""
    print("🚀 Lazy Import Demo")
    print("=" * 40)
    
    try:
        from xwlazy.lazy import (
            enable_lazy_imports,
            disable_lazy_imports,
            is_lazy_import_enabled,
            lazy_import,
            register_lazy_module,
            get_lazy_import_stats
        )
        
        print("✅ Lazy import utilities imported successfully")
        
        # Enable lazy imports
        enable_lazy_imports()
        print(f"📋 Lazy imports enabled: {is_lazy_import_enabled()}")
        
        # Register some modules for lazy loading
        print("\n📝 Registering modules for lazy import...")
        register_lazy_module("json", "json")
        register_lazy_module("yaml", "yaml")
        register_lazy_module("pickle", "pickle")
        
        # Import modules lazily
        print("\n🔄 Importing modules lazily...")
        json_module = lazy_import("json")
        yaml_module = lazy_import("yaml")
        pickle_module = lazy_import("pickle")
        
        # Use the modules
        print("\n💼 Using lazily imported modules...")
        data = {"test": "data", "number": 42}
        json_result = json_module.dumps(data)
        print(f"  JSON result: {json_result}")
        
        pickle_result = pickle_module.dumps(data)
        print(f"  Pickle result: {len(pickle_result)} bytes")
        
        # Get stats
        stats = get_lazy_import_stats()
        print(f"\n📊 Lazy import stats: {stats}")
        
        # Disable lazy imports
        disable_lazy_imports()
        print(f"\n🛑 Lazy imports disabled: {is_lazy_import_enabled()}")
        
    except Exception as e:
        print(f"❌ Lazy import demo failed: {e}")
        import traceback
        traceback.print_exc()


def demo_lazy_install():
    """Demonstrate lazy install functionality."""
    print("\n\n🛠️ Lazy Install Demo")
    print("=" * 40)
    
    try:
        from xwlazy.lazy import (
            enable_lazy_install,
            disable_lazy_install,
            is_lazy_install_enabled,
            install_and_import,
            install_missing_package,
            get_lazy_install_stats
        )
        
        print("✅ Lazy install utilities imported successfully")
        
        # Enable lazy install
        enable_lazy_install()
        print(f"📋 Lazy install enabled: {is_lazy_install_enabled()}")
        
        # Try to install and import a common package
        print("\n🔄 Testing lazy install with 'requests'...")
        try:
            requests_module = install_and_import("requests")
            print("✅ Requests module available")
            
            # Test using the module
            print("🌐 Testing HTTP request...")
            response = requests_module.get("https://httpbin.org/json", timeout=5)
            if response.status_code == 200:
                print(f"  ✅ HTTP request successful: {response.status_code}")
            else:
                print(f"  ⚠️ HTTP request returned: {response.status_code}")
                
        except Exception as e:
            print(f"  ⚠️ Could not test requests: {e}")
        
        # Try to install a package that might not exist
        print("\n🧪 Testing with non-existent package...")
        try:
            fake_module = install_and_import("definitely_not_a_real_package_name_12345")
            print("❌ This should not succeed")
        except ImportError as e:
            print(f"  ✅ Correctly failed to install fake package: {e}")
        
        # Get stats
        stats = get_lazy_install_stats()
        print(f"\n📊 Lazy install stats: {stats}")
        
        # Disable lazy install
        disable_lazy_install()
        print(f"\n🛑 Lazy install disabled: {is_lazy_install_enabled()}")
        
    except Exception as e:
        print(f"❌ Lazy install demo failed: {e}")
        import traceback
        traceback.print_exc()


def demo_package_mapping():
    """Demonstrate package name mapping."""
    print("\n\n🗺️ Package Mapping Demo")
    print("=" * 40)
    
    try:
        from xwlazy.lazy import DependencyMapper as PackageMapper
        
        print("✅ Package mapper imported successfully")
        
        # Test common mappings
        test_cases = [
            ("cv2", "opencv-python"),
            ("PIL", "Pillow"),
            ("yaml", "PyYAML"),
            ("sklearn", "scikit-learn"),
            ("bs4", "beautifulsoup4"),
            ("jwt", "PyJWT"),
            ("requests", "requests")  # Same name
        ]
        
        print("\n📋 Testing package name mappings...")
        for import_name, expected_package in test_cases:
            actual_package = PackageMapper.get_package_name(import_name)
            status = "✅" if actual_package == expected_package else "❌"
            print(f"  {status} {import_name} -> {actual_package} (expected: {expected_package})")
        
    except Exception as e:
        print(f"❌ Package mapping demo failed: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Main demo function."""
    print("🌟 xwsystem Lazy Tools Demonstration")
    print("=" * 60)
    
    print("\n💡 What we're demonstrating:")
    print("  • lazy_import: Performance optimization through deferred imports")
    print("  • lazy_install: Automatic package installation on import failure")
    print("  • package_mapper: Smart mapping of import names to pip packages")
    
    try:
        # Run all demos
        demo_lazy_import()
        demo_lazy_install()
        demo_package_mapping()
        
        print("\n\n✅ All demos completed!")
        print("\n🎯 Key Benefits:")
        print("  • lazy_import: Faster startup, lower memory usage")
        print("  • lazy_install: Automatic dependency resolution")
        print("  • Smart package mapping: Handles import/pip name differences")
        print("\n📦 Usage:")
        print("  pip install exonware-xwsystem[lazy]  # For auto-install features")
        
    except Exception as e:
        print(f"\n❌ Demo suite failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
