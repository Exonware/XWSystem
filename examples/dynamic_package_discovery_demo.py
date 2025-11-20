"""
Dynamic Package Discovery Demo for xwsystem

This demo shows how the dynamic package discovery system works.
It automatically discovers package mappings from project configuration files
and makes the lazy install system reusable across all exonware libraries.

Author: Eng. Muhammad AlShehri
Company: eXonware.com
Email: connect@exonware.com
Version: 0.0.1
Generated: 2025-01-27
"""

import sys
import os
import json
from pathlib import Path

# Add src to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def demo_package_discovery():
    """Demo 1: Package Discovery from Project Files"""
    print("=" * 60)
    print("🚀 DEMO 1: Dynamic Package Discovery")
    print("=" * 60)
    
    from xwlazy.lazy import (
        LazyDiscovery, 
        discover_dependencies,
        export_dependency_mappings
    )
    
    # Create discovery instance
    discovery = LazyDiscovery()
    
    print(f"📁 Project root: {discovery.project_root}")
    print(f"📁 Current working directory: {os.getcwd()}")
    
    # Discover dependencies
    dependencies = discover_dependencies()
    print(f"\n📦 Discovered {len(dependencies)} dependencies:")
    
    # Show first 10 dependencies
    for i, (import_name, package_name) in enumerate(list(dependencies.items())[:10]):
        print(f"   {import_name} → {package_name}")
    
    if len(dependencies) > 10:
        print(f"   ... and {len(dependencies) - 10} more dependencies")
    
    # Show discovery sources
    sources = discovery.get_discovery_sources()
    print(f"\n🔍 Discovery sources: {sources}")
    
    # Show dependencies by category
    print(f"\n📊 Dependencies discovered from:")
    for source in sources:
        count = sum(1 for info in discovery.discovered_dependencies.values() if info.source == source)
        print(f"   {source}: {count} dependencies")

def demo_lazy_config_integration():
    """Demo 2: Integration with Lazy Install"""
    print("\n" + "=" * 60)
    print("🚀 DEMO 2: Lazy Install Integration")
    print("=" * 60)
    
    from xwlazy.lazy import (
        LazyInstaller,
        DependencyMapper,
        get_lazy_install_stats,
        discover_dependencies
    )
    
    # Get discovered dependencies
    dependencies = discover_dependencies()
    print(f"📦 Dependencies discovered: {len(dependencies)}")
    
    # Test dependency name resolution
    test_imports = ['msgpack', 'requests', 'yaml', 'numpy', 'pandas']
    print(f"\n🔍 Dependency name resolution:")
    mapper = DependencyMapper()
    for import_name in test_imports:
        package_name = mapper.get_package_name(import_name)
        print(f"   {import_name} → {package_name}")
    
    # Show lazy install stats
    stats = get_lazy_install_stats()
    print(f"\n📊 Lazy install stats:")
    print(f"   Enabled: {stats['enabled']}")
    print(f"   Total installed: {stats['total_installed']}")
    print(f"   Total failed: {stats['total_failed']}")

def demo_cross_library_usage():
    """Demo 3: Cross-Library Usage"""
    print("\n" + "=" * 60)
    print("🚀 DEMO 3: Cross-Library Usage")
    print("=" * 60)
    
    print("💡 This system can be used across all exonware libraries:")
    print()
    
    libraries = ['xwsystem', 'xwnode', 'xwdata', 'xwentity', 'xwschema', 'xwaction']
    
    for library in libraries:
        print(f"📚 {library}:")
        print(f"   • Automatically discovers packages from {library}/pyproject.toml")
        print(f"   • Automatically discovers packages from {library}/requirements.txt")
        print(f"   • Uses same lazy_import_with_install() function")
        print(f"   • Same configuration system")
        print()
    
    print("🎯 Benefits:")
    print("   • No hardcoded package lists")
    print("   • Always up-to-date with project dependencies")
    print("   • Consistent behavior across all libraries")
    print("   • Easy to maintain and extend")

def demo_custom_configuration():
    """Demo 4: Custom Configuration"""
    print("\n" + "=" * 60)
    print("🚀 DEMO 4: Custom Configuration")
    print("=" * 60)
    
    from exonware.xwsystem.config.package_discovery import PackageDiscovery
    
    # Create a custom discovery instance
    discovery = PackageDiscovery()
    
    print("🔧 Adding custom package mappings:")
    
    # Add some custom mappings
    custom_mappings = [
        ('my_custom_lib', 'my-custom-package', 'custom'),
        ('internal_tool', 'internal-tool-package', 'internal'),
        ('special_format', 'special-format-package', 'serialization')
    ]
    
    for import_name, package_name, category in custom_mappings:
        discovery.add_custom_mapping(import_name, package_name, category)
        print(f"   ✅ {import_name} → {package_name} (category: {category})")
    
    # Show updated packages
    packages = discovery.discover_all_packages()
    print(f"\n📦 Total packages after custom additions: {len(packages)}")
    
    # Show custom packages
    custom_packages = [name for name in packages.keys() if name.startswith(('my_', 'internal_', 'special_'))]
    print(f"🔧 Custom packages: {custom_packages}")

def demo_export_functionality():
    """Demo 5: Export Functionality"""
    print("\n" + "=" * 60)
    print("🚀 DEMO 5: Export Functionality")
    print("=" * 60)
    
    from xwlazy.lazy import export_dependency_mappings
    
    # Export to a temporary file
    export_file = "temp_dependency_mappings.json"
    
    try:
        export_dependency_mappings(export_file)
        print(f"✅ Exported dependency mappings to {export_file}")
        
        # Read and display the exported data
        with open(export_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\n📊 Exported data:")
        print(f"   Total dependencies: {data['total_count']}")
        print(f"   Sources: {data['sources']}")
        
        # Show sample dependencies
        sample_dependencies = list(data['dependencies'].items())[:5]
        print(f"\n📦 Sample dependencies:")
        for import_name, package_name in sample_dependencies:
            print(f"   {import_name} → {package_name}")
        
    except Exception as e:
        print(f"❌ Export failed: {e}")
    finally:
        # Clean up
        if os.path.exists(export_file):
            os.remove(export_file)
            print(f"🧹 Cleaned up {export_file}")

def demo_real_world_scenarios():
    """Demo 6: Real-World Scenarios"""
    print("\n" + "=" * 60)
    print("🚀 DEMO 6: Real-World Scenarios")
    print("=" * 60)
    
    print("🌍 Real-world usage scenarios:")
    print()
    
    print("📚 Scenario 1: xwnode library")
    print("   • xwnode/pyproject.toml contains: requests, aiohttp, pydantic")
    print("   • System automatically discovers these packages")
    print("   • lazy_import_with_install('requests') works automatically")
    print("   • No manual configuration needed")
    print()
    
    print("📚 Scenario 2: xwdata library")
    print("   • xwdata/requirements.txt contains: pandas, numpy, h5py")
    print("   • System automatically discovers these packages")
    print("   • lazy_import_with_install('pandas') works automatically")
    print("   • Same code, different project")
    print()
    
    print("📚 Scenario 3: Custom project")
    print("   • Custom project with package-mappings.json")
    print("   • Defines custom import → package mappings")
    print("   • System uses custom mappings + common mappings")
    print("   • Fully customizable behavior")
    print()
    
    print("🎯 Key advantages:")
    print("   • Zero configuration for standard projects")
    print("   • Automatic discovery from existing files")
    print("   • Consistent API across all libraries")
    print("   • Easy to extend and customize")
    print("   • Always synchronized with project dependencies")

def main():
    """Run all demos"""
    print("🚀 xwsystem Dynamic Package Discovery Demo")
    print("=" * 60)
    print("This demo shows how the dynamic package discovery system")
    print("automatically discovers package mappings from project files")
    print("and makes the lazy install system reusable across all")
    print("exonware libraries (xwnode, xwdata, xwentity, etc.).")
    print()
    
    try:
        demo_package_discovery()
        demo_lazy_config_integration()
        demo_cross_library_usage()
        demo_custom_configuration()
        demo_export_functionality()
        demo_real_world_scenarios()
        
        print("\n" + "=" * 60)
        print("✅ Demo completed successfully!")
        print("=" * 60)
        print()
        print("🎯 Key Benefits:")
        print("   • Automatic package discovery from project files")
        print("   • No hardcoded package lists")
        print("   • Reusable across all exonware libraries")
        print("   • Always up-to-date with project dependencies")
        print("   • Easy to customize and extend")
        print("   • Consistent behavior across projects")
        print()
        print("💡 Next Steps:")
        print("   1. Test with different project structures")
        print("   2. Add support for more configuration formats")
        print("   3. Integrate with CI/CD pipelines")
        print("   4. Add package version management")
        print("   5. Create library-specific configurations")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
