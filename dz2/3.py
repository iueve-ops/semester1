def palindrome(string):
    return string[::-1] == string

mirror_values = {
    'A': 'A',
    'H': 'H',
    'I': 'I',
    'M': 'M',
    'O': 'O',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    '1': '1',
    '8': '8',
    'E': '3',
    '3': 'E',
    'J': 'L',
    'L': 'J',
    'S': '2',
    '2': 'S',
    'Z': '5',
    '5': 'Z'
}

def mirror(string):
    temp_string = ''
    for char in string:
        if char in mirror_values:
            temp_string = mirror_values[char] + temp_string  
        else:
            return False
    return temp_string == string

def mirrored_palindrome(string):
    return palindrome(string) and mirror(string)

inputed_string = input()

is_palindrome = palindrome(inputed_string)
is_mirrored = mirror(inputed_string)
is_mirrored_palindrome = mirrored_palindrome(inputed_string)

if is_mirrored_palindrome:
    print(inputed_string + ' is a mirrored palindrome')
elif is_palindrome:
    print(inputed_string + ' is a palindrome')
elif is_mirrored:
    print(inputed_string + ' is a mirrored string')
else:
    print(inputed_string + ' is not a palindrome')