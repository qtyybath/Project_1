#2.(необов'язкове виконання) Написати власний менеджер контексту, задачею якого буде
# друкувати "==========" – 10 знаків дорівнює перед виконанням коду та після виконання коду,
# таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом,
# проте програма не має завершити своєї роботи.


class MyContextManager:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_value, traceback):
        print("=" * 10)
        if exc_type is not None:
            print(f"Error: {exc_type} - {exc_value}")
        return True


file = open("ame.txt", "r")


with MyContextManager():
    print(file.read())
