# test_zigzagperp.py
"""
Tests for ZigZagPerp module.
"""

import unittest
from zigzagperp import ZigZagPerp

class TestZigZagPerp(unittest.TestCase):
    """Test cases for ZigZagPerp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZigZagPerp()
        self.assertIsInstance(instance, ZigZagPerp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZigZagPerp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
