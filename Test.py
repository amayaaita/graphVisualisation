import unittest
from TreeNode import Tree 
from Sol import LCA

class TestLCAMethod(unittest.TestCase):
    
    def test_3_Node_Tree(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(5), dummy.search(1)).key,dummy.search(3).key)

    def test_Root_As_Result(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(1), dummy.search(6)).key,dummy.search(3).key)

    def test_Both_Desendants_Same(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(8), dummy.search(8)).key,dummy.search(8).key)

    def test_Both_Desendants_Same_As_Root(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(3), dummy.search(3)).key,dummy.search(3).key)

    def test_Mid_Tree_Result_Right(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(4), dummy.search(6)).key,dummy.search(5).key)

    def test_Mid_Tree_Result_Left(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(2), dummy.search(0)).key,dummy.search(1).key)

    def test_Mid_Tree_Result_Left_Deeper(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(7), dummy.search(8)).key,dummy.search(8).key)

    def test_Mid_Tree_Result_Left_split_level(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(7), dummy.search(4)).key,dummy.search(5).key)



if __name__ == '__main__':
    caller =LCA()
    dummy = Tree()
    dummy.add_node(3)
    dummy.add_node(1)
    dummy.add_node(5)
    dummy.add_node(6)
    dummy.add_node(2)
    dummy.add_node(0)
    dummy.add_node(8)
    dummy.add_node(4)
    dummy.add_node(7)
    dummy.traverse()
   
    unittest.main()