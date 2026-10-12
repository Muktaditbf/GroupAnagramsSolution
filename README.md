# 🔤 Group Anagrams

A Python solution to the classic **Group Anagrams** problem (LeetCode #49): put words made of the same letters into the same group.

## Example

```
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## How it works

1. Sort each word's letters to get its "signature": `"eat"`, `"tea"` and `"ate"` all become `"aet"`.
2. Use the signature as a dictionary key, and add the word to that key's list.
3. The dictionary's values are the groups.

```python
key = "".join(sorted(word))
anagrams.setdefault(key, []).append(word)
```

- **Time:** O(n · k log k), for n words of up to k letters
- **Space:** O(n · k)

## Run it

```bash
python anagram-grouper-algorithm.py
```
