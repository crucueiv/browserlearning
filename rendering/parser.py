from rendering.dom import Node

def parse_html(html):
    inside_tag = False
    tag_buffer = ""
    text_buffer = ""

    root = Node("element", tag="document")
    stack = [root]

    for c in html:

        if c == "<":
            inside_tag = True

            # flush texto antes de tag
            if text_buffer.strip():
                stack[-1].add_child(Node("text", text=text_buffer.strip()))
                text_buffer = ""

            tag_buffer = ""
            continue

        if c == ">":
            inside_tag = False

            tag = tag_buffer.strip()

            # cierre de tag
            if tag.startswith("/"):
                stack.pop()

            else:
                new_node = Node("element", tag=tag)
                stack[-1].add_child(new_node)
                stack.append(new_node)

            tag_buffer = ""
            continue

        if inside_tag:
            tag_buffer += c
        else:
            text_buffer += c

    return root