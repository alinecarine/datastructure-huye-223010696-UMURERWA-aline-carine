stack_basketball = []
stack_football = []
stack_swimming = []


def push_team(sport, team):
    if sport == "Basketball":
        stack_basketball.append(team)
        print(f"Team '{team}' registered for Basketball.")
    elif sport == "Football":
        stack_football.append(team)
        print(f"Team '{team}' registered for Football.")
    elif sport == "Swimming":
        stack_swimming.append(team)
        print(f"Team '{team}' registered for Swimming.")


def pop_team(sport):
    if sport == "Basketball" and stack_basketball:
        team = stack_basketball.pop()
        print(f"Undo registration of team '{team}' for Basketball.")
    elif sport == "Football" and stack_football:
        team = stack_football.pop()
        print(f"Undo registration of team '{team}' for Football.")
    elif sport == "Swimming" and stack_swimming:
        team = stack_swimming.pop()
        print(f"Undo registration of team '{team}' for Swimming.")
    else:
        print(f"No teams to undo for {sport}.")

push_team("Basketball", "Team A")
push_team("Football", "Team B")
push_team("Swimming", "Team C")

pop_team("Basketball")
pop_team("Football")
pop_team("Swimming")

queue_basketball = []
queue_football = []
queue_swimming = []


def schedule_match(sport, match):
    if sport == "Basketball":
        queue_basketball.append(match)
        print(f"Match '{match}' scheduled for Basketball.")
    elif sport == "Football":
        queue_football.append(match)
        print(f"Match '{match}' scheduled for Football.")
    elif sport == "Swimming":
        queue_swimming.append(match)
        print(f"Match '{match}' scheduled for Swimming.")


def process_match(sport):
    if sport == "Basketball" and queue_basketball:
        match = queue_basketball.pop(0)
        print(f"Processing match '{match}' for Basketball.")
    elif sport == "Football" and queue_football:
        match = queue_football.pop(0)
        print(f"Processing match '{match}' for Football.")
    elif sport == "Swimming" and queue_swimming:
        match = queue_swimming.pop(0)
        print(f"Processing match '{match}' for Swimming.")
    else:
        print(f"No matches to process for {sport}.")


schedule_match("Basketball", "Team A vs Team B")
schedule_match("Football", "Team C vs Team D")
schedule_match("Swimming", "Team E vs Team F")

process_match("Basketball")
process_match("Football")
process_match("Swimming")

available_teams_basketball = []
available_teams_football = []
available_teams_swimming = []


def add_team(sport, team):
    if sport == "Basketball":
        available_teams_basketball.append(team)
        print(f"Team '{team}' added to available Basketball teams.")
    elif sport == "Football":
        available_teams_football.append(team)
        print(f"Team '{team}' added to available Football teams.")
    elif sport == "Swimming":
        available_teams_swimming.append(team)
        print(f"Team '{team}' added to available Swimming teams.")


def remove_team(sport, team):
    if sport == "Basketball" and team in available_teams_basketball:
        available_teams_basketball.remove(team)
        print(f"Team '{team}' removed from available Basketball teams.")
    elif sport == "Football" and team in available_teams_football:
        available_teams_football.remove(team)
        print(f"Team '{team}' removed from available Football teams.")
    elif sport == "Swimming" and team in available_teams_swimming:
        available_teams_swimming.remove(team)
        print(f"Team '{team}' removed from available Swimming teams.")
    else:
        print(f"Team '{team}' not found in {sport} teams.")


add_team("Basketball", "Team A")
add_team("Football", "Team B")
add_team("Swimming", "Team C")

remove_team("Basketball", "Team A")
remove_team("Football", "Team B")
remove_team("Swimming", "Team C")