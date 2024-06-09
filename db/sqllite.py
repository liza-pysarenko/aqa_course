import sqlite3


def create_db():
    connection = sqlite3.connect('shop.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


def add_products():
    products = [
        ('Orange', 0.5, 100),
        ('Apple', 0.3, 200),
        ('Banana', 0.2, 150)
    ]

    connection = sqlite3.connect('shop.db')
    cursor = connection.cursor()

    cursor.executemany('''
        INSERT INTO Products (name, price, quantity)
        VALUES (?, ?, ?)
    ''', products)

    connection.commit()
    connection.close()


def show_products():
    connection = sqlite3.connect('shop.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    print("All Products:")
    for product in all_products:
        print(product)

    cursor.execute('SELECT * FROM Products WHERE price > 0.25')
    expensive_products = cursor.fetchall()
    print("\nProducts with price higher than 0.25:")
    for product in expensive_products:
        print(product)

    cursor.execute('UPDATE Products SET price = 0.25 WHERE name = "Banana"')
    connection.commit()
    print("\nUpdated the price of Banana to 0.25:")
    cursor.execute('SELECT * FROM Products WHERE name = "Banana"')
    updated_banana_price = cursor.fetchall()
    for product in updated_banana_price:
        print(product)

    cursor.execute('DELETE FROM Products WHERE name = "Apple"')
    connection.commit()
    print("\nDeleted Apple from Products:")
    cursor.execute('SELECT * FROM Products')
    remaining_products = cursor.fetchall()
    for product in remaining_products:
        print(product)

    connection.close()


def main():
    create_db()
    add_products()
    show_products()


if __name__ == "__main__":
    main()
