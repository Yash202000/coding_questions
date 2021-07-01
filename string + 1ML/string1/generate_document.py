characters = input()
document = input()

def gen_document(document,characters):
    for i in characters:
        documentfreq = document.count(i)
        characterfreq = characters.count(i)
        if documentfreq > characterfreq:
            return "false"

    return 'true'

print(gen_document(document,characters))

