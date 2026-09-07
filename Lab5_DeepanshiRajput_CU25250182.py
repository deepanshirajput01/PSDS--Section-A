# Infix to Postfix Conversion using Stack

''' def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for char in expression:

        # If character is an operand
        if char.isalnum():
            postfix += char

        # If opening parenthesis
        elif char == '(':
            stack.append(char)

        # If closing parenthesis
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()

            if stack:
                stack.pop()

        # If character is an operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Main program
expression = "A+(B*C)"

print("Infix Expression:", expression)

result = infix_to_postfix(expression)

print("Postfix Expression:", result) '''






'''# Postfix Expression Evaluation using Stack

def evaluate_postfix(expression):
    stack = []

    for char in expression:

        # If character is a number
        if char.isdigit():
            stack.append(int(char))

        # If character is an operator
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2

            elif char == '-':
                result = operand1 - operand2

            elif char == '*':
                result = operand1 * operand2

            elif char == '/':
                result = operand1 / operand2

            elif char == '^':
                result = operand1 ** operand2

            stack.append(result)

    return stack.pop()


# Main program
postfix = "23*5+"

print("Postfix Expression:", postfix)

result = evaluate_postfix(postfix)

print("Result:", result) '''






# Binary Search Tree
# Insertion, Deletion and Traversals


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BST class
class BST:

    # INSERTION
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root


    # INORDER TRAVERSAL
    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


    # PREORDER TRAVERSAL
    def preorder(self, root):

        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


    # POSTORDER TRAVERSAL
    def postorder(self, root):

        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


    # FIND MINIMUM VALUE
    def find_min(self, root):

        current = root

        while current.left is not None:
            current = current.left

        return current


    # DELETION
    def delete(self, root, data):

        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:

            # Case 1 and Case 2
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)

            root.data = temp.data

            root.right = self.delete(root.right, temp.data)

        return root


# ---------------- MAIN PROGRAM ----------------

tree = BST()

root = None

# Insert elements
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = tree.insert(root, value)


# Traversals
print("Inorder Traversal:")
tree.inorder(root)

print("\nPreorder Traversal:")
tree.preorder(root)

print("\nPostorder Traversal:")
tree.postorder(root)


# Delete a node
print("\n\nDeleting 30...")
root = tree.delete(root, 30)


# Display tree after deletion
print("\nInorder after deletion:")
tree.inorder(root)