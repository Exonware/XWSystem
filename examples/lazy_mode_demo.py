"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1.360
Generation Date: September 18, 2025

Lazy Mode Demo - Demonstrates xwsystem lazy loading capabilities.
"""

import time
import sys
import os

# Add the src directory to the path for local development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    import xwsystem
    from xwsystem import (
        enable_lazy_mode,
        disable_lazy_mode,
        is_lazy_mode_enabled,
        get_lazy_mode_stats,
        configure_lazy_mode,
        preload_modules,
        optimize_lazy_mode,
        register_lazy_module,
        get_lazy_module
    )
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're running this from the xwsystem directory")
    sys.exit(1)


def demo_basic_lazy_mode():
    """Demonstrate basic lazy mode functionality."""
    print("🚀 Lazy Mode Demo - Basic Functionality")
    print("=" * 50)
    
    # Check initial state
    print(f"Lazy mode enabled: {is_lazy_mode_enabled()}")
    
    # Enable lazy mode
    print("\n📋 Enabling lazy mode...")
    enable_lazy_mode(strategy="on_demand", enable_monitoring=True)
    print(f"Lazy mode enabled: {is_lazy_mode_enabled()}")
    
    # Get initial stats
    stats = get_lazy_mode_stats()
    print(f"\n📊 Initial stats: {stats}")
    
    # Configure lazy mode
    print("\n⚙️ Configuring lazy mode...")
    configure_lazy_mode(
        preload_threshold=3,
        clear_cache_on_disable=True,
        enable_monitoring=True
    )
    
    # Register some modules for lazy loading
    print("\n📝 Registering modules for lazy loading...")
    register_lazy_module("json", "json")
    register_lazy_module("yaml", "yaml")
    register_lazy_module("pickle", "pickle")
    
    # Get updated stats
    stats = get_lazy_mode_stats()
    print(f"📊 Stats after registration: {stats}")
    
    # Preload some modules
    print("\n🔄 Preloading modules...")
    preload_modules(["json", "yaml"])
    
    # Run optimization
    print("\n🎯 Running optimization...")
    optimize_lazy_mode()
    
    # Get final stats
    final_stats = get_lazy_mode_stats()
    print(f"\n📊 Final stats: {final_stats}")
    
    # Disable lazy mode
    print("\n🛑 Disabling lazy mode...")
    disable_lazy_mode()
    print(f"Lazy mode enabled: {is_lazy_mode_enabled()}")


def demo_performance_comparison():
    """Demonstrate performance benefits of lazy mode."""
    print("\n\n⚡ Performance Comparison Demo")
    print("=" * 50)
    
    # Test without lazy mode
    print("📋 Testing without lazy mode...")
    start_time = time.time()
    
    # Simulate loading multiple modules
    modules_to_test = ["json", "yaml", "pickle", "csv", "xml"]
    for module_name in modules_to_test:
        try:
            register_lazy_module(module_name, module_name)
            loader = get_lazy_module(module_name)
            # Force loading
            _ = loader._get_module()
        except Exception as e:
            print(f"  ⚠️ Could not load {module_name}: {e}")
    
    without_lazy_time = time.time() - start_time
    print(f"⏱️ Time without lazy mode: {without_lazy_time:.4f} seconds")
    
    # Test with lazy mode
    print("\n📋 Testing with lazy mode...")
    enable_lazy_mode(strategy="on_demand")
    
    start_time = time.time()
    
    # Register modules but don't load them yet
    for module_name in modules_to_test:
        try:
            register_lazy_module(f"lazy_{module_name}", module_name)
        except Exception as e:
            print(f"  ⚠️ Could not register {module_name}: {e}")
    
    with_lazy_time = time.time() - start_time
    print(f"⏱️ Time with lazy mode (registration only): {with_lazy_time:.4f} seconds")
    
    # Now load them on demand
    start_time = time.time()
    for module_name in modules_to_test:
        try:
            loader = get_lazy_module(f"lazy_{module_name}")
            # This will trigger lazy loading
            _ = loader._get_module()
        except Exception as e:
            print(f"  ⚠️ Could not load lazy_{module_name}: {e}")
    
    lazy_load_time = time.time() - start_time
    print(f"⏱️ Time for lazy loading: {lazy_load_time:.4f} seconds")
    
    # Get performance stats
    stats = get_lazy_mode_stats()
    print(f"\n📊 Performance stats: {stats}")
    
    disable_lazy_mode()


def demo_advanced_features():
    """Demonstrate advanced lazy mode features."""
    print("\n\n🔧 Advanced Features Demo")
    print("=" * 50)
    
    # Enable lazy mode with advanced configuration
    enable_lazy_mode(
        strategy="cached",
        enable_monitoring=True,
        preload_threshold=2,
        clear_cache_on_disable=False
    )
    
    # Register multiple modules
    modules = {
        "json": "json",
        "yaml": "yaml", 
        "pickle": "pickle",
        "csv": "csv",
        "xml": "xml.etree.ElementTree"
    }
    
    print("📝 Registering multiple modules...")
    for name, path in modules.items():
        register_lazy_module(name, path)
    
    # Simulate usage patterns
    print("\n🔄 Simulating usage patterns...")
    for i in range(3):
        # Access json multiple times
        loader = get_lazy_module("json")
        _ = loader._get_module()
        
        # Access yaml multiple times  
        loader = get_lazy_module("yaml")
        _ = loader._get_module()
    
    # Run optimization to preload frequently used modules
    print("\n🎯 Running optimization...")
    optimize_lazy_mode()
    
    # Get detailed stats
    stats = get_lazy_mode_stats()
    print(f"\n📊 Detailed stats:")
    print(f"  - Total registered: {stats.get('total_registered', 0)}")
    print(f"  - Loaded count: {stats.get('loaded_count', 0)}")
    print(f"  - Unloaded count: {stats.get('unloaded_count', 0)}")
    print(f"  - Access counts: {stats.get('access_counts', {})}")
    
    disable_lazy_mode()


def main():
    """Main demo function."""
    print("🌟 xwsystem Lazy Mode Demonstration")
    print("=" * 60)
    
    try:
        # Run all demos
        demo_basic_lazy_mode()
        demo_performance_comparison()
        demo_advanced_features()
        
        print("\n\n✅ All demos completed successfully!")
        print("\n💡 Key Benefits of Lazy Mode:")
        print("  • Reduced startup time")
        print("  • Lower memory usage")
        print("  • On-demand module loading")
        print("  • Performance monitoring")
        print("  • Smart caching and optimization")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
