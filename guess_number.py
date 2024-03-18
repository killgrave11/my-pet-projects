import random

tries = 0

number = random.randint(1, 100)

print("Я загадал число от 1 до 100. Попробуйте угадать его. У вас 10 попыток.")

while tries <= 10:
    guess = int(input("Ваше число: "))
    
    tries += 1
    
    if guess < number:
        print("Я загадал число больше.")
    
    if guess > number:
        print("Я загадал число меньше.")
        
    if guess == number:
        print(f"Поздравляю! Вы угадали за {tries} попыток!")
        break
        
    if guess != number and tries == 11:
        print(f"Мои соболезнования, вы проиграли. Я загадал число {number}")
        break
