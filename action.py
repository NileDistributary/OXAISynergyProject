from ai import register_action

@register_action
def extract_list(text: str) -> list[str]:
    return text.split(",")