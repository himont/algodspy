import random


class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


def insert_bst(new_node, root):
    if root == None:
        root = new_node
    else:
        while root != None:
            if new_node.val < root.val:
                if root.left == None:
                    root.left = new_node
                    return
                else:
                    root = root.left
            else:
                if root.right == None:
                    root.right = new_node
                    return
                else:
                    root = root.right


def find_ancestor(root, data1, data2):
    max_data = max(data1, data2)
    min_data = min(data1, data2)
    lca = None
    while True:
        if root:
            if root.val > min_data and root.val < max_data:
                lca = root.val
                break
            if root.val == min_data or root.val == max_data:
                lca = root.val
                break
            if root.val > max_data:
                root = root.left
            elif root.val < min_data:
                root = root.right
        else:
            break
    return lca


if __name__ == '__main__':
    number_of_nodes = 20
    arr = random.sample(range(0,100),number_of_nodes)
    print(arr)
    root =Node(arr[0])
    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        insert_bst(new_node, root)
    data_index_arr = random.sample(range(0, number_of_nodes), 2)
    data1 = arr[data_index_arr[0]]
    data2 = arr[data_index_arr[1]]
    lca = find_ancestor(root, data1, data2)
    if lca:
        print("Lowest common ancestor of %d and %d is %d" %(data1, data2, lca))
    else:
        print("Lowest common ancestor not found for %d and %d" %(data1, data2))