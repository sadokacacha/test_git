# Function to count vowels and non-vowels in a string
def count_vowels_and_non_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels (uppercase and lowercase)
    vowel_count = 0  # Initialize vowel count to 0
    non_vowel_count = 0  # Initialize non-vowel count to 0

    # Loop through each character in the string

def count_vowels(input_string):
    vowels = "aeiouAEIOUd"  
    count = 0  
    for char in input_string:
        if char in vowels:  
            count += 1
    return count
user_input = input("Enter a string: ")  
vowel_count = count_vowels(user_input)  
print(f"The number of vowels in the string is: {vowel_count}")