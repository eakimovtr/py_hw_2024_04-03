def check_equal_lines(file1, file2) -> list[tuple]:
    unequal_lines: list[tuple] = []
    for lines_pair in zip(file1, file2):
        if lines_pair[0] != lines_pair[1]:
            unequal_lines.append(lines_pair)
    return unequal_lines
            
        
        
file1 = open("hw_2024_04_03/resources/eq_lines_1.txt", mode="r")
file2 = open("hw_2024_04_03/resources/eq_lines_2.txt", mode="r")
print(check_equal_lines(file1, file2))