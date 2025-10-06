def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    if node is None or not isinstance(node, dict):
        return []

    node_type = node.get("type")

    if node_type == "item":
        # Only return the name if it exists
        name = node.get("name")
        return [name] if name else []

    elif node_type == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    # Unknown node type
    return []
