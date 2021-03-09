with open("csv_data.txt", "r") as list_file:
    csv_lines = list_file.read().splitlines()

# split lines method
    for row in csv_lines:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
