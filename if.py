number = 88
guess = int(input('Привет! Введите целое число:'))
if guess == number:
    print('Мои поздравления! Ты гений!')
elif guess > number:
    print('Нет, загаданное число немного больше этого.')
else:
    print('Нет, загаданное число немного меньше этого.')
    print('Игра завершена.')