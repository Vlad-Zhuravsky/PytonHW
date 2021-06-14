def power(x, y):
    x, y = float(x), int(y)
    if x <= 0 or y >= 0:
        return "х должен быть больше 0, а у меньше 0"
    else:
        result = 1
        for _ in range(abs(y)):
            result *= 1 / x
        return f"результат возведения х в степень у: {round(result,6)}"