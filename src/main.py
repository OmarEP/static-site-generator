from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import *

def main():
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
    )
    new_nodes = split_nodes_link([node])
    



if __name__ == "__main__":
    main()