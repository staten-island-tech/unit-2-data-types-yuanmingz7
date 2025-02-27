def vote(age, id):
    if age< 18 or id == False:
        print("cannot vote")
    elif age >18 and id == True:
        print("vote")


def skins(money, age, isAvailable):
    if money < 10 or age < 18 or isAvailable ==False:
        return ("cannotbuy")
def skins2(money, cost, isAvailable):
    if isAvailable == True:
        if money > 10 or cost == 0:
            print()