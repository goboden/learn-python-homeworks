
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(discount)
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        return 'Исключение ValueError'
    except TypeError:
        return 'Исключение TypeError'


def main():
    print(discounted(100, 10))
    print(discounted(100, 30))
    print(discounted(100, 30, 50))
    print(discounted(100, 30, 150))
    print(discounted(100, 'abc'))
    print(discounted(100, 30, 'abc'))


if __name__ == '__main__':
    main()
