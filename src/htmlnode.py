class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        prop_vals = []
        for k, v in self.props.items():
            val = f'{k}="{v}"'
            prop_vals.append(val)
        return " " + " ".join(prop_vals)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children) if self.children else 0}, props={self.props})"
    
