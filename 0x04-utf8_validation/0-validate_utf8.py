#!/usr/bin/python3
'''implementing a utf-validation.'''


def validUTF8(data):
    '''Initialize a variable to keep track of
       the number of expected following bytes.
    '''

    expected_following_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if expected_following_bytes > 0 and (byte >> 6) == 0b10:
            expected_following_bytes -= 1
        # Check if the current byte is a single-byte character (0xxxxxxx)
        elif (byte >> 7) == 0:
            expected_following_bytes = 0
        # Check if the current byte is the start of a multi-byte character
        elif (byte >> 5) == 0b110:
            expected_following_bytes = 1
        elif (byte >> 4) == 0b1110:
            expected_following_bytes = 2
        elif (byte >> 3) == 0b11110:
            expected_following_bytes = 3
        else:
            # If none of the conditions match, it's an invalid byte
            return False

    return expected_following_bytes == 0
