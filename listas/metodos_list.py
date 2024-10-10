languages = []

# append
languages.append("Python")
languages.append("Python")
languages.append("Java")
languages.append("JavaScript")
languages.append("Java")
print(languages)

# copy
languages_copy = languages.copy()
print(languages)
print(languages_copy)

# clear
languages_copy.clear()
print(languages)
print(languages_copy)

# count
print(languages.count("Python"))
print(languages.count("Java"))

# extend
languages.extend(["C", "C#", "C++"])
print(languages)

# index
print(languages.index("Java"))
print(languages.index("Python"))

# pop
languages.pop()
print(languages)
languages.pop(1)
print(languages)

# remove
languages.remove("Java")
print(languages)

# reverse
languages.reverse()
print(languages)

# sort
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.sort(key=lambda x: len(x))
print(languages)
languages.sort(key=lambda x: len(x), reverse=True)
print(languages)

# len
print(len(languages))

# sorted
print(sorted(languages))
