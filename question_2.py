def StringChallenge(sen):
    encoded_str = ""
    count = 1
    for i in range(1, len(sen)):
        if sen[i] == sen[i-1]:
            count += 1
        else:
            encoded_str += str(count) + sen[i-1]
            count = 1
    encoded_str += str(count) + sen[-1]

    challenge_token = "jf6qdyivlb2"
    final_output = encoded_str[::-1] + ": " + challenge_token[::-1]

    return final_output
