class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text # The text content of the node
        self.text_type = text_type # The Type of text "bold", "Italic", etc.
        self.url = url # The URL of the link or image

    def __eq__(self, __value: object) -> bool:
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url
    
    def __repr__(self) -> str:
         return f'TextNode("{self.text}", "{self.text_type}", {self.url})'