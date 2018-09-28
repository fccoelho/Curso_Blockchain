"""
Solution to HW 2 by Breno Gomes
"""

import hashlib


def join_and_hash(str1, str2):
    return hashlib.sha256(str1.encode("utf-8") + str2.encode("utf-8")).hexdigest()


class MerkleTree:
    def __init__(self, content):
        # SORTING SO SAME SUBSETS GENERATE SAME MERKEL TREE
        self.content = sorted(content)
        self.branches = [self.content]

    def __str__(self):
        return str(list(self.branches))

    def root(self):
        return self.branches[len(self.branches) - 1][0]

    def make_merkel_tree(self):
        while len(self.branches[len(self.branches) - 1]) != 1:
            new_branch = []
            current_branch = self.branches[len(self.branches) - 1]
            for i in range(0, len(current_branch), 2):
                if i == len(current_branch) - 1:
                    new_branch.append(join_and_hash(current_branch[i], current_branch[i]))
                    break
                new_branch.append(join_and_hash(current_branch[i], current_branch[i + 1]))
            self.branches.append(new_branch)

    def join_trees(self, iterator):
        new_tree = MerkelTree(iterator)
        new_tree.make_merkel_tree()
        self.branches.append([join_and_hash(self.root(), new_tree.root())])
        for i in range(0, len(new_tree.branches)):
            self.branches[len(self.branches) - (i + 2)] += new_tree.branches[len(new_tree.branches) - (i + 1)]


# Added by Flavio for grading

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
        self.assertListEqual(test_leaves_even, mt.content)

    def test_get_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertListEqual(test_leaves_even, mt.content)

    def test_odd_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertIsInstance(mt, MerkleTree)

    def test_order(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(['bola', 'caixa', 'casa', 'peixe'])
        self.assertEqual(mt.root(), mt2.root())

    def test_verify_leaves(self):
        mt = MerkleTree(test_leaves_even)
        r = mt.verify_leaf('casa', mt.root)

    def test_join_trees(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(test_leaves_odd)
        mtj = mt.join_trees()


# Example of creating and joining a tree
if __name__ == "__main__":
    mt = MerkleTree(["b", "c", "a", "d", "e"])
    mt.make_merkel_tree()
    print(mt)

    mt.join_trees(["f", "g", "h"])
    print(mt)

    unittest.main()
