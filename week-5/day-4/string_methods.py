# a = "aeroplane is a good mode of transport"
# b = a.split()  # splits a string into words in a list
# print(b)

# skip a word and print the sentence
# a = "aeroplane is a good mode of transport"
# b = a.split()
# print(b)
# b = b[::2]
# print(" ".join(i for i in b))

# display only unique words
# a = "aeroplane ok is a good mode of transport good bye ok done"
# # b = a.split()
# # c = []
# # for i in b:
# #     if i not in c:
# #         c.append(i)
# # print(c)
# # orelse
# print(list(set(a.split())))

# print each word in reverse and print sentence
a = "aeroplane ok is a good mode of transport good bye ok done"
b = a.split()
print(b)
c = []
for i in b:
    c.append(i[::-1])
print(" ".join(i for i in c))

# orelse
