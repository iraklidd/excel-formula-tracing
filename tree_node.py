import json

class TreeNode:
    def __init__(self, level, name, cell, formula, parameters=None, sublevel=None):
        self.level = level
        self.name = name
        self.cell = cell
        self.formula = formula
        self.parameters = parameters if parameters else []
        self.sublevel = sublevel if sublevel else []

    def add_child(self, node):
        """Add a child node (sublevel) to the current node."""
        self.sublevel.append(node)
    
    def to_dict(self):
        """Converts the node to a dictionary (JSON serializable)."""
        return {
            "level": self.level,
            "name": self.name,
            "cell": self.cell,
            "formula": self.formula,
            "parameters": self.parameters,
            "sublevel": [child.to_dict() for child in self.sublevel]
        }


    def print_tree(self, indent=0):
        """Print the tree structure in a simple indented format."""
        indent_str = "  " * indent
        print(f"{indent_str}{self.name}: {self.cell} -> {self.formula}")
        for child in self.sublevel:
            child.print_tree(indent + 1)