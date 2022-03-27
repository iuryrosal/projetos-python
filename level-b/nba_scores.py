from requests import get

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response["links"]

def get_currentScoreboard():
    response = get(BASE_URL+get_links()["currentScoreboard"]).json()
    games = response["games"]

    for game in games:
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        clock = game["clock"]
        period = game["period"]

        print("#########################################\n")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"SCORE: {home_team['score']} x {away_team['score']}")
        print(f"{clock} - {period['current']}\n")

def get_teams_stats():
    stats = get_links()["leagueTeamStatsLeaders"]
    data = get(BASE_URL+stats).json()
    teams = data["league"]["standard"]["regularSeason"]["teams"]

    teams = list(filter(lambda x: x["name"] != "Team", teams))
    teams.sort(key = lambda x: int(x["ppg"]["rank"]))

    for team in teams:
        team_name = team["name"]
        nickname = team["nickname"]
        ppg_avg = team["ppg"]["avg"]
        rank = team["ppg"]["rank"]
        print(f"RANK: {rank} | {team_name} - {nickname} | PPG Médio: {ppg_avg}")



while True:
    print("########################\n")
    print("SEJA BEM VINDO!!!! DADOS NBA IURYROSALTECH\n")
    print("1 - Ver Jogos\n")
    print("2 - Ver Times por PPG\n")
    user_choice = input("Opção: ")

    if user_choice == "1":
        get_currentScoreboard()
    elif user_choice == "2":
        get_teams_stats()
    else:
        continue