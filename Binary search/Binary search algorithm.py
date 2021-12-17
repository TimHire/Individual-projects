import pandas as pd

random_numbers = pd.read_csv("Random number list.csv")
print(random_numbers.head())
random_number_list = sorted(random_numbers["Numbers"].tolist())
random_numbers_final = list(set(random_number_list))         # Gets rid of duplicates as a set cannot have duplicates in
print(random_number_list)


test_list = list(range(0, 102, 2))             # test case looking for numbers in the array


def binary_search(input_list, element):
    print(f"Looking for element {element} in the list "
          f"- {len(input_list)} elements between {min(input_list)} and {max(input_list)}")
    while len(input_list) > 1:
        middle = round(len(input_list) / 2)
        middle_element = input_list[middle]
        if element < middle_element:
            input_list = input_list[:middle]
        elif element > middle_element:
            input_list = input_list[middle:]
        elif element == middle_element:
            return "The element is in the list"
        else:
            print("There has been an error ")
        print(len(input_list), input_list)
    return "The element is not in the list"


print(binary_search(random_numbers_final, 4566))
print()
print(binary_search(test_list, 15))
