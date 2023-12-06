with open('Input', 'r') as file:
    calibration = file.read()

#krotka gdzie S = ((czerwone, zielone, niebieskie); itd)
Game_1 = ([1, 3, 5], [1, 4, 0], [3, 2, 5])
PossibleGames = (3, 5, 4)
max_list = []
counter = 0
result = 0

for k in range(3):             #najwieksze mozliwosci w pojednyczej grze
    max_number = max(Game_1[0][k], Game_1[1][k], Game_1[2][k])
    max_list.append(max_number)

for i in range(3):
    if max_list[i] < PossibleGames[i]:
        counter += 1

if counter == 3:
    result += 1         #sumuje gry ktore moga sie odbyc

print(result)