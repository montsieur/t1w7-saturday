from text_processing import count_words, unique_words, count_characters, count_unique_characters, reverse_string

# Test string
test_string = "Hello World hello"

# Using word count module

print("Word Count is: ", count_words(test_string))
print("Unique words:", unique_words(test_string))

# Using char_count module
print("Character Count:", count_characters(test_string))
print("Unique Character Count:", count_unique_characters(test_string))

# Using reverse module
print("Reversed string:", reverse_string(test_string))