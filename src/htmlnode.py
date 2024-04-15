class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __eq__(self, __value: object) -> bool:
        return self.tag == __value.tag and self.value == __value.value and self.children == __value.children and self.props == __value.props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, __value: object) -> bool:
        return self.tag == __value.tag and self.value == __value.value and self.props == __value.props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be provided")
        if self.children is None:
            raise ValueError("Children must be provided")
        child_arg = ""
        for child in self.children:
            child_arg += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_arg}</{self.tag}>"
    
    def __eq__(self, __value: object) -> bool:
        return self.tag == __value.tag and self.children == __value.children and self.props == __value.props
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"