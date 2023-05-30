def StringChallenge(sen):
    sen = ''.join(c for c in sen if c.isalnum() or c.isspace())

    words = sen.split()

    longest_word = max(words, key=len)
    token = "jf6qdyivlb2"
    result = longest_word[::-1] + ":" + token[::-1]

    return result
