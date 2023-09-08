#Код соответствует императивной, структурной и процедурной парадигмам

def print_mult_table(n):
    if n < 1 or n > 9:
        print("Необходимо ввести значение от 1 до 9")
    else:
        for i in range(1, n + 1):
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

def main():
    print_mult_table(3)

if __name__ == "__main__":
    main()
