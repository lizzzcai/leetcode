

```python
# 572. Subtree of Another Tree
def traverse_tree(node):
    '''
    You use it as a delimiter between the nodes in the string representation.
    The reason why is because take a test case of [12], [1]. So we have our s node with val=12 and no children, and t node with val=2 and no children. If we turn them to string without the #, we get the following s=12 None None and t='2 None None'. This will cause a false positive for us. If we add a # to the beginning of every node with a value, we get s=#12 None None and t=#2 None None. Now t is no longer a substring of s and doesn't create a false positive anymore.
    '''
    if node:
        return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
    else:
        return "_"

```