from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    html_node = HTMLNode(None, None, None, {
            "href": "https://www.google.com", 
            "target": "_blank",
    })
    print(html_node.props_to_html())


if __name__ == "__main__":
    main()