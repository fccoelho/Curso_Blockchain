"""
Solution to HW2 by Carla Parreiras
"""

import hashlib
import json
from collections import OrderedDict


class MerkleTree:

    #  Iniciando a classe
    def __init__(self, listoftransaction=None):
        self.leaves = listoftransaction
        self.past_transaction = OrderedDict()

    # Criando a Merkle Tree
    def make_merkle_tree(self):
        listoftransaction = self.leaves
        past_transaction = self.past_transaction
        temp_transaction = []
        for index in range(0, len(listoftransaction), 2):  # vamos passar pela lista toda
            current = listoftransaction[index]  # começando pelo elemento da esquerda, o primeiro
            if index + 1 != len(listoftransaction):
                current_right = listoftransaction[index + 1]  # vai passando para os termos que estão a sua direita
            else:  # chegando no último item da lista, criamos uma string cheia
                current_right = ''
                current_hash = hashlib.sha256(current)  # e aplica a função hash 256 para o valor
            if current_right != '':  # se for diferente da empty string, então aplica a hash function 256
                current_right_hash = hashlib.sha256(current_right)
            past_transaction[listoftransaction[index]] = current_hash.hexdigest()  # adiciona ao dicionário
            if current_right != '':
                past_transaction[listoftransaction[index + 1]] = current_right_hash.hexdigest()
            if current_right != '':  # criando uma lista de transações
                temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())
            else:  # mas se o primeiro já é uma empty string, então o valor é o p´roprio current
                temp_transaction.append(current_hash.hexdigest())
        if len(listoftransaction) != 1:  # Atualizando as variáveis e rodando a função novamente
            self.listoftransaction = temp_transaction
            self.past_transaction = past_transaction
            self.make_merkle_tree()

    def Last_transacion(self):  # retorna a última transação
        return self.past_transaction

    def Get_Root(self):  # retorna a raiz
        last_key = list(self.past_transaction.keys())[-1]
        return self.past_transaction[last_key]

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

    def test_odd_leaves(self):
        mt = MerkleTree(test_leaves_even)
        self.assertIsInstance(mt, MerkleTree)
    def test_order(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(['bola', 'casa', 'caixa', 'peixe'])
        self.assertListEqual(mt.Get_Root(), mt2.Get_Root())
    def test_verify_leaves(self):
        mt = MerkleTree(test_leaves_even)
        r = mt.verify_leaf('casa', mt.root)
    def test_join_trees(self):
        mt = MerkleTree(test_leaves_even)
        mt2 = MerkleTree(test_leaves_odd)
        mtj = mt.join_trees()


if __name__ == "__main__":
    unittest.main()
