def string_book_text(string_text):
    words = string_text.split()
    return len(words)

def char_count(book_text):
    dict_text = {}
    chars = book_text.lower()
    for char in chars:
        if char.isalpha():
            dict_text[char] = dict_text.get(char, 0) + 1
    return dict_text

def sort_report(char_count):
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    report = ""
    for char, count in sorted_chars:
        if char.isalpha():
            report += f"{char}: {count}\n"
    return report