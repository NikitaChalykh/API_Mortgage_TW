def mortgage_calculator(obj, price, deposit, term=None):
    # пропорция для нахождения годовой ставки
    ratio = ((int(price) - int(deposit)) - obj.payment_min) / (
        obj.payment_max - obj.payment_min
    )
    # годовая ставка по кредиту
    rate = obj.rate_min + (obj.rate_max - obj.rate_min) * ratio
    if term is None:
        return rate
    # ежемесячная процентная ставка по кредиту
    month_rate = rate / 1200
    # общая ставка по кредиту
    global_rate = (1 + month_rate) ** (int(term) * 12)
    # расчитываем аннуитентный платеж
    return ((int(price) - int(deposit)) * month_rate * global_rate) / (
        global_rate - 1
    )
