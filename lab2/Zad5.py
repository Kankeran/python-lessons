# Wydrukuj alfabet w formacie: AaBbCcDd….., a następnie w formacie:
# aAbBcCdD…..

bigLetters = ""
smallLetters = ""
bigFirst = ""
smallFirst = ""

for i in range(65, 91, 1):
    bigLetters += chr(i)
for i in range(97, 123, 1):
    smallLetters += chr(i)

for i in range(26):
    bigFirst += bigLetters[i] + smallLetters[i]
    smallFirst += smallLetters[i] + bigLetters[i]

print(bigFirst)
print(smallFirst)
