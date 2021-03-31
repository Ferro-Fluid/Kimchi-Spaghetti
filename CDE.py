import random
import numpy as np

def rand_prof():
    desc = random.randrange(1, 24);
    if desc == 1:
        pref = "Baker";
    elif desc == 2:
        pref = "Butcher";
    elif desc == 3:
        pref = "Stonemason";
    elif desc == 4:
        pref = "Weaver";
    elif desc == 5:
        pref = "Winemaker";
    elif desc == 6:
        pref = "Mason";
    elif desc == 7:
        pref = "Farmer";
    elif desc == 8:
        pref = "Watchman";
    elif desc == 9:
        pref = "Cobbler";
    elif desc == 10:
        pref = "Wheelwright";
    elif desc == 11:
        pref = "Roofer";
    elif desc == 12:
        pref = "Locksmith";
    elif desc == 13:
        pref = "Tanner";
    elif desc == 14:
        pref = "Tax Collector";
    elif desc == 15:
        pref = "Belt Maker";
    elif desc == 16:
        pref = "Grocer";
    elif desc == 17:
        pref = "Merchant";
    elif desc == 18:
        pref = "Armourer";
    elif desc == 19:
        pref = "Carpenter";
    elif desc == 20:
        pref = "Cook";
    elif desc == 21:
        pref = "Blacksmith";
    elif desc == 22:
        pref = "Forrester";
    elif desc == 23:
        pref = "Miner";
    else:
        pref = "Hunter";

    return pref

def prof_pref(A):
    A[17] = A[17]+10;
    I = np.argsort(A)[::-1][:3];
    skl = ["","",""];
    pref_1 = "";
    pref_2 = "";
    pref_3 = "";
    for g in range(2):
        if I[g] == 1:
            skl[g] = "Strength";
        elif I[g] == 2:
            skl[g] = "Business";
        elif I[g] == 3:
            skl[g] = "Precision";
        elif I[g] == 4:
            skl[g] = "Creavity";
        elif I[g] == 5:
            skl[g] = "Smithing";
        elif I[g] == 6:
            skl[g] = "Riding/Driving";
        elif I[g] == 7:
            skl[g] = "Direction/navigation";
        elif I[g] == 8:
            skl[g] = "Hunting";
        elif I[g] == 9:
            skl[g] = "Tanning";
        elif I[g] == 10:
            skl[g] = "Leather working";
        elif I[g] == 11:
            skl[g] = "Woodworking";
        elif I[g] == 12:
            skl[g] = "Cooking";
        elif I[g] == 13:
            skl[g] = "Negotiation";
        elif I[g] == 14:
            skl[g] = "Agriculture";
        elif I[g] == 15:
            skl[g] = "Desire for Quality";
        elif I[g] == 16:
            skl[g] = "Desire for family";
        elif I[g] == 17:
            skl[g] = "Challenge";
        elif I[g] == 18:
            skl[g] = "Likability";

    if skl[0] == "Strength":
        if skl[1] == "Precision":
            if skl[2] == "Woodworking":
                pref_1 = "Forrester";
            else:
                pref_1 = "Mason";
        else:
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_1 = "Miner";
            else:
                pref_1 = "Roofer";
    elif skl[0] == "Business":
        if skl[1] == "Negotiation":
            if skl (3) == "Likability":
                pref_1 = "Grocer";
            else: 
                pref_1 = "Merchant";
        else: 
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_1 = "Merchant";
            else:
                pref_1 = "Grocer";
    elif skl[0] == "Precision":
        if skl[1] == "Strength":
            pref_1 = "Stonemason";
        elif skl[1] == "Creativity":
            pref_1 = "Weaver";
        elif skl[1] == "Navigation":
            pref_1 = "Watchman";
        elif skl[1] == "Smithing":
            pref_1 = "Locksmith";
        else:
            desc = random.randrange(0, 3);
            if desc == 0:
                pref_1 = "Stonemason";
            elif desc == 1:
                pref_1 = "Weaver";
            elif desc == 2:
                pref_1 = "Watchman";
            else:
                pref_1 = "Locksmith";
    elif skl[0] == "Smithing":
        if skl[1] == "Creativity":
            if skl[2] == "Business":
                pref_1 = "Armourer";
            else:
                desc = random.randrange(0, 5);
                if desc == 0:
                    pref_1 = "Blacksmtih";
                else:
                    pref_1 = "Armourer";
        elif skl[1] == "Strength":
            if skl[2] == "Business":
                pref_1 = "Blacksmith";
            else:
                desc = random.randrange(0, 5);
                if desc == 0:
                    pref_1 = "Armourer";
                else:
                    pref_1 = "Blacksmith";
        else:
            pref_1 = "Blacksmtih";
    elif skl[0] == "Hunting":
        pref_1 = "Hunter";
    elif skl[0] == "Tanning":
        pref_1 = "Tanner";
    elif skl[0] == "Leatherworking":
        if skl[1] == "Precision":
            if skl[2] == "Woodworking":
                pref_1 = "Cobbler";
            else: 
                pref_1 = "Belt Maker";
        elif skl[1] == "Woodworking":
            pref_1 = "Cobbler";
        else:
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_1 = "Belt Maker";
            else:
                pref_1 = "Cobbler";
    elif skl[0] == "Woodworking":
        if skl[1] == "Precision":
            if skl[2] == "Creavity":
                pref_1 = "Carpenter";
            else:
                desc = random.randrange(0, 2);
                if desc == 0:
                    pref_1 = "Wheelwright";
                else:
                    pref_1 = "Carpenter";
        else:
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_1 = "Carpenter";
            else:
                pref_1 = "Wheelwright";
    elif skl[0] == "Cooking":
        if skl[1] == "Creativity":
            if skl[2] == "Business":
                pref_1 = "Cook";
            elif skl[2] == "Likability":
                pref_1 = "Baker";
            else:
                desc = random.randrange(0, 1);
                if desc == 0:
                    pref_1 = "Cook";
                else:
                    pref_1 = "Baker";
        elif skl[1] == "Business":
            if skl[2] == "Negotiation":
                pref_1 = "Butcher";
            elif skl[2] == "Creativity":
                pref_1 = "Cook";
            else:
                desc = random.randrange(0, 2);
                if desc == 0:
                    pref_1 = "Cook";
                else:
                    pref_1 = "Butcher";
        else:
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_1 = "Cook";
            else:
                pref_1 = "Baker";
    elif skl[0] == "Agriculture":
        if skl[1] == "Creativity":
            pref_1 = "Winemaker";
        elif skl[1] == "Strength":
            pref_1 = "Farmer";
        else:
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_1 = "Winemaker";
            else:
                pref_1 = "Farmer";
    elif skl[0] == "Likability":
        if skl[1] == "Navigation":
            pref_1 = "Tax Collector";
        else:
            desc = random.randrange(0, 5);
            if desc == 0:
                pref_1 = "Tax Collector";
            else:
                pref_1 = rand_prof();
    else:
        pref_1 = rand_prof()
    
    if skl[1] == "Strength":
        if skl[2] == "Precision":
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_2 = "Forrester";
                if pref_2 == pref_1:
                    pref_2 = "Mason";
            else:
                pref_2 = "Mason";
                if pref_2 == pref_1:
                    pref_2 = "Forrester";
        else:
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_2 = "Miner";
                if pref_2 == pref_1:
                    pref_2 = "Roofer";
            else:
                pref_2 = "Roofer";
                if pref_2 == pref_1:
                    pref_2 = "Miner";
    elif skl[1] == "Business":
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_2 = "Grocer";
                if pref_2 == pref_1:
                    pref_2 = "Merchant";
            else:
                pref_2 = "Merchant";
                if pref_2 == pref_1:
                    pref_2 = "Grocer";
    elif skl[1] == "Precision":
        if skl[2] == "Strength":
            pref_2 = "Stonemason";
        elif skl[2] == "Creativity":
            pref_2 = "Weaver";
        elif skl[2] == "Navigation":
            pref_2 = "Watchman";
        elif skl[2] == "Smithing":
            pref_2 = "Locksmith";
        else:
            desc = random.randrange(0, 3);
            if desc == 0:
                pref_1 = "Stonemason";
            elif desc == 1:
                pref_1 = "Weaver";
            elif desc == 2:
                pref_1 = "Watchman";
            else:
                pref_1 = "Locksmith";
    elif skl[1] == "Smithing":
        if skl[2] == "Creativity":
            desc = random.randrange(0, 5);
            if desc == 0:
                pref_2 = "Blacksmtih";
                if pref_2 == pref_1:
                    pref_2 = "Armourer";
            else:
                pref_2 = "Armourer";
                if pref_2 == pref_1:
                    pref_2 = "Blacksmith";
        elif skl[2] == "Strength":
            desc = random.randrange(0, 5);
            if desc == 0:
                pref_2 = "Blacksmith";
                if pref_2 == pref_1:
                    pref_2 = "Armourer";
            else:
                pref_2 = "Armourer";
                if pref_2 == pref_1:
                    pref_2 = "Blacksmith";
        else:
            desc = random.randrange(0, 5);
            if desc == 0:
                pref_2 = "Blacksmtih";
            else:
                pref_2 = rand_prof();
    elif skl[1] == "Hunting":
        pref_2 = "Hunter";
    elif skl[1] == "Tanning":
        pref_2 = "Tanner";
    elif skl[1] == "Leatherworking":
        if skl[2] == "Precision":
            pref_2 = "Cobbler";
        elif skl[2] == "Woodworking":
            pref_2 = "Cobbler";
        else:
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_2 = "Belt Maker";
                if pref_2 == pref_1:
                    pref_2 = "Cobbler";
            else:
                pref_2 = "Cobbler";
                if pref_2 == pref_1:
                    pref_2 = "Belt Maker";
    elif skl[1] == "Woodworking":
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_2 = "Carpenter";
                if pref_2 == pref_1:
                    pref_2 = "Wheelwright";
            else:
                pref_2 = "Wheelwright";
                if pref_2 == pref_1:
                    pref_2 = "Carpenter";
    elif skl[1] == "Cooking":
        if skl[2] == "Creativity":
            desc = random.randrange(0, 1);
            if desc == 0:
                pref_2 = "Cook";
                if pref_2 == pref_1:
                    pref_2 = "Baker";
            else:
                pref_2 = "Baker";
                if pref_2 == pref_1:
                    pref_2 = "Cook";
        elif skl[2] == "Business":
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_2 = "Cook";
                if pref_2 == pref_1:
                    pref_2 = "Butcher";
            else:
                pref_2 = "Butcher";
                if pref_2 == pref_1:
                    pref_2 = "Cook";
        else:
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_2 = "Cook";
                if pref_2 == pref_1:
                    pref_2 = "Baker";
            else:
                pref_2 = "Baker";
                if pref_2 == pref_1:
                    pref_2 = "Cook";
    elif skl[1] == "Agriculture":
        if skl[2] == "Creativity":
            pref_2 = "Winemaker";
        elif skl[2] == "Strength":
            pref_2 = "Farmer";
        else:
            desc = random.randrange(0, 2);
            if desc == 0:
                pref_2 = "Winemaker";
                if pref_2 == pref_1:
                    pref_2 = "Farmer";
            else:
                pref_2 = "Farmer";
                if pref_2 == pref_1:
                    pref_2 = "Winemaker";
    elif skl[1] == "Likability":
        if skl[2] == "Navigation":
            pref_2 = "Tax Collector";
        else:
            desc = random.randrange(0, 5);
            if desc == 0:
                pref_2 = "Tax Collector";
            else:
                pref_2 = rand_prof();
    else:
        pref_2 = rand_prof()
    
    if skl[2] == "Strength":
        desc = random.randrange(0, 3);
        if desc == 0:
            pref_3 = "Forrester";
        elif desc == 1:
            pref_3 = "Mason";
        elif desc == 2:
            pref_3 = "Miner";
        else:
            pref_3 = "Roofer";
    elif skl[2] == "Business":
        desc = random.randrange(0, 1);
        if desc == 0:
            pref_3 = "Grocer";
        else:
            pref_3 = "Merchant";
    elif skl[2] == "Precision":
        desc = random.randrange(0, 3);
        if desc == 0:
            pref_3 = "Stonemason";
        elif desc == 1:
            pref_3 = "Weaver";
        elif desc == 2:
            pref_3 = "Watchman";
        else:
            pref_3 = "Locksmith";
    elif skl[2] == "Smithing":
        desc = random.randrange(0, 5);
        if desc == 0:
            pref_3 = "Armourer";
        else:
            pref_3 = "Blacksmith";
    elif skl[2] == "Hunting":
        pref_3 = "Hunter";
    elif skl[2] == "Tanning":
        pref_3 = "Tanner";
    elif skl[2] == "Leatherworking":
        desc = random.randrange(0, 1);
        if desc == 0:
            pref_3 = "Belt Maker";
        else:
            pref_3 = "Cobbler";
    elif skl[2] == "Woodworking":
        desc = random.randrange(0, 2);
        if desc == 0:
            pref_3 = "Carpenter";
        else:
            pref_3 = "Wheelwright";
    elif skl[2] == "Cooking":
        desc = random.randrange(0, 2);
        if desc == 0:
            pref_3 = "Cook";
        elif desc == 1:
            pref_3 = "Baker";
        else:
            pref_3 = "Butcher";
    elif skl[2] == "Agriculture":
        desc = random.randrange(0, 3);
        if desc == 0:
            pref_3 = "Winemaker";
        else:
            pref_3 = "Farmer";
    elif skl[2] == "Likability":
        pref_3 = "Tax Collector";
    else:
        pref_3 = rand_prof()
    
    if pref_3 == pref_1:
        pref_3 = rand_prof();
    elif pref_2 == pref_3:
        pref_3 = rand_prof();

    T3 = [pref_1,pref_2,pref_3];
    return T3

Cit_0 = input("Set initial number of villagers: ");                            ##Initial population

Cit_0 = int(Cit_0)

## Skills:
## 1.##ength
## 2.Business
## 3.Precision
## 4.Creativity
## 5.Smithing
## 6.Riding/Driving
## 7.Direction/navigation
## 8.Hunting
## 9.Tanning
## 10.Leatherworking
## 11.Woodworking
## 12.Cooking
## 13.Negotiation
## 14.Agrigculture

## Peronality traits/skills:
## 15.Desire for Luxury/quality
## 16.Desire for family
## 17.Challenge
## 18.Likeability

Num_skl = 14;
Num_pers = 4;
size = Num_skl+Num_pers;

Skills = [0]*size;

POP = np.zeros((Cit_0, Num_skl+Num_pers+1));                        ##Population Array 
i = 0

for i in range(Cit_0):                                                ##Generates skill levels for each citizen
    POP[i,0] = i;
    for j in range(Num_skl+Num_pers):
        Skills[j] = random.randrange(1, 20);                          ##Default range for skills is 1 to 20
        if j == 14:
            Skills[j] = random.randrange(0, 5);                       ##Range for quality is 0 to 5
            POP[i,j+1] = Skills[j];
        elif j == 15:
            Skills[j] = random.randrange(1, 10);                      ##Range for Family is 1 to 10
            POP[i,j+1] = Skills[j];
        elif j == 16:
            Skills[j] = Skills[j] - 10;                         ##Range for challenge is -10 to 10
            POP[i,j+1] = Skills[j];
        else:
            POP[i,j+1] = Skills[j];

TOP_Pref = [[""]*4 for i in range(Cit_0)]     

for j in range(Cit_0):
     Cit_s = POP[j,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]];
     top3 = prof_pref(Cit_s);
     print(top3)
     for n in range(3):
         TOP_Pref[j][n+1] = top3[n];

print(TOP_Pref)



