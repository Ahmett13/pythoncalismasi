def incalculator():
    a = int(input("İlk sayıyı giriniz "))
    hesaplama = str(input("İşlemi Giriniz "))
    b = int(input("2. sayıyı giriniz "))

    if hesaplama == "+":
        print(f"{a} + {b} = {a+b}")
    elif hesaplama == "-":
        print(f"{a} - {b} = {a-b}")
    elif hesaplama == "*":
        print(f"{a} * {b} = {a*b}")
    elif hesaplama == "/":
        if b == 0:
            print("Tanımsız")
        else:print(f"{a} / {b} = {a/b}")