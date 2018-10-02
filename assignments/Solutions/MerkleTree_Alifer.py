"""
Solution to homework 2 contributed by Alifer Sales
"""

def string_to_sha256(string):

    if isinstance(string,str):
        string = string.encode()

    output = sha256()
    output.update(string)
    return output.hexdigest()

class MerkleTree():
    
    def __init__(self, leaves):
        """
        Merkle tree implementation. Initialize with the leaves nodes 
        and return a MerkleTree object, with some appropriates methods.
        
        :input leaves: iterable (as list) of strings.
        """
        
        self.leaves = leaves
        self.is_ready = False
        self.levels = []
        self.root = None
        
        
    def make_merkle_tree(self):
        """Create the merkle tree based on the self.leaves"""
        
        if self.is_ready:
            print("The merkle tree already is done.")
            return None
        
        leaves_hash = [string_to_sha256(leaf) for leaf in self.leaves]
        
        levels = []
        current_level = leaves_hash
        while len(current_level) > 1:
            
            current_level
            levels = [current_level] + levels
            
            aux_current = current_level
            current_level = []
            while aux_current != []:
                if len(aux_current) >= 2:
                    node_children = aux_current[0:2]
                    node_children.sort()
                    node_hash = string_to_sha256(''.join(node_children))
                    current_level.append(node_hash)
                    aux_current = aux_current[2:]
                else:
                    current_level.append(aux_current[0])
                    aux_current = []
                    
        self.root = current_level[0]
        self.levels = [current_level] + levels
        self.is_ready = True
        
    def verify_leaf(self, leaf, root):
        """
        Verify if `leaf` is a leaf of merkle tree, which `root` is its root.
        
        :input leaf: string | the leaf string that will be verified.
        :return: True if the leaf is in tree. False, otherwise.
        """
        if self.is_ready:
            if root == self.root and leaf in self.leaves:
                    return True
        return False
    
    def delete_leaf(self, leaf):
        """If `leaf` is in the merkle tree, then it is deleted."""
        
        if not self.is_ready:
            print("The merkle tree was not builded. Please, run self.make_merkle_tree()")
            return None
        
        if not self.verify_leaf(leaf, self.root):
            print("The leaf is not in the tree.")
            return None
        
        self.leaves.remove(leaf)
        self.is_ready = False
        self.make_merkle_tree()


#  Added by Flavio  for testing
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
        random.shuffle(test_leaves_even)
        mt2 = MerkleTree(test_leaves_even)

        self.assertListEqual(test_leaves_even, mt2.leaves)
    def test_verify_leaves(self):
        mt = MerkleTree(test_leaves_even)
        r = mt.verify_leaf('casa', mt.root)

if __name__ == "__main__":
    unittest.main()
