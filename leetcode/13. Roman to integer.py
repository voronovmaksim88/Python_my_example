s = "DCXXI"
integer = 0

i = 0
while i < len(s):
    if len(s) == 1 or \
            i == (len(s) - 1) and len(s) > 1:  # строка из одного символа или последний символ
        if s[i] == "I":
            integer += 1
        if s[i] == "V":
            integer += 5
        if s[i] == "X":
            integer += 10
        if s[i] == "L":
            integer += 50
        if s[i] == "C":
            integer += 100
        if s[i] == "D":
            integer += 500
        if s[i] == "M":
            integer += 1000
        break

    if i < (len(s) - 1) and len(s) > 1:
        if s[i] == "I" and s[i + 1] == "V":
            integer += 4
            i += 2
            continue

        if s[i] == "I" and s[i + 1] == "X":
            integer += 9
            i += 2
            continue

        if s[i] == "I" and s[i + 1] != "V" and s[i + 1] != "X":
            integer += 1
            i += 1
            continue

        if s[i] == "V":
            integer += 5
            i += 1
            continue

        if s[i] == "X" and s[i + 1] == "L":
            integer += 40
            i += 2
            continue

        if s[i] == "X" and s[i + 1] == "C":
            integer += 90
            i += 2
            continue

        if s[i] == "X" and s[i + 1] != "C" and s[i + 1] != "D":
            integer += 10
            i += 1
            continue

        if s[i] == "L":
            integer += 50
            i += 1
            continue

        if s[i] == "C" and s[i + 1] == "D":
            integer += 400
            i += 2
            continue

        if s[i] == "C" and s[i + 1] == "M":
            integer += 900
            i += 2
            continue

        if s[i] == "C" and s[i + 1] != "D" and s[i + 1] != "M":
            integer += 100
            i += 1
            continue

        if s[i] == "D":
            integer += 500
            i += 1
            continue

        if s[i] == "M":
            integer += 1000
            i += 1
            continue

print(integer)
