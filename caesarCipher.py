
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# cipher key
key = 3

# the alphabet after applying the cipher key
cipher = []

#make sure we stay in bounds
count = 0

# append the alphabet letters to the cipher list starting with the cipher key index
while count < len(alphabet):
    cipher.append(alphabet[key])
    key = (key + 1) % len(alphabet)
    count += 1

# make key value pairs out of the original and cipher alphabet
dictionary = dict(zip(alphabet, cipher))

for k, v in dictionary.items():
    print(k, v)



    