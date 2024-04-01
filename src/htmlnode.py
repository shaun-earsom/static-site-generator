class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        s_prop = ""
        for prop in self.props:
            s_prop += " " + prop + "=" + "\"" + self.props[prop] + "\""
        return s_prop
    
    def __repr__(self) -> str:
        return f'HTMLNode("{self.tag}", "{self.value}", "{self.children}", "{self.props}")'
    
class LeafNode(HTMLNode):
    def __init__(self, *, tag=None, value, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props, children=None)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return self.value
        if self.tag == "p":
            return "<" + self.tag + ">" + self.value + "</" + self.tag + ">"
        if self.tag == "a" and self.props != None:
            return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"