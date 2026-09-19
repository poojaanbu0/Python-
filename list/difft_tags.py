def make_words(tag,words):
    return f"<{tag}>{words}</{tag}>"

tag = ['i','uo']
words = ['hello','hi']
target_re = []
for target in range(len(words)):
    res = make_words(tag[target],words[target])
    target_re.append(res)
print(target_re)

pairs = [("list", "dict"),("set","tuple")]
tra = [make_words(t,w) for t,w in pairs]
print(tra)