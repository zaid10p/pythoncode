from data_structure.stack import Stack
from data_structure.binary_tree import BinaryTree, Node
from functools import wraps


b = BinaryTree(Node(6))

for v in [5, 3, 9, 7, 8, 7.5, 12, 11]:
    b.add(Node(v))

b.inorder()
b.delete(9)
print(" ------")
b.inorder()


st = Stack([2, 3])
st.pop()
st.push(5)
# print(st.getList())

# Decorators example :


def get_user_role() -> int:
    return 1


def access_control(access_level: int):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*arg, **kwargs):
            if get_user_role() <= access_level:
                return func(*arg, **kwargs)
            else:
                raise PermissionError(
                    'You do not have the proper access level.')
        return inner_wrapper
    return outer_wrapper


@access_control(1)
def deleteFile(filename):
    print(f" {filename} is deleted")


deleteFile("asd")
