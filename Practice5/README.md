# Practice5 - Python Regular Expressions & Receipt Parsing

This folder contains exercises focused on Python regular expressions and a practical receipt parsing task. The repository structure is:

```
Practice5/
├── receipt_parser.py   # Contains regex exercises and receipt parser
├── raw.txt             # Sample receipt data used by the parser
└── README.md           # This document
```

## 2.1 Python RegEx Exercises
The first section of `receipt_parser.py` covers topics from the W3Schools tutorial:

- Introduction to regex and metacharacters
- Special sequences (`\d`, `\w`, `\s`, etc.)
- Character classes and sets
- Quantifiers (`*`, `+`, `{n}`, `{n,}`, `{n,m}`)
- Searching with `re.search`, `re.findall`, `re.split`, `re.sub`, `re.match`
- Using flags like `re.IGNORECASE` and `re.MULTILINE`

The file contains ten numbered exercises; running the script will print solutions and demonstrate patterns.

## 2.2 Practical Exercise: Receipt Parsing
`raw.txt` holds a simulated grocery receipt. The parser extracts:

- All prices (with or without `$` sign)
- Item names with their prices (ignoring subtotal/tax lines)
- Total amount
- Date and time stamp
- Payment method

The output is printed in JSON format for easy consumption.

### Example invocation

```bash
cd Practice5
env\Scripts\activate       # if you use virtualenv
python receipt_parser.py
```

## 2.3 GitHub Instructions
To save your work:

```bash
git add .
git commit -m "Add Practice5 - Python regex exercises and receipt parser"
git push origin main
```

Feel free to experiment with your own regex patterns and extend the parser to handle different receipt formats.
