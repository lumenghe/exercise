def calculate(nathanael, gabriel):
    maman = nathanael
    nathanael = nathanael + gabriel
    gabriel = maman

    return nathanael, gabriel


gabriel = 0
nathanael = 1

for i in range(10):
    nathanael, gabriel = calculate(nathanael, gabriel)
    print(f"{i}:nathanael={nathanael}, gabriel={gabriel}, maman={maman}")
