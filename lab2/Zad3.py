# Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy
# użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

string = input("Podaj tresc do zaszyfrowania: ")
wzrost = int(input("Podaj o ile maja sie przesunac litery: "))
newString = ""
for char in string:
    if not char.isalpha():
        newString += char
        continue
    duze = 91 > ord(char) > 64
    char = chr(ord(char) + wzrost)
    while duze and ord(char) > 90 or ord(char) > 122:
        char = chr(ord(char)-26)
    newString += char

print(newString)
