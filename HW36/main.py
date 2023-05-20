# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(oper, num_rows=6, num_columns=6):
    a = [0] * num_rows
    for i in range(num_rows):
        a[i] = [0]*num_columns

    for i in range(num_rows):
        for j in range(num_columns):
            a[i][j] = oper(i+1,j+1)
    print(f'число строк {num_rows}')
    print(f'число столбцов {num_columns}')
    print()
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print()

print_operation_table(lambda x,y: x*y,7,8)