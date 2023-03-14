def roll_call_dwarves(dwarves):
    count = 1
    for dwarf in dwarves:
        print(f"{count}. {dwarf}")
        count += 1


def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]


def long_planeteer_calls(list):
    for call in list:
        if len(call) > 4:
            return True
    return False


def find_the_cheese():
    pass
