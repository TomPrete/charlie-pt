import csv

# ---- Read CSV Data -> rows as a list
# with open('nfl_teams.csv') as nfl_teams_file:
#     csv_reader = csv.reader(nfl_teams_file) # returns csv row in a list
#     for row in csv_reader:
#         print(row)
#         # if row[1] == 'Bangals':
#         #     print(f"---- {row[1]} -----")
#         #     print("WIN RECORD: ", row[2])
#         #     print("LOSS RECORD: ", row[3])


# ---- Read CSV Data -> as a dict (dictionary)
with open('nfl_teams.csv') as nfl_teams_file:
    csv_reader = csv.DictReader(nfl_teams_file)
    for row in csv_reader:
        print(f"---- {int(row['id'])}: {row['team']} ----")
        print("WIN RECORD: ", type(int(row['wins'])))
        print("LOSS RECORD: ", int(row['losses']))

# ---- Writing to CSV File - mode "W" overwrites all data in csv file
# with open('nfl_teams.csv', mode='a') as nfl_teams_file:
#     nfl_writer = csv.writer(nfl_teams_file)
#     nfl_writer.writerow([5, ' Titans', 12,5])
#     nfl_writer.writerow([6,'Colts', 9,8])
#     nfl_writer.writerow([7,'Chiefs', 12,5])

# with open('nfl_teams.csv', mode='a') as nfl_teams_file:
#     headers = ['id', 'team', 'wins', 'losses']
#     nfl_writer = csv.DictWriter(nfl_teams_file, fieldnames=headers)
#     nfl_writer.writerow({
#         'id': 8,
#         'team': 'Raiders',
#         'wins': 10,
#         'losses': 7
#     })
#     nfl_writer.writerow({
#         'id': 9,
#         'team': 'Packers',
#         'wins': 13,
#         'losses': 4
#     })
#     nfl_writer.writerow({
#         'id': 10,
#         'team': 'Buccaneers',
#         'wins': 13,
#         'losses': 4
#     })

