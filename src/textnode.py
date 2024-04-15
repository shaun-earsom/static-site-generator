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
    new_node_list = []
    
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_node_list.append(old_nodes)
    this_node = node.text
    node_list = this_node.split(delimiter)

    for i in range(len(node_list)):
        if i == 0:
            new_node_list.append(TextNode(node_list[i], text_type_text))
        elif i % 2 != 0:
            new_node_list.append(TextNode(node_list[i], text_type))
        else:
            new_node_list.append(TextNode(node_list[i], text_type_text))
    
    return new_node_list
        