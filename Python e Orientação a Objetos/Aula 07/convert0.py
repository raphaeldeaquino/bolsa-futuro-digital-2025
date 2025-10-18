def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU é {convert(au)} m")


def convert(au):
    return au * 149597870700


if __name__ == "__main__":
    main()