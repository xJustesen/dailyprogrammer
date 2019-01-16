def upc(numbers):
    ''' Given an 11 digit number as a string, this function calculates the 12th digit that would make a valid UPC.
        If the string has fewer than 11 digits, zeros are appended to the front of the string.
    '''

    if len(numbers) < 11:
        numbers = "0" * (11 - len(numbers)) + numbers

    odds = [int(i) for i in numbers[::2]]
    evens = [int(i) for i in numbers[1::2]]
    M = (3 * sum(odds) + sum(evens)) % 10
    return 0 if M == 0 else 10 - M

def main():
    a = "4210000526"
    b = "3600029145"
    c = "12345678910"
    d = "1234567"

    print("upc(" + str(a) + ") => " + str(upc(a)))
    print("upc(" + str(b) + ") => " + str(upc(b)))
    print("upc(" + str(c) + ") => " + str(upc(c)))
    print("upc(" + str(d) + ") => " + str(upc(d)))

if __name__ == '__main__':
    main()
