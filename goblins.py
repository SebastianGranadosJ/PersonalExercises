gamers = []
def add_gamer  (gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

kimberly = {"name":"kimberly", "availability":["Mondays", "Tuesdays", "Fridays"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def build_daily_frequency_table():
    return {"Monday":0, "Tuesday":0, "Wednesday":0,"Thursday":0, "Friday":0,"Saturday":0, "Sunday":0}
count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list,available_frequency):
    for days in available_frequency.keys():
        for gamer in gamers_list:
            if days in gamer['availability']:
                available_frequency[days] += 1

calculate_availability(gamers, count_availability)

def find_best_nigh(availability_table):
    x = 0
    the_day = ""
    for days, people in availability_table.items():
        if people > x:
            x = people
            the_day = days
    return the_day
game_night = find_best_nigh(count_availability)

def available_on_night(gamers_list, day):
    available = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            available.append(gamer["name"])
    return available


attending_game_night = available_on_night(gamers, game_night)

form_email = form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
    for name in gamers_who_can_attend:
        print("""
        Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day} and have a blast!

Magically Yours,
the Sorcery Society
""".format(name = name, day = day, game = game))



unable_to_attend_best_night = []
for gamer in gamers:
    if not gamer['name']  in attending_game_night:
        unable_to_attend_best_night.append(gamer)
print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_nigh(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers,second_night)
send_email(available_second_game_night,second_night,"Abruptly Goblins!")
