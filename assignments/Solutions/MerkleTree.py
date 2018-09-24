from hashlib import sha256
from copy import deepcopy

class MerkleTree():
    
    def __init__(self, transactions):
        """
        Merkle tree implementation. Initialize with the leaf nodes 
        and return a MerkleTree object, with some appropriates methods.
        
        :input transactions: iterable (as list) of strings.
        """
        
        self.leaves = [transactions]
        self.tree = self.make_merkle_tree(transactions)
    
    
    @staticmethod
    def __sha256_function__(string):
        
        if isinstance(string,str):
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
        for i in range(0,len(merkle_tree),2):

            if i < len(merkle_tree) - 1:
                first_node = merkle_tree[i]
                second_node = merkle_tree[i + 1]

            else: # odd number of nodes case
                first_node = merkle_tree[i]
                second_node = merkle_tree[i]

            new_node = {'key': self.__sha256_function__(first_node['key']+second_node['key']),
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
        
        first_tree = tree
        second_tree = self.make_merkle_tree(transactions)
        
        ## Join the trees
        new_merkle_tree = {
            'key': self.__sha256_function__(first_tree['key']+second_tree['key']),
            'left': first_tree,
            'right': second_tree
        }
        
        if change_original_tree:
            self.tree = new_merkle_tree
            self.leaves.append(transactions)
        return new_merkle_tree
        
        
# The following functions do not contribute for the assignment.

    def __merkle_root_search__(self, merkle_tree, root):
        """
        return the partial merkle tree where the root is `root` input. 
        """
        tree = deepcopy(merkle_tree)
        
        # Uhul! We found.
        if tree['key'] == root:
            return tree
        
        # In this case, tree['right'] is also None. Bad, We didn't find.
        elif tree['left'] == None:
            return None
        
        # We still hope to find.
        else:            
            # Search the left child tree
            left_search = merkle_root_search(tree['left']) 
            if left_search != None:
                return left_search
            
            #if the root isn't in the left, search in the right child tree
            else:
                return merkle_root_search(tree['right'])
            
    def __get_leaves__(self, tree, leaves=[]):
        """
        Recursive function to get the leaves of a merkle tree.
        """
        # It is a leave!!!!! Uhul
        if tree['left'] == None:
            leaves.append(tree['key'])
        else:
            leaves = self.__get_leaves__(tree['left'], leaves)
            leaves = self.__get_leaves__(tree['right'], leaves)
        
        return leaves 
                
    def verify_leaf(self, leave, merkle_root):
        ## Not finished.
        
        leave_hash = self.__sha256_function__(leave)
        specific_tree = self.__merkle_root_search__(tree, merkle_root)
        leaves = self.__get_leaves__(specific_tree, [])
        ### ???
        