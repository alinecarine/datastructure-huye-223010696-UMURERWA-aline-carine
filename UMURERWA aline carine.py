#  Stacks for team registrations
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

# Queues for match scheduling
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

# Example usage
push_team("Basketball", "Lakers")
push_team("Football", "Patriots")
push_team("Swimming", "Sharks")

pop_team("Basketball")
pop_team("Football")
pop_team("Swimming")

schedule_match("Basketball", "Lakers vs Bulls")
schedule_match("Football", "Patriots vs Giants")
schedule_match("Swimming", "Sharks vs Dolphins")

process_match("Basketball")
process_match("Football")
process_match("Swimming")
