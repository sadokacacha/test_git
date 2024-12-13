<<<<<<< HEAD
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
=======
# Function to count vowels and non-vowels in a string
def count_vowels_and_non_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels (uppercase and lowercase)
    vowel_count = 0  # Initialize vowel count to 0
    non_vowel_count = 0  # Initialize non-vowel count to 0
>>>>>>> 526a463256edb0eb4610aba0e982b72692c98b6b

    # Loop through each character in the string
    for char in input_string:
<<<<<<< HEAD
        if char in vowels:
            count += 1
=======
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1
        elif char.isalpha():  # Check if the character is a non-vowel letter
            non_vowel_count += 1
>>>>>>> 526a463256edb0eb4610aba0e982b72692c98b6b

    return vowel_count, non_vowel_count

<<<<<<< HEAD

user_input = input("Enter a string: ")
user_input = input("Enter a string: ")
user_input = input("Enter a string: ")
user_input = input("Enter a string: ")
user_input = input("Enter a string: ")
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
=======
# Example usage
user_input = input("Enter a string: ")  # Get input from the user
vowel_count, non_vowel_count = count_vowels_and_non_vowels(user_input)  # Count vowels and non-vowels in the input string
>>>>>>> 526a463256edb0eb4610aba0e982b72692c98b6b
print(f"The number of vowels in the string is: {vowel_count}")
print(f"The number of non-vowel letters in the string is: {non_vowel_count}")
