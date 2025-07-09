def num_words(str):
    return len(str.split())
def num_chars(str):
    str_clean = "".join(c for c in str if c.isalpha())
    str_clean_lwr = str_clean.lower()
    count = {}
    for c in str_clean_lwr:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count
def sort_on(items):
    return items["num"]
def dic_sort(dic):
    list = []
    for k, v in dic.items():
        list.append({"char": k, "num": v})
    list.sort(reverse=True, key=sort_on)
    return list
