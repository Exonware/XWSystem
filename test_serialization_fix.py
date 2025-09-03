#!/usr/bin/env python3
"""
Quick test to verify serialization fixes are working.

Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: August 31, 2025
"""

def test_json_serializer_instantiation():
    """Test that JsonSerializer can be instantiated without abstract method errors."""
    try:
        from exonware.xsystem.serialization.json import JsonSerializer
        
        # Should not raise abstract method error
        serializer = JsonSerializer()
        print("✅ JsonSerializer instantiation successful")
        
        # Test basic methods
        test_data = {"test": "data"}
        serialized = serializer.dumps_text(test_data)
        deserialized = serializer.loads_text(serialized)
        
        assert deserialized == test_data
        print("✅ JsonSerializer basic functionality working")
        
        # Test binary methods
        binary_data = serializer.dumps_binary(test_data)
        recovered = serializer.loads_bytes(binary_data)
        
        assert recovered == test_data
        print("✅ JsonSerializer binary methods working")
        
        return True
        
    except Exception as e:
        print(f"❌ JsonSerializer test failed: {e}")
        return False


def test_yaml_serializer_instantiation():
    """Test that YamlSerializer can be instantiated without abstract method errors."""
    try:
        from exonware.xsystem.serialization.yaml import YamlSerializer
        
        # Should not raise abstract method error
        serializer = YamlSerializer()
        print("✅ YamlSerializer instantiation successful")
        
        # Test basic methods
        test_data = {"test": "data"}
        serialized = serializer.dumps_text(test_data)
        deserialized = serializer.loads_text(serialized)
        
        assert deserialized == test_data
        print("✅ YamlSerializer basic functionality working")
        
        # Test binary methods
        binary_data = serializer.dumps_binary(test_data)
        recovered = serializer.loads_bytes(binary_data)
        
        assert recovered == test_data
        print("✅ YamlSerializer binary methods working")
        
        return True
        
    except Exception as e:
        print(f"❌ YamlSerializer test failed: {e}")
        return False


def test_xserialization_instantiation():
    """Test that xSerialization can be instantiated and used."""
    try:
        from exonware.xsystem.serialization import xSerialization
        
        # Should not raise abstract method error
        serializer = xSerialization()
        print("✅ xSerialization instantiation successful")
        
        # Test basic functionality
        test_data = {"test": "data"}
        serialized = serializer.dumps(test_data)
        deserialized = serializer.loads(serialized)
        
        assert deserialized == test_data
        print("✅ xSerialization basic functionality working")
        
        return True
        
    except Exception as e:
        print(f"❌ xSerialization test failed: {e}")
        return False


def main():
    """Run all serialization tests."""
    print("🧪 Testing Serialization Fixes")
    print("=" * 40)
    
    tests = [
        test_json_serializer_instantiation,
        test_yaml_serializer_instantiation,
        test_xserialization_instantiation,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All serialization tests passed!")
        return 0
    else:
        print("💥 Some serialization tests failed!")
        return 1


if __name__ == "__main__":
    exit(main())
