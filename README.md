# regularExpressions
This note gives some tips to manipulate regular expression and extract some useful informations about someone, something when it is available.
Before giving some tips, I define regular expression and explain its role in text mining.

A regular expression is a search pattern used for matching one or more characters within a string. It can match specific characters, wildcards, and ranges of characters.
It helps you extract informations about something, someone etc.

To do something in text mining using regularExpressions, you must define a pattern, that is a specific structure of string from a dictonnary.
For avoiding a shit explanatory about dictionary , I do some example to do this staff on data.

- .       - Any Character Except New Line
- \d      - Digit (0-9)
- \D      - Not a Digit (0-9)
- \w      - Word Character (a-z, A-Z, 0-9, _)
- \W      - Not a Word Character
- \s      - Whitespace (space, tab, newline)
- \S      - Not Whitespace (space, tab, newline)

- \b      - Word Boundary
- \B      - Not a Word Boundary
- ^       - Beginning of a String
- $       - End of a String

- []      - Matches Characters in brackets
- [^ ]    - Matches Characters NOT in brackets
- |       - Either Or
- ( )     - Group

Quantifiers:
- \*       - 0 or More
- \+       - 1 or More
- \?       - 0 or One
- {3}     - Exact Number
- {3,4}   - Range of Numbers (Minimum, Maximum)
