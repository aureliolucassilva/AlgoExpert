def tournamentWinner(competitions, results):
    lastIdx = len(competitions)
    points = {}

    for idx in range(lastIdx):
        homeTeam = competitions[idx][0]
        awayTeam = competitions[idx][1]
        if results[idx] == 1:
            if homeTeam in points:
                points[homeTeam] += 3
            else:
                points[homeTeam] = 3
        else:
            if awayTeam in points:
                points[awayTeam] += 3
            else:
                points[awayTeam] = 3

    winner = max(points, key=points.get)
    return winner


