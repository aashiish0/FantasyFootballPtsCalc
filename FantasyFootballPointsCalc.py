
scoring_format = input("What scoring format would you like to use: ")

if scoring_format.upper() == "PPR":
    position = input("Which position would you like calculate the points for (QB, RB, WR, TE, D/ST, K): ")
    if position.upper() == "QB":
        passing_yards = int(input("Passing yards: "))
        passing_touchdowns = int(input("Passing touchdowns: "))
        rushing_yards = int(input("Rushing Yards: "))
        rushing_touchdowns = int(input("Rushing touchdowns: "))
        turnovers = int(input("Interception/Fumbles: "))
        
        QB_points = (float(passing_yards / 25) + float(passing_touchdowns * 4) + float(rushing_yards / 10) + float(rushing_touchdowns * 6) - float(turnovers * 2))
        print("Fantasy points: ", round(QB_points, 2))
    
    elif position.upper() == "RB" or position.upper() == "TE" or position.upper() == "WR":
        rushing_yards = int(input("Rushing Yards:"))
        recieving_yards = int(input("Recieving Yards: "))
        receptions = int(input("Receptions: "))
        touchdowns = int(input("Touchdowns: "))
        fumbles_lost = int(input("Fumbles Lost: "))

        points_recievers = (float(rushing_yards / 10) + float(recieving_yards / 10) + float(receptions * 1) + float(touchdowns * 6) - float(fumbles_lost * 2))
        print("Fantasy points: ", round(points_recievers, 2))
        
    elif position.upper() == "K":
        extra_points = int(input("PATs: "))
        under_forty = int(input("Field goals (19-39): "))
        under_fifty = int(input("Field goals (40-49): "))
        under_sixty = int(input("Field goals (50-59): "))
        above_sixty = int(input("Field goals (60+): "))
        missed_FG = int(input("Missed field goals: "))

        points_kicker = ((extra_points * 1) + (under_forty * 3) + (under_fifty * 4) * (under_sixty * 5) + (under_sixty * 6) - (missed_FG * 1))
        print("Fantasy points: ", points_kicker)

    elif position.upper() == "D/ST" or position.upper() == "D":
        interceptions = int(input("Interceptions: "))
        fumbles_recovered = int(input("Fumbles Recovered: "))
        touchdowns = int(input("KR/Defensive TDs: "))
        sacks = int(input("Sacks: "))
        blocks = int(input("Blocked Punt, PAT, or FG: "))
        safety = int(input("Safety: "))
        points_allowed = int(input("Points Allowed: "))  
        yards_allowed = int(input("Yards Allowed: "))



def calculatePointsAllowed(points_allowed):
            if points_allowed == 0:
                points = 5
            elif points_allowed >= 1 and points_allowed <= 6:
                points = 4
            elif points_allowed >= 7 and points_allowed <= 13:
                points = 3
            elif points_allowed >= 14 and points_allowed <= 17:
                points = 1
            elif points_allowed >= 18 and points_allowed <= 27:
                points = 0
            elif points_allowed >= 28 and points_allowed <= 34:
                points = -1
            elif points_allowed >= 35 and points_allowed <= 45:
                points = -3
            elif points_allowed >= 46:
                points = -5
            return points

def calculateYardsAllowed(yards_allowed):
            if yards_allowed < 100:
                yards = 5
            elif yards_allowed >= 100 and yards_allowed < 199:
                yards = 3
            elif yards_allowed >= 200 and yards_allowed < 299:
                yards = 2
            elif yards_allowed >= 300 and yards_allowed < 349:
                yards = 0
            elif yards_allowed >= 350 and yards_allowed < 399:
                yards = -1
            elif yards_allowed >= 400 and yards_allowed < 449:
                yards = -3
            elif yards_allowed >= 450 and yards_allowed < 499:
                yards = -5
            elif yards_allowed >= 500 and yards_allowed < 549:
                yards = -6
            elif yards_allowed >= 550:
                yards = -7
            return yards


dst_points = ((interceptions*2) + (fumbles_recovered*2) + (touchdowns * 6) + sacks + (blocks*2) + (safety*2) + calculatePointsAllowed(points_allowed) + calculateYardsAllowed(yards_allowed))
print("Fantasy Points: ", dst_points)
                


        


