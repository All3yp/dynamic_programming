# https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python

def reverse_string_mode_c(input_string):
    reversed_string = ""
    for i in input_string:
        reversed_string = i + reversed_string
    return reversed_string

def reversed_string_mode_easy(str):
    return str[::-1]

input_str = "Hello, World!"
result_01 = reverse_string_mode_c(input_str)
result_02 = reversed_string_mode_easy(input_str)
print(result_01)  # Saída: "!dlroW ,olleH"
print(result_02)