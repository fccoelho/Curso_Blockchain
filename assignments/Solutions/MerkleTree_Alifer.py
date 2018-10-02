"""
Solution to homework 2 contributed by Alifer Sales
"""

from hashlib import sha256


class MerkleTree():

    def __init__(self, transactions):
        """
        Merkle tree implementation. Initialize with the leaf nodes 
        and return a MerkleTree object, with some appropriates methods.
        
        :input transactions: iterable (as list) of strings.
        """

        self.leaves = [transactions]
        self.tree = self.make_merkle_tree(transactions)
        
    def root(self, tree=None):
        """
        Returns the merkle root of the `tree` input. If `tree` is None, will be
        considered the self.tree.
        """
        
        if tree == None:
            tree = self.tree
        
        return tree['key']
        
    @staticmethod
    def __sha256_function__(string):

        if isinstance(string, str):
            string = string.encode()

        output = sha256()
        output.update(string)
        return output.hexdigest()

    def __merkle_tree_builder__(self, merkle_tree):
        """
        Auxiliar recursive function to create go up one level on
        the merkle tree.
        
        :input merkle_tree: list of merkle trees
        """

        new_merkle_tree = []
        for i in range(0, len(merkle_tree), 2):

            if i < len(merkle_tree) - 1:
                first_node = merkle_tree[i]
                second_node = merkle_tree[i + 1]

            else:  # odd number of nodes case
                first_node = merkle_tree[i]
                second_node = merkle_tree[i]

            new_node = {'key': self.__sha256_function__(first_node['key'] + second_node['key']),
                        'left': first_node,
                        'right': second_node
                        }
            new_merkle_tree.append(new_node)

        return new_merkle_tree

    def make_merkle_tree(self, transactions):
        """
        Create a merkle tree based on the transactions strings input.
        
        :input transactions: iterable (as list) of strings.
        :output: Returns the merkle tree for the inputed transactions.
        """

        ## Hash the transactions string
        current_row = list(map(self.__sha256_function__, transactions))

        ## As each element of current_row is a leaf, create the leaf structure
        merkle_tree = []
        for i in current_row:
            merkle_tree.append(
                {'key': i, 'left': None, 'right': None}
            )

        ## When there are only the leafs on the `merkle_tree`, we are on the
        ## bottom level of the tree. Each iteration will go up one tree level,
        ## decreasing the number of nodes untill the top level of tree, when
        ## `merkle_tree` will have only a dict, with the complete merkle tree.
        while len(merkle_tree) > 1:
            merkle_tree = self.__merkle_tree_builder__(merkle_tree)

        return merkle_tree[0]

    def join_trees(self, transactions, merkle_tree=None):
        """
        Return a join of a existent merkle tree with a new merkle tree, based on the
        transactions input.
        
        :input transactions: iterable (as list) of strings | Transactions of the new merkle tree.
        :input merkle_tree: dict | The already existent merkle tree that will be joined. 
                            If None, will be used the self.tree and it will be changed with output.
        :output: Returns a joined merkle tree with the `merkle_tree` and the transactions merkle tree. 
        """
        change_original_tree = False
        if merkle_tree == None:
            merkle_tree = self.tree
            change_original_tree = True

        first_tree = merkle_tree
        second_tree = self.make_merkle_tree(transactions)

        ## Join the trees
        new_merkle_tree = {
            'key': self.__sha256_function__(first_tree['key'] + second_tree['key']),
            'left': first_tree,
            'right': second_tree
        }

        if change_original_tree:
            self.tree = new_merkle_tree
            self.leaves.append(transactions)
        return new_merkle_tree

    def partial_merkle_tree(self, root, tree=None):
        """
        return the partial merkle tree where the root is the first ocurrence 
        (top-bottom, left-right) of the `root` input in the `tree`.
        
        :input root: string | The hash of the node that will be the root of the partial tree.
        :input tree: dict | The merkle tree. If None, will be used the self.tree.
        
        :return: dict | The partial merkle tree.
        """
        if tree == None:
            tree = self.tree

        # Uhul! We found.
        if tree['key'] == root:
            return tree

        # In this case, tree['right'] is also None. Bad, We didn't find.
        elif tree['left'] == None:
            return None

        # We still hope to find.
        else:
            # Search the left child tree
            left_search = self.partial_merkle_tree(root, tree['left'])
            if left_search != None:
                return left_search

            # if the root isn't in the left, search in the right child tree
            else:
                return self.partial_merkle_tree(root, tree['right'])

    def get_leaves(self, tree, leaves=None):
        """
        Returns the leaves of a merkle tree.
        
        Recursive function to get the leaves of a merkle tree.
        """

        if leaves == None:
            leaves = []

        # It is a leaf!!!!! Uhul
        if tree['left'] == None:
            leaves.append(tree['key'])
        else:
            leaves = self.get_leaves(tree['left'], leaves)
            leaves = self.get_leaves(tree['right'], leaves)

        return leaves

    def verify_leaf(self, leaf, merkle_root, tree=None, leaf_hash=False):
        """
        Verify if `leaf` is a leaf of the partial merkle tree `tree`, where the 
        root is the first occurrence (top-bottom, left-right) of the `merkle_root`.
        
        :input leaf: string | the leaf string that will be verified.
        :input merkle_root: hash string | hash of the node that will be considered root.
        :input tree: dict | the merkle tree. If None, will be used the self.tree.
        :input leaf_hash: bool | True if the `leaf` is a hash. False, otherwise.
        
        :return: True if the leaf is in tree. False, otherwise.
        """
        if tree == None:
            tree = self.tree

        if not leaf_hash:
            leaf = self.__sha256_function__(leaf)
        specific_tree = self.partial_merkle_tree(merkle_root, tree)
        leaves = self.get_leaves(specific_tree)
        if leaf in leaves:
            return True
        return False


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
        # self.assertListEqual(test_leaves_even, mt.leaves)
        self.assertListEqual([test_leaves_even], mt.leaves)
    def test_get_leaves(self):
        mt = MerkleTree(test_leaves_even)
        # self.assertListEqual(test_leaves_even, mt.get_leaves(mt))
        self.assertListEqual([mt.__sha256_function__(i) for i in test_leaves_even],
                             mt.get_leaves(mt.tree))
    def test_odd_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertIsInstance(mt, MerkleTree)
    def test_order(self):
        mt = MerkleTree(test_leaves_even)
        random.shuffle(test_leaves_even)
        mt2 = MerkleTree(test_leaves_even)

        # self.assertListEqual(test_leaves_even, mt2.leaves)
        self.assertListEqual([test_leaves_even], mt2.leaves)
        
    def test_verify_leaves(self):
        mt = MerkleTree(test_leaves_even)
        
        # r = mt.verify_leaf('casa', mt.root)
        r = mt.verify_leaf('casa', mt.root())
    
    def test_join_trees(self):
        mt = MerkleTree(test_leaves_even)
        #  mt2 = MerkleTree(test_leaves_odd)
        #  mtj = mt.join_trees(mt2)
        mtj = mt.join_trees(test_leaves_odd)


if __name__ == "__main__":
    unittest.main()