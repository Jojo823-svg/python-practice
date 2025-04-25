# Defining function
def string_reverse(y):
    string_rev = " "  # Begin with an empty space to store the reversed word
    for char in y:
        string_rev = char + string_rev  # each letter of y will be added before the string_rev
    return string_rev


print(string_reverse("Joy"))  # The output becomes yoj