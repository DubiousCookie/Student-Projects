R = 18
PG_13 = 13
PG = 6
G = 0
CUS_IN = int(input('"Hey! Welcome to the Movies? What age are you?" : ' ))
if CUS_IN >= R and CUS_IN < 101 :
    print('"Great! You can watch R rated movies! Dont see anything too violent!"')
if CUS_IN >= PG_13 and CUS_IN < R :
    print('"Nice! You can watch PG 13 movies! Dont eat too much sugar!"')
if CUS_IN >= PG  and CUS_IN < PG_13 :
    print('"Oh! Wanna see a Disney movie? Always stay with your parents!"')
if CUS_IN >= G and CUS_IN < PG :
    print('"Oh god who left this child alone!"')
if CUS_IN >= 101 or CUS_IN <=0 :
    print('"As if smart ass."')
