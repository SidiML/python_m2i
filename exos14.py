def compter_lettre_a(sentences):
    count = 0
    for letter in sentences:
        if letter == 'A' or letter == 'a':
            count += 1
    print('résultat:', count)

compter_lettre_a ("aaasaidia")