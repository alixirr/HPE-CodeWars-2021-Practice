try:
    with open(r"input.txt", "r") as f:
        lines = []

        for line in f:
            lines.append(line.rstrip())

    lines.pop(0)
    lines.reverse()

    for line in lines:
        print(line)

except Exception as e:
    print("An error occurred:", str(e))