from enum import Enum


# dispatch the packages to the correct stack according to their volume and mass

# sort:
# bulky = vol >= 1,000,000 cm3 OR one of the dimensions is >= 150 cm
# heavy = mass >= 20kg
# ht and lgth in cm
# mass in kg
# return string (name of stack where package should go)

# dispatch:
# standard = not bulky OR not heavy --> handle normally
# special = either heavy OR bulky --> cant be handled automatically
# rejected = bulky AND heavy --> rejected

class DispatchCategory(str, Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def sort(width: float, height: float, length: float, mass: float) -> DispatchCategory:
    volume = width * height * length  # in cm^3
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20  # in kg

    match (is_bulky, is_heavy):
        case (True, True):
            return DispatchCategory.REJECTED
        case (True, False) | (False, True):
            return DispatchCategory.SPECIAL
        case (False, False):
            return DispatchCategory.STANDARD


def test_sort():
    try:
        assert sort(100, 100, 100, 10) == DispatchCategory.SPECIAL  # bulky, not heavy
        assert sort(200, 50, 10, 5) == DispatchCategory.SPECIAL # bulky, not heavy
        assert sort(100, 100, 100, 25) == DispatchCategory.REJECTED # bulky, heavy
        assert sort(200, 200, 200, 25) == DispatchCategory.REJECTED # bulky, heavy
        assert sort(149, 149, 149, 19.9) == DispatchCategory.SPECIAL # bulky, not heavy
        assert sort(150, 100, 100, 19.9) == DispatchCategory.SPECIAL # bulky, not heavy
        assert sort(100, 100, 100, 20) == DispatchCategory.REJECTED #  bulky, heavy
        assert sort(1000, 1000, 1, 20) == DispatchCategory.REJECTED # bulky, heavy
        assert sort(100, 100, 80, 19.9) == DispatchCategory.STANDARD # not bulky, not heavy
        assert sort(100, 90, 80, 15) == DispatchCategory.STANDARD # not bulky, not heavy
    except AssertionError as e:
        print("test failed")
        raise
    print("all tests passed.")


if __name__ == "__main__":
    test_sort()    