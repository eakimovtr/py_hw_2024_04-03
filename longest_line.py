def find_longest_line(input_path: str) -> int:
    with open(input_path, mode="r") as input:
        return max(map(len, input.readlines()))
    
    
input_path = "hw_2024_04_03/resources/longest_line.txt"
print(find_longest_line(input_path))