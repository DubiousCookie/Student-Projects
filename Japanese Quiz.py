#I want to make a quick quiz to help with my japanese studies
#1rst, I will make a humorous intro
上手 = 0
GAKSEI_IN= input('"Hello, do you wish to take a quick quiz on Japanese?" : ' )
if GAKSEI_IN == "Yes":
    print('"Great!"')
    while 上手 <= 6 :
        HEAR_IN = input('"もう いちど いって ください。What does this mean?" : ')
        if HEAR_IN == "Please say it again.":
                print ('"日本語 が 上手!"')
                print('"次の問題!/Next Question!"')
                上手 = 上手 +1
        SLOW_IN = input('"もう すこし ゆっくり おねがいします。 What does this mean?" : ')
        if SLOW_IN == 'More slowly please.':
            print ('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        READ_IN = input('"よんで ください。 What does this mean?" : ')
        if READ_IN == "Please read.":
                print ('"日本語 が 上手!"')
                print('"次の問題!/Next Question!"')
                上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        NIH_IN = input('"それは にほんごで なんと いいますか。 What does this mean?" : ')
        if NIH_IN == "How do you say that in Japanese?":
            print('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        LIS_IN = input('"きいて ください。 What does this mean?" : ')
        if LIS_IN == 'Please listen.':
            print('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0


else:
    print('"Too bad!"')
    while 上手 <=6:
        HEAR_IN = input('"もう いちど いって ください。What does this mean?" : ')
        if HEAR_IN == "Please say it again.":
                print ('"日本語 が 上手!"')
                print('"次の問題!/Next Question!"')
                上手 = 上手 +1
        SLOW_IN = input('"もう すこし ゆっくり おねがいします。 What does this mean?" : ')
        if SLOW_IN == 'More slowly please.':
            print ('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        READ_IN = input('"よんで ください。 What does this mean?" : ')
        if READ_IN == "Please read.":
                print ('"日本語 が 上手!"')
                print('"次の問題!/Next Question!"')
                上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        NIH_IN = input('"それは にほんごで なんと いいますか。 What does this mean?" : ')
        if NIH_IN == "How do you say that in Japanese?":
            print('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
        LIS_IN = input('"きいて ください。 What does this mean?" : ')
        if LIS_IN == 'Please listen.':
            print('"日本語 が 上手!"')
            print('"次の問題!/Next Question!"')
            上手 = 上手 +1
        else: print('"もう一度試してください!/Try again!"')
        上手 = 0
