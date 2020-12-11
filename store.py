from typing import List, Dict
from time import sleep

from model.product import Product
from utils.helper import format_float_str

products: List[Product] = []
car: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('#######################')
    print('=======  Welcome  ========')
    print('=======  Shopping  =======')
    print('#######################')


    print('Choise an option below: ')
    print('1 - Register Product')
    print('2 - List Product')
    print('3 - Pay Products')
    print('4 - Visual Car')
    print('5 - Close Order')
    print('6 - Exit')


    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        pay_product()
    elif option == 4:
        visual_car()
    elif option == 5:
        close_oder()
    elif option == 6:
        print('Check back Often')
        sleep(2)
        exit()
    else:
        print('Invalid Option')
        sleep(1)
        menu()


def register_product() -> None:
    print('Register Products')
    print('===================')


    name: str = input('Please inform the product name:')
    price: float = float(input('Inform prince product:'))

    product: Product = Product(name, price)

    products.append(products)

    print(f'The Product {product.name} was successfully registered')
    sleep(2)
    menu()

def list_products() -> None:
    if len(products) > 0:
        print('Product Listing')
        print('===================')
        for product in products:
            print(product)
            print('================')
            sleep(1)
    else:
        print('No exist product register')
    sleep(2)
    menu()


def take_product():
    pass


def pay_product() -> None:
    if len(products) > 0:
        print('Inform the code product you want to car')
        print('======================================')
        print('========== Available Product ===============')
        for product in products:
            print(product)
            print('==========================================')
            sleep(1)
        code: int = int(input())

        product: products = take_product(code)

        if product:
            if len(car) > 0:
                has_car: bool = False
                for item in car:
                    qnt: int = int.get(product)
                    if qnt:
                        item[product] = qnt + 1
                        print(f'Product {product.name} has {qnt +1 } drive in cart ')
                        has_car = True
                        sleep(2)
                        menu()
                if not has_car:
                    prod = {product: 1}
                    car.append(prod)
                    print(f'The product {product.name} was added to the cart')
                    sleep(2)
                    menu()

            else:
                item = {product: 1}
                car.append(item)
                print(f'The product {product.name} was added to the cart')
                sleep(2)
                menu()
        else:
            print(f'The product {code} was not found')
            sleep(2)
            menu()
    else:
        print('No exist products')
    sleep(2)
    menu()

def visual_car() -> None:
    if len(car) > 0:
        print('Products in the car:')

        for item in car:
            for dados in item.items():
                print(dados[0])
                print(f'Amount {dados[1]}')
                print('============')
                sleep(1)
    else:
        print('No exist product')
        sleep(2)
        menu()

def close_oder() -> None:
    if len(car) > 0:
        value_total: float = 0

        print("Car's product")
        for item in products:
            for dados in item.item():
                print(dados[0])
                print(f'Qnt: {dados[1]}')
                value_total += dados[0].price + dados[1]
                print('=================================')
                sleep(2)
        print(f'Your Bill is {format_float_str(value_total)}')
        print('Check back Often')
        car.clear()
        sleep()
    else:
        print('No exist product register')
    sleep(2)
    menu()

def product_code(code: int) -> Product:
    pr: Product = None

    for product in products == code:
        if product.code == code:
            pr = product

    return pr

if __name__ == '__main__':
    main()



