even = True
while True:
    try:
        text = input()
    except EOFError:
        break

    new_text = []
    for ch in text:
        if ch == "\"":
            if even:
                new_text.append("``")
                even = False
            else:
                new_text.append("''")
                even = True
        else:
            new_text.append(ch)

    print("".join(new_text))
