CHEESES = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]}")


def summon_captain_planet(planeteer_calls):
    titled_elements = [e.title() for e in planeteer_calls]
    return [e + "!" for e in titled_elements]

def long_planeteer_calls(call_list):
    for c in call_list:
        if len(c) > 4:
            return True
    
    return False

def find_the_cheese(str_list):
    for str in str_list:
        if str in CHEESES:
            return str
        
    return None
