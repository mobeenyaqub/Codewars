def duplicate_count(text):
    text = text.lower()
    return len([i for i in sorted(set(text)) if text.count(i) > 1])
