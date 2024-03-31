def remove_last_line(input_path: str, output_path: str) -> None:
    with open(input_path, mode="r") as input:
        with open(output_path, mode="w") as output:
            output.writelines([line for line in input.readlines()][:len(input.readlines())-1])
            
            
input_path = "hw_2024_04_03/resources/remove_input.txt"
output_path = "hw_2024_04_03/resources/remove_output.txt"
remove_last_line(input_path, output_path)