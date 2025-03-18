from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None or value == "":
            raise ValueError("all leaf nodes must have a value")
        super().__init__(tag=tag, value=value, props=props)
        self.children = None

    @property
    def children(self):
        return None
        
    @children.setter
    def children(self, value):
        if value is not None:  # Allow None to handle initialization
            raise AttributeError("LeafNode cannot have children.")

    def to_html(self):
        if not self.tag:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"