with open(r"input.txt", "r") as f:
    lines = []

    for line in f:
        lines.append(line.rstrip())

    length = int(lines.pop(0))

    birthday = []

    for date in lines:
        birthday.append(date[0:5])

    repeated = []
    for i in range(length):
        k = i + 1
        for j in range(k, length):
            if birthday[i] == birthday[j] and birthday[i] not in repeated:
                repeated.append(birthday[i])
    
    print(len(repeated))
    if len(repeated) == 0:
        print("\nduplicates: None")
    else:
        print("duplicates: ", end = "")
        for i in range(len(repeated)):
            print(repeated[i], end = " ")