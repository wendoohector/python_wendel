t_care = 25


pos_x = t_care // 2  
pos_y = 1  
vers_le_bas = True  
while True:
    for i in range(t_care):
        if i == 0 or i == t_care - 1:
            print("-" * t_care)
        else:
            ligne = "|" + " " * (t_care - 2) + "|"
            if pos_y == i:
                ligne = ligne[:pos_x] + "O" + ligne[pos_x + 1:]
            print(ligne)
    
    
    if vers_le_bas:
        pos_y += 1
    else:
        pos_y -= 1


    if pos_y == t_care - 1:
        vers_le_bas = False
    elif pos_y == 1:
        vers_le_bas = True

    
    print("\033[H\033[J")
