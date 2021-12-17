import string

with open("Personal statement 5.txt") as ps:                #with loop closes the document at the end of the loop
    full_text = ps.readlines()
    #print(full_text)

total_character = 0
for line in full_text:
    if line != "\n":                        #Don't print the extra line as already adding an extra line as a result of the for loop
        total_character += len(line)
        print(line)
    else:
        total_character += 1                #As removing extra line need to add another character as I think they might include a new line as a new character

print("\n\nTotal characters:     {}".format(total_character))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
lower_total, capital_total, numbers_total, space_total, punc_total = 0, 0, 0, 0, 0

for line in full_text:
    if line.find("\n") != -1:
        line.replace("\n", " ")         #May want to remove the space at a later point
    for char in line:
        if char in string.ascii_lowercase:
            lower_total += 1
        elif char == " ":
            space_total += 1
        elif char in string.ascii_uppercase:
            capital_total += 1
        elif char in string.digits:
            numbers_total += 1
        else:
            punc_total += 1         #Assuming all other characters must be punctuation

print("Lower case letters:   {} or {}%".format(lower_total, round((lower_total * 100) / total_character)))
print("Upper case letters:   {}  or {}%".format(capital_total, round((capital_total * 100) / total_character)))
print("Numbers:              {}   or {}%".format(numbers_total, round((numbers_total * 100) / total_character)))
print("Punctuation:          {}   or {}%".format(punc_total, round((punc_total * 100) / total_character)))
print("Spaces:               {}  or {}%".format(space_total, round((space_total * 100) / total_character)))