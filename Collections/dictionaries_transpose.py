def transpose_dictionary(vocabulary):

    for key, value in vocabulary.items():

      vocabulary.pop(key)
      vocabulary[value]  = key

    return vocabulary

def main():
    vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
    print(vocabulary)
    transpose_dictionary(vocabulary)
    print(vocabulary)
main()