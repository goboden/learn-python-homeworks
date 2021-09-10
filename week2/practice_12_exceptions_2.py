
class TooMuchDiscount(Exception):
    def __init__(self):
        self.text = 'Слишком большая максимальная скидка'


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise TooMuchDiscount
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        return 'Исключение ValueError'
    except TypeError:
        return 'Исключение TypeError'
    except TooMuchDiscount as ex:
        return ex.text


def main():
    print(discounted(100, 10))
    print(discounted(100, 30))
    print(discounted(100, 30, 50))
    print(discounted(100, 30, 150))
    print(discounted(100, []))
    print(discounted(100, 30, 'abc'))


if __name__ == '__main__':
    main()
