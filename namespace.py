def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Если мы попытаемся вызвать inner_function вне test_function,
# мы получим ошибку, поскольку inner_function
# определяется только в рамках test_function.

test_function()

