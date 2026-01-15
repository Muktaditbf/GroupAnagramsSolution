# 1. The Input (A list of words to sort)
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 2. The Storage (Dictionary)
anagrams = {}

# 3. The Loop
for word in words:
    # 4. Find the "DNA" (Sort the letters)
    # sorted("eat") becomes ['a', 'e', 't']
    # "".join(...) turns it back into "aet"
    key = "".join(sorted(word))
    
    # 5. Group them
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word] # Create a new list for this key

# 6. Print just the groups
print(list(anagrams.values()))