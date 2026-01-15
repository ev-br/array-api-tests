#!/usr/bin/env python3
"""
Simple test to validate π parsing in complex values
"""
import sys
import math

# Add the array_api_tests module to the path
sys.path.insert(0, '/home/runner/work/array-api-tests/array-api-tests')

from array_api_tests.test_special_cases import parse_complex_value, parse_value

def test_parse_value_pi():
    """Test that parse_value correctly handles π expressions"""
    # Test simple π
    result = parse_value('π')
    assert abs(result - math.pi) < 1e-10, f"Expected {math.pi}, got {result}"
    print("✓ parse_value('π') works")
    
    # Test π/2
    result = parse_value('π/2')
    expected = math.pi / 2
    assert abs(result - expected) < 1e-10, f"Expected {expected}, got {result}"
    print(f"✓ parse_value('π/2') = {result}")
    
    # Test 3π/4
    result = parse_value('3π/4')
    expected = 3 * math.pi / 4
    assert abs(result - expected) < 1e-10, f"Expected {expected}, got {result}"
    print(f"✓ parse_value('3π/4') = {result}")

def test_parse_complex_value():
    """Test that parse_complex_value correctly handles complex values with π"""
    # Test +0 + 0j
    result = parse_complex_value('+0 + 0j')
    expected = complex(0.0, 0.0)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ parse_complex_value('+0 + 0j') = {result}")
    
    # Test the critical case: +0 + πj/2
    result = parse_complex_value('+0 + πj/2')
    expected = complex(0.0, math.pi / 2)
    assert abs(result.real - expected.real) < 1e-10, f"Real part mismatch"
    assert abs(result.imag - expected.imag) < 1e-10, f"Imaginary part mismatch: expected {expected.imag}, got {result.imag}"
    print(f"✓ parse_complex_value('+0 + πj/2') = {result}")
    print(f"  Real part: {result.real}")
    print(f"  Imaginary part: {result.imag} (expected {math.pi/2})")
    
    # Test NaN + NaN j
    result = parse_complex_value('NaN + NaN j')
    assert math.isnan(result.real), f"Expected NaN for real part, got {result.real}"
    assert math.isnan(result.imag), f"Expected NaN for imaginary part, got {result.imag}"
    print(f"✓ parse_complex_value('NaN + NaN j') = {result}")
    
    # Test -0 - πj/4
    result = parse_complex_value('-0 - πj/4')
    expected = complex(-0.0, -math.pi / 4)
    assert abs(result.imag - expected.imag) < 1e-10, f"Imaginary part mismatch"
    print(f"✓ parse_complex_value('-0 - πj/4') = {result}")

if __name__ == '__main__':
    print("Testing π parsing in complex values...")
    print()
    
    try:
        test_parse_value_pi()
        print()
        test_parse_complex_value()
        print()
        print("✅ All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
