def is_pangram(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    sentence = "".join(sorted(set(list(sentence.lower()))))

    if alpha in sentence:
        return(True)
    else:
        return(False)
