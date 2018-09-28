u"""
Test code to validate Merkle tree implementation
You can copy and paste this code to the bottom of you source file with the Merkle Tree implementation
"""

import unittest
import random

test_leaves_even = ['casa', 'bola', 'peixe', 'caixa']
test_leaves_odd = ['um', 'dois', 'três']

class TestMerkleTree(unittest.TestCase):
    def test_tree_creation(self):
        mt = MerkleTree(test_leaves_even)
        self.assertIsInstance(mt, MerkleTree)
    def test_return_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertListEqual(test_leaves_even, mt.leaves)
    def test_get_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertListEqual(test_leaves_even, mt.get_leaves(mt))
    def test_odd_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertIsInstance(mt, MerkleTree)
    def test_order(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(['bola', 'casa', 'caixa', 'peixe'])
        self.assertListEqual(mt.root, mt2.root)
    def test_verify_leaves(self):
        mt = MerkleTree(test_leaves_even)
        r = mt.verify_leaf('casa', mt.root)
    def test_join_trees(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(test_leaves_odd)
        mtj = mt.join_trees()


if __name__ == "__main__":
    unittest.main()
