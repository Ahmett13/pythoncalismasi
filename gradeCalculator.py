def GradeCalculator():
    import time
    midterm = input("Midterm = ")
    final = input("Final = ")
    average = (float(midterm)*0.4)+(float(final)*0.6)
    print(f"Your average {average}")

    time.sleep(1)
    if average >= 60:
        print("Congralutations, you passed :)")

    else: print("You failed :(")