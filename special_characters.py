# ASCII characters found at https://donsnotes.com/tech/charsets/ascii.html

shift_characters = {

    'a': 'A', 'b': 'B', 'c': 'C',
    'd': 'D', 'e': 'E', 'f': 'F',
    'g': 'G', 'h': 'H', 'i': 'I',
    'j': 'J', 'k': 'K', 'l': 'L',
    'm': 'M', 'n': 'N', 'o': 'O',
    'p': 'P', 'q': 'Q', 'r': 'R',
    's': 'S', 't': 'T', 'u': 'U',
    'v': 'V', 'w': 'W', 'x': 'X',
    'y': 'Y', 'z': 'Z', '[': '{',
    '?': '?', 'caps_lock': 'caps_lock',
    '0': ')', '1': '!', '2': '@',
    '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*',
    '9': '(', '-': '_', ']': '}'

}

ctrl_characters = {'a': '\\x01', 'b': '\\x02', 'c': '\\x03',
                   'd': '\\x04', 'e': '\\x05', 'f': '\\x06',
                   'g': '\\x07', 'h': '\\x08', 'i': '\\x09',
                   'j': '\\x0a', 'k': '\\x0b', 'l': '\\x0c',
                   'm': '\\x0d', 'n': '\\x0e', 'o': '\\x0f',
                   'p': '\\x10', 'q': '\\x11', 'r': '\\x12',
                   's': '\\x13', 't': '\\x14', 'u': '\\x15',
                   'v': '\\x16', 'w': '\\x17', 'x': '\\x18',
                   'y': '\\x19', 'z': '\\x1a', '[': '\\x1b',
                   ']': '\\x1d', '^': '\\x1e', '_': '\\x1f',
                   '?': '\\x7f', 'caps_lock': 'caps_lock',
                   '0': '<48>', '1': '<49>', '2': '<50>',
                   '3': '<51>', '4': '<52>', '5': '<53>',
                   '6': '<54>', '7': '<55>', '8': '<56>',
                   '9': '<57>', '-': '<189>', '+': '<187>',
                   'A': '\\x01', 'B': '\\x02', 'C': '\\x03',
                   'D': '\\x04', 'E': '\\x05', 'F': '\\x06',
                   'G': '\\x07', 'H': '\\x08', 'I': '\\x09',
                   'J': '\\x0a', 'K': '\\x0b', 'L': '\\x0c',
                   'M': '\\x0d', 'N': '\\x0e', 'O': '\\x0f',
                   'P': '\\x10', 'Q': '\\x11', 'R': '\\x12',
                   'S': '\\x13', 'T': '\\x14', 'U': '\\x15',
                   'V': '\\x16', 'W': '\\x17', 'X': '\\x18',
                   'Y': '\\x19', 'Z': '\\x1a'
                   }

alt_and_ctrl_characters = {

    'a': '<65>', 'b': '<66>', 'c': '<67>',
    'd': '<68>', 'e': '<69>', 'f': '<70>',
    'g': '<71>', 'h': '<72>', 'i': '<73>',
    'j': '<74>', 'k': '<75>', 'l': '<76>',
    'm': '<77>', 'n': '<78>', 'o': '<79>',
    'p': '<80>', 'q': '<81>', 'r': '<82>',
    's': '<83>', 't': '<84>', 'u': '<85>',
    'v': '<86>', 'w': '<87>', 'x': '<88>',
    'y': '<89>', 'z': '<90>', '[': '<91>',
    '\\': '<92>', ']': '<93>', '^': '<94>',
    '_': '<95>', '?': '<63>', 'caps_lock': 'caps_lock',
    'A': '<65>', 'B': '<66>', 'C': '<67>',
    'D': '<68>', 'E': '<69>', 'F': '<70>',
    'G': '<71>', 'H': '<72>', 'I': '<73>',
    'J': '<74>', 'K': '<75>', 'L': '<76>',
    'M': '<77>', 'N': '<78>', 'O': '<79>',
    'P': '<80>', 'Q': '<81>', 'R': '<82>',
    'S': '<83>', 'T': '<84>', 'U': '<85>',
    'V': '<86>', 'W': '<87>', 'X': '<88>',
    'Y': '<89>', 'Z': '<90>', '+': '=',
    '0': '<48>', '1': '<49>', '2': '<50>',
    '3': '<51>', '4': '<52>', '5': '<53>',
    '6': '<54>', '7': '<55>', '8': '<56>',
    '9': '<57>'

}

shift_and_ctrl_characters = {

    '0': '<48>', '1': '<49>', '2': '\\x00',
    '3': '<51>', '4': '<52>', '5': '<53>',
    '6': '\\x1e', '7': '<55>', '8': '<56>',
    '9': '<57>', '-': '\\x1f', '+': '<187>'

}