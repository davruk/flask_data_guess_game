with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines()

    for line in ninja_lines:
        print(line)
