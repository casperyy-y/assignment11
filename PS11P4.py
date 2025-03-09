filename = "players.txt"
with open(filename, "w") as file:
    file.write("""Smith 0.267
Johnson 0.300
Williams 0.275
Brown 0.260
Jones 0.290
Miller 0.285
Davis 0.310
Garcia 0.245
Rodriguez 0.295
Wilson 0.280
""")

player_names = []
batting_averages = []

with open(filename, "r") as file:
    for line in file:
        data = line.strip().split()
        player_names.append(data[0])
        batting_averages.append(float(data[1]))

def display_players(names, averages):
    print("\nPlayer Names and Batting Averages:")
    for i in range(len(names)):
        print(f"{names[i]} - {averages[i]:.3f}")

display_players(player_names, batting_averages)

def search_player(names, averages):
    while True:
        search_name = input("\nEnter a player last name (or type 'exit' to quit): ").strip()
        if search_name.lower() == "exit":
            break
        if search_name in names:
            index = names.index(search_name)
            print(f"Player: {search_name}, Batting Average: {averages[index]:.3f}")
        else:
            print("Name not found.")

search_player(player_names, batting_averages)
