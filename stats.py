def write_stats(src_path: str, output_path: str) -> None:
    count_lines: int = 0
    count_symbols: int = 0
    count_vowels: int = 0
    count_consonants: int = 0
    count_digits: int = 0
    
    with open(src_path, mode="r") as src:
        count_lines = len(src.readlines())
        src_name = src.name
        src.seek(0)
        src_str = src.read()
        for char in src_str:
            char: str
            if char.isspace():
                continue
            count_symbols += 1
            if char.isnumeric():
                count_digits += 1
            if char.isalpha():
                if char in ['a','e','i','o','u']:
                    count_vowels += 1
                else:
                    count_consonants += 1
    
    with open(output_path, mode="w") as output:
        output.write(f"{src_name}\n")
        output.write(f"Lines: {count_lines}\n")
        output.write(f"Symbols: {count_symbols}\n")
        output.write(f"Vowels: {count_vowels}\n")
        output.write(f"Consonants: {count_consonants}\n")
        output.write(f"Digits: {count_digits}")

src_path = "hw_2024_04_03/resources/stats_src.txt"
output_path = "hw_2024_04_03/resources/stats_output.txt"
write_stats(src_path, output_path)