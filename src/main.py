from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import *
from markdown_blocks import(
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)

def main():
    md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
    print(markdown_to_html_node(md).to_html())

if __name__ == "__main__":
    main()

'<div><ol><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ol><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>'