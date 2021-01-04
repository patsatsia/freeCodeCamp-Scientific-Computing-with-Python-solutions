def arithmetic_arranger(problems, with_answers = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    full_answers = []
    for example in problems:
        if example.split()[1] != "+" and example.split()[1] != "-":
            return "Error: Operator must be '+' or '-'."

        try:
            first_operand = int(example.split()[0])
            second_operand = int(example.split()[2])
        except:
            return "Error: Numbers must only contain digits."

        if len(str(first_operand)) > 4 or len(str(second_operand)) > 4:
            return "Error: Numbers cannot be more than four digits."
        operator = example.split()[1]
        answer = 0
        if operator == "+":
            answer = first_operand + second_operand
        elif operator == "-":
            answer = first_operand - second_operand
        else:
            print("get the fuck out of here")

        length = 0
        line1_len = len(str(first_operand))
        line2_len = len(str(second_operand))

        if line1_len >= line2_len:
            length = line1_len + 2
        else:
            length = line2_len + 2

        
        if with_answers == True:
            solution = (f"{first_operand}".rjust(length)+ "\n" f"{operator}" + " " + f"{second_operand}".rjust(length-2) + "\n" +  ("-"*(length)) + "\n" + f" {answer}".rjust(length))
        else:
            solution = (f"{first_operand}".rjust(length)+ "\n" f"{operator}" + " " + f"{second_operand}".rjust(length-2) + "\n" +  ("-"*(length)))
        full_answers.append((solution))

    formated_full_answers = []
    for t in full_answers:
        x = t.split("\n")
        formated_full_answers.append(x)


    final_strings = []
    if with_answers == True:
        loop_range = 4
    else:
        loop_range = 3
    for num in range(loop_range):
        x = ""

        for num2 in range(len(problems)):
            x += formated_full_answers[num2][num] + "    "

        x = x.rstrip()
        final_strings.append(x)
    
    
    arranged_problems = "\n".join(final_strings)
    return arranged_problems

