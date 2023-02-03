import redis

client = redis.Redis(host="redis", port=6379)

if __name__ == '__main__':
    while True:
        user_input = input('Выберите действие:\n'
                           '1. Вычислить арифметическое выражение\n'
                           '2. Завершить программу\n'
                           '>>> ')

        match user_input:
            case '1':
                some_input = input('>>> Введите пример: ')
                client.lpush("queue", some_input)
            case '2':
                print('Вы завершили программу')
                break
