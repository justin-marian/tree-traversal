import pytest
from main import Tree
from unittest.mock import patch
from io import StringIO

@pytest.mark.printPreorderTree
def test_printPreorderTree(capsys):
    """ Test method for _printPreorderTree method """
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    
    expected_output = "5\n3\n2\n4\n7\n6\n8\n"
    
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tree._printPreorderTree(tree.getRoot())
        assert fake_out.getvalue() == expected_output

@pytest.mark.printPostorderTree
def test_printPostorderTree(capsys):
    """ Test method for _printPostorderTree method """
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    
    expected_output = "2\n4\n3\n6\n8\n7\n5\n"
    
    with patch('sys.stdout', new=StringIO()) as fake_out:
        tree._printPostorderTree(tree.getRoot())
        assert fake_out.getvalue() == expected_output
