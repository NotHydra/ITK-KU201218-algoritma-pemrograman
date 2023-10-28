print()

with open("raw-text-file.txt", "r") as f_input:
    with open("converted-text-file.txt", "w") as f_output:
        print("Converting File...")
        f_output.write(f_input.read().replace("\n", ""))
        print("File Conversion Done...")
