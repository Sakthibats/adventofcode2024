

def part1():
    # init array
    fin = 0

    # Read the file and process line by line
    file_path = 'input.txt'  # Replace with your file path
    with open(file_path, 'r') as file:
        for line in file:
            numbers = [char for char in line if char.isdigit()]
            num = int(numbers[0] + numbers[-1])
            # print(num)
            fin+=num

    print(fin)

def replace_spelled_numbers(s):
    # Mapping of spelled-out numbers to digits
    number_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    num = ""

    # for i in range(len(s)-5):
    #     strr = s[i:i+5]
    #     for word, digit in number_map.items():
    #         if word in strr:
    #             strr = strr.replace(word, digit)
    #             num+=digit
    #             break
    #     if len(num)>0:
    #         break

    for i in range(len(s)-5):
        strr = s[-i-5-1:-i-1]
        print(strr)
        # for word, digit in number_map.items():
        #     if word in strr:
        #         strr = strr.replace(word, digit)
        #         num+=digit
        #         break
        # if len(num)>1:
        #     break
    # print(num)
    
    return s

def part2():
    # init array
    fin = 0

    # Read the file and process line by line
    file_path = 'input.txt'  # Replace with your file path
    with open(file_path, 'r') as file:
        for line in file:
            replace_spelled_numbers(line)
            # numbers = [char for char in line if char.isdigit()]
            # num = int(numbers[0] + numbers[-1])
            # print(num)
            # fin+=num

    print(fin)
        
part2()

