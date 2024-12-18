def sieve_of_eratosthenes(n):
    # Инициализируем список, где индекс будет представлять число
    is_prime = [True] * (n + 1)
    p = 2  # Начинаем с первого простого числа

    while p * p <= n:
        # Если is_prime[p] не изменился, значит p является простым
        if is_prime[p]:
            # Обозначаем все кратные p как составные
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Собираем все простые числа в список
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

# Пример использования
n = 30  # Задаем предел
print(sieve_of_eratosthenes(n))
