from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic" 
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text # The text content of the node
        self.text_type = text_type # The Type of text "bold", "Italic", etc.
        self.url = url # The URL of the link or image

    def __eq__(self, __value: object) -> bool:
        print(__value)
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url
    
    def __repr__(self) -> str:
         return f'TextNode("{self.text}", "{self.text_type}", {self.url})'
    
def text_node_to_html_node(text_node):  
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception(f"Not supported text type in text_node_to_html_node: {text_node.text_type}.")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] 
    node_list = old_nodes.split(delimiter)
    if old_nodes != text_type_text:
        pass
    if text_type == text_type_text:
        pass
    if text_type == text_type_bold:
        pass
    if text_type == text_type_italic:
        pass
    if text_type == text_type_code:
        pass

    raise Exception(f"Not supported text type in split_nodes_delimiter: {text_type}.")
