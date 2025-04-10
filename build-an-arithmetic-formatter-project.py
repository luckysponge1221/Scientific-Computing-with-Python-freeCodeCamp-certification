def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_lines = []
    second_lines = []
    third_lines = []
    results = []

    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."

        elements = problem.split()
        first = elements[0]
        operand = elements[1]
        second = elements[2]

        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_len = len(first)
        second_len = len(second)
        spacing = max(first_len, second_len) + 2

        first_line = f'{first.rjust(spacing)}'
        first_lines.append(first_line)

        second_line = f'{operand} {second.rjust(spacing-2)}'
        second_lines.append(second_line)

        line = '-'*spacing
        third_lines.append(line)

        if operand == '+':
            result = str(int(first) + int(second))
        elif operand == '-':
            result = str(int(first) - int(second))
        results.append(result.rjust(spacing))

    final = '    '.join(first_lines) + '\n' + '    '.join(second_lines) + '\n' + '    '.join(third_lines)

    if show_answers == True:
        final += '\n' + '    '.join(results)
    
    return final

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

arithmetic_arranger(["3801 - 2", "123 + 49"])

arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
