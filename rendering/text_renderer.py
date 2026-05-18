from rendering.parser import parse_html
from networking.loader import load_url
def render_url(url):
    html_content = load_url(url)
    parsed_content = parse_html(html_content)
    
    result = ""
    
    for child in parsed_content.children:
        if child.node_type == "text":
            result += child.text + "\n"
        else:
            result += render_child(child)
    return result

def render_child(node):
    result = ""

    for child in node.children:
        if child.node_type == "text":
            result += child.text + "\n"
        else:
            result += render_child(child)

    return result