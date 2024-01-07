class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    """ Arithmetic Operators """
    # +
    def __add__(self, other):
        z = Complex()
        z.__real = self.__real + other.__real
        z.__imag = self.__imag + other.__imag
        return z

    # -
    def __sub__(self, other):
        z = Complex()
        z.__real = self.__real - other.__real
        z.__imag = self.__imag - other.__imag
        return z

    # *
    def __mul__(self, other):
        z = Complex()
        z.__real = self.__real * other.__real
        z.__imag = self.__imag * other.__imag
        return z

    # /
    def __truediv__(self, other):
        z = Complex()
        z.__real = self.__real / other.__real
        z.__imag = self.__imag / other.__imag
        return z

    # %
    def __mod__(self, other):
        z = Complex()
        z.__real = self.__real % other.__real
        z.__imag = self.__imag % other.__imag
        return z

    """ Display Arithmetic Output """
    def display(self):
        print(self.__real, self.__imag)
