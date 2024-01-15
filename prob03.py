try:
    with open(r"input.txt", "r") as f:
        # Initialize a list to store lines
        lines = []

        # Read each line from the file and append to the list
        for line in f:
            lines.append(line.rstrip())  # rstrip removes newline characters at the end

    # Now 'lines' contains each line from the file
    # You can access individual lines using indexing (e.g., lines[0], lines[1], ...)
    # Or iterate through the lines as needed
    # for i, line in enumerate(lines):
    #     print(f"Line {i + 1}: {line}")
    y = 0
    x = 0
    printed = False
    
    for line in lines:
        x = 0
        
        for char in line:
            if (char == "P"):
                print("Ace, move fast, pigeon is at (" + str(x) + ", " + str(y) + ")")
                printed = True
            x += 1
        y += 1

    if (printed == False):
        print("No pigeon, try another map, Ace")   

except Exception as e:
    print("An error occurred:", str(e))
