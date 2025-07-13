# dispatch the packages to the correct stack according to their volume and mass

# sort:
# bulky = vol >= 1,000,000 cm3 OR one of the dimensions is >= 150 cm
# heavy = mass >= 150cm
# ht and lgth in cm
# mass in kg
# return string (name of stack where package should go)

# dispatch:
# standard = not bulky OR not heavy --> handle normally
# special = either heavy OR bulky --> cant be handled automatically
# rejected = bulky AND heavy --> rejected


