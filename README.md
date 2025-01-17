# **Regex: Sequence of Characters to Define a Search Pattern**

## **Overview**
Regex, short for **Regular Expressions**, is a sequence of characters designed to define search patterns. It is a powerful tool widely used for string matching, text processing, and data validation.

## **Definition**
A Regular Expression (Regex) is a pattern composed of text characters and metacharacters. These patterns are used to perform tasks like searching, replacing, or validating strings in text data.

## **Purpose**
Regex simplifies complex text manipulation tasks by providing a structured way to define search patterns. It is commonly used in:
- Programming languages (e.g., Python, Java, JavaScript).
- Text editors (e.g., VS Code, Sublime Text).
- Command-line tools (e.g., grep, sed).

## **Core Components**
1. **Literals**: Matches exact text (e.g., `cat` matches "cat").
2. **Metacharacters**: Special characters for advanced pattern matching (e.g., `.` for any character).
3. **Quantifiers**: Define how many times a pattern should appear (e.g., `a*` matches "a", "aaa").
4. **Character Classes**: Specify sets of characters (e.g., `[a-z]` for all lowercase letters).
5. **Anchors**: Define start (`^`) or end (`$`) positions in text.

## **Example Patterns**
| Pattern       | Matches                                      |
|---------------|----------------------------------------------|
| `^Hello`      | Strings starting with "Hello".              |
| `[0-9]{3}`    | Any sequence of exactly 3 digits.           |
| `(cat|dog)`   | Either "cat" or "dog".                      |
| `\bword\b`    | The word "word" as a whole word.            |

## **Applications**
- **Search and Replace**: Modifying text efficiently.
- **Data Validation**: Validating email addresses, phone numbers, etc.
- **Text Extraction**: Extracting specific data from logs, files, etc.

## **Getting Started**
To use Regex in your project, refer to the documentation of your programming language. Example for Python:
```python
import re

# Matching a pattern
pattern = r"\d{3}-\d{2}-\d{4}"
text = "My number is 123-45-6789."
match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
