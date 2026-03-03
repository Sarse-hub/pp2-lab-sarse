import re
import json

# ---------------------------------------------------------------------------
# Section A: regular expression exercises from W3Schools
# ---------------------------------------------------------------------------

def regex_exercises():
    print("=== RegEx Exercises ===")

    # 1. a followed by zero or more b's
    pattern1 = re.compile(r"^ab*$")
    tests1 = ["a", "ab", "abb", "ac", "b"]
    print("1:", [s for s in tests1 if pattern1.match(s)])

    # 2. a followed by two to three b's
    pattern2 = re.compile(r"^ab{2,3}$")
    tests2 = ["ab", "abb", "abbb", "abbbb"]
    print("2:", [s for s in tests2 if pattern2.match(s)])

    # 3. sequences of lowercase letters joined with underscore
    text3 = "snake_case example, notCamel, another_one"
    print("3:", re.findall(r"[a-z]+_[a-z]+", text3))

    # 4. one uppercase letter followed by lowercase letters
    text4 = "Hello there General Kenobi"  # "Hello" -> match
    print("4:", re.findall(r"[A-Z][a-z]+", text4))

    # 5. 'a' followed by anything, ending in 'b'
    pattern5 = re.compile(r"^a.*b$")
    tests5 = ["ab", "axxb", "abx", "a123b"]
    print("5:", [s for s in tests5 if pattern5.match(s)])

    # 6. replace spaces, comma, dot with colon
    text6 = "one two,three.four"
    print("6:", re.sub(r"[ ,\.]+", ":", text6))

    # 7. snake case to camel case
    def snake_to_camel(s):
        parts = s.split("_")
        return parts[0] + ''.join(p.title() for p in parts[1:])
    print("7:", snake_to_camel("this_is_snake_case"))

    # 8. split string at uppercase letters
    def split_at_upper(s):
        return re.split(r"(?=[A-Z])", s)
    print("8:", split_at_upper("CamelCaseString"))

    # 9. insert spaces between words starting with capital letters
    text9 = "ThisIsASentence"
    print("9:", re.sub(r"(?<!^)(?=[A-Z])", " ", text9))

    # 10. camel case to snake case
    def camel_to_snake(s):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()
    print("10:", camel_to_snake("camelCaseString"))


# ---------------------------------------------------------------------------
# Section B: receipt parsing logic
# ---------------------------------------------------------------------------

def parse_receipt(text: str) -> dict:
    # all prices preceded by $ or without
    prices = re.findall(r"\$?\d+\.\d{2}", text)
    prices = [p.strip("$") for p in prices]

    # items (ignore subtotal, tax, total)
    items = []
    for m in re.finditer(r"^(.*?)\s+\$?(\d+\.\d{2})$", text, re.MULTILINE):
        name = m.group(1).strip()
        if re.search(r"subtotal|tax|total", name, re.IGNORECASE):
            continue
        items.append({"name": name, "price": float(m.group(2))})

    total = None
    m_total = re.search(r"total[:\s]+\$?(\d+\.\d{2})", text, re.IGNORECASE)
    if m_total:
        total = float(m_total.group(1))

    date_time = None
    m_dt = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", text)
    if m_dt:
        date_time = m_dt.group(1)

    payment_method = None
    m_pay = re.search(r"payment\s*method[:\s]+(.+)", text, re.IGNORECASE)
    if m_pay:
        payment_method = m_pay.group(1).strip()

    return {
        "prices": prices,
        "items": items,
        "total": total,
        "date_time": date_time,
        "payment_method": payment_method,
    }


# ---------------------------------------------------------------------------
# If executed as script, run exercises and parse the provided raw.txt
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    regex_exercises()

    try:
        with open("raw.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("raw.txt not found in current directory")
        text = ""

    print("\n=== Receipt Parsing ===")
    result = parse_receipt(text)
    print(json.dumps(result, indent=2))
