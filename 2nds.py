customer={
    "name":"John",
    "age":30,
    "is_verified":True
}
print(customer["name"])
print(customer.get("birthdate","1 jan 2023"))#if there is no birthdate it replaces it with the given value

phn=input("Enter Phone Number: ")
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",

}
output=""
for ch in phn:
    output += (digit_mapping.get(ch,"!"))+" "

print(output)

message=input(">")
words=message.split(' ')
emojis={
    ":)":"[smiley]",
    ":(":"[frownie]"

}
output=""
for word in words:
    output+=emojis.get(word,word)

print(output)