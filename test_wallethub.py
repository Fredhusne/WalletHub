# test_wallethub.py
"""
Tests for WalletHub module.
"""

import unittest
from wallethub import WalletHub

class TestWalletHub(unittest.TestCase):
    """Test cases for WalletHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletHub()
        self.assertIsInstance(instance, WalletHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
