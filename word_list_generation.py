import random
word_list = []

with open('bip39_english.txt') as f:
    word_list = f.read().splitlines()

for x in range(48):
    selection = random.randint(0, len(word_list)-1)
    word_list.pop(selection)

twofa_list = word_list[::2][:1000]

with open('2fa_english.txt', "w") as f:
    for x in twofa_list:
        f.write(x + "\n")

print(twofa_list[random.randrange(0,999)]+ " " +twofa_list[random.randrange(0,999)])
