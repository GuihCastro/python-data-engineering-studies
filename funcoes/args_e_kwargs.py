def show_poem(date, *text, **info):
    poem = "\n".join(text)
    meta_data = "\n".join([f"{key.title()}: {value}" for key, value in info.items()])
    message = f"{date}\n\n{poem}\n\n{meta_data}"
    print(message)

show_poem(
    "22 de agosto de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex if better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Erros should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "The should be one -- and preferably only one -- obvious way to do it.",
    "Although that may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    author="Tim Peters",
    year=1999
)