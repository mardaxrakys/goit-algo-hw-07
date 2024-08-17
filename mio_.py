#----------------------------------------------- Task_1
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання
bst = BinarySearchTree()
for value in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(value)

print("Максимальне значення:", find_max(bst.root))

#------------------------------------------------------------------------ Task_2
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
print("Мінімальне значення:", find_min(bst.root))
#------------------------------------------------------------------------- Task_3
def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
print("Сума всіх значень:", sum_of_values(bst.root))
#------------------------------------------------------------------------- Task_4
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, reply=None):
        if reply is None:
            # Видалити всі відповіді
            self.text = "Цей коментар було видалено."
            self.is_deleted = True
        else:
            # Видалити конкретну відповідь
            if reply in self.replies:
                self.replies.remove(reply)
                reply.text = "Цей коментар було видалено."
                reply.is_deleted = True

    def display(self, indent=0):
        if self.is_deleted:
            print(" " * indent + f"{self.author}: {self.text}")
        else:
            print(" " * indent + f"{self.author}: {self.text}")
            for reply in self.replies:
                reply.display(indent + 4)

# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()  # Видалення відповіді

root_comment.display()
