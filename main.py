
import doctest

from BoyerMoore import BoyerMoore

def main(wanted_tape, full_tape, isPrint = False):
    """ 

    >>> main("11123444445", "4445555444111234444454444444444441112344445")
    [10]
    >>> main("1332", "111111")
    []
    >>> main("1332", "13321332")
    [0, 4]

    """
    boyerMoore = BoyerMoore(wanted_tape)
    result = boyerMoore.find_in(full_tape)

    if isPrint:
        for i in result:
            print(f"Was founded in {i}")

    return result

if __name__ == "__main__":
    doctest.testmod()
    #main("1132", "321412412123121132", True)
    