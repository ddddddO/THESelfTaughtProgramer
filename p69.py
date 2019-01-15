#1
def square():
    """
    Returns int(x) ** 2.
    :return: x ** 2.
    """
    x = input("in number:")
    try:
        return int(x) ** 2
    except ValueError:
        return

#print(square())

#2
def disp(s):
    """
    :param s: string.
    """
    print(str(s))

#disp("sdsds")

#3
def introduce(name, hobby, age, blood="B", weight=46):
    """
    :param name: string.
    :param hobby: string.
    :param age: int.
    :param blood: string.
    :param weight: int.
    """
    print('私は、{}。体重は、{}kg。趣味は、{}。血液型は、{}。歳は、{}'.format(name, weight, hobby, blood, age))

#introduce("daiki", "cycle", 26)
#introduce("daiki", "cycle", 26, "A", 100)

#4
def division(x):
    """
    Returns x // 2.
    :param x: int.
    :return: // 2
    """
    return x // 2

def yonbai(x):
    """
    Returns 4 * x
    :param x: int
    :returns: * 4
    """
    return 4 * x

#xx = division(7)
#print(yonbai(xx))

#5
def return_float(sf):
    """
    Returns float(sf)
    :param sf: string
    :return: float(sf)
    """
    try:
        return float(sf)
    except ValueError:
        print("invalid value!")
        return

#print(return_float(9999999999999999999999999999999999999999999999999))

#6 docstring