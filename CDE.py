##Current known bugs:
##    1. When the first profession preference is Weaver, Watchman or Stonemason, there is a chance that the second profession preference will be " ". Can be seen by printing array top3 as it runs.

##Current function/segments being worked on:
##    1. Initial job allocation based on job preferences of initial pop putlation and initial job ratios.
##          -function defined as Job_Sel0()

##Needed lists:
##    1. Farmer profession Products
##    2. Miner Profession Products
##    3. Forrester Profession Products
##    4. Mason Profession Products
##    5. Stonemason Profession Products
##    6. Hunter Profession Products
##    7. Blacksmith Profession Products
##    8. Weaver Profession Products
##    9. Cook Profession Products
##    10. Baker Profession Products
##    11. Butcher Profession Products
##    12. Carpenter Profession Products
##    13. Tanner Profession Products
##    14. Grocer Profession Products
##    15. Merchant Profession Products
##    16. Roofer Profession Products
##    17. Winemaker Profession Products
##    18. Locksmith Profession Products
##    19. Armourer Profession Products
##    20. Watchman Profession Products
##    21. Cobbler Profession Products
##    22. Wheelwright Profession Products
##    23. Belt Maker Profession Products
##    24. Tax Collector Profession Products

##Needed fuctions:
##    1. Farmer profession
##    2. Miner Profession
##    3. Forrester Profession
##    4. Mason Profession
##    5. Stonemason Profession
##    6. Hunter Profession
##    7. Blacksmith Profession
##    8. Weaver Profession
##    9. Cook Profession
##    10. Baker Profession
##    11. Butcher Profession
##    12. Carpenter Profession
##    13. Tanner Profession
##    14. Grocer Profession
##    15. Merchant Profession
##    16. Roofer Profession
##    17. Winemaker Profession
##    18. Locksmith Profession
##    19. Armourer Profession
##    20. Watchman Profession
##    21. Cobbler Profession
##    22. Wheelwright Profession
##    23. Belt Maker Profession
##    24. Tax Collector Profession
##    25. New citizen creation
##    26. working age job initalization
##    27. Top level individual citizen function?
##    28. 'perfect descision' calculator for previous few weeks/months
##    
import random
import numpy as np

            #List of jobs
J_ls = ["Farmer", "Miner", "Forrester", "Mason", "Stonemason", "Hunter", "Blacksmith", "Weaver" ,"Cook", "Baker", "Butcher", "Carpenter", "Tanner", "Grocer", "Merchant", "Roofer", "Winemaker", "Locksmith", "Armourer", "Watchman", "Cobbler", "Wheelwright", "Belt Maker", "Tax Collector"]

def rand_prof():                                        #Chooses a random profession from the full list of jobs. Needs reworking to pull from list
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

def prof_pref(A):                           #Determines the top 3 job preferences for a character based on the top 3 skills
    A[17] = A[17]+10;
    I = np.argsort(A)[::-1][:3];
    skl = ["","",""];
    pref_1 = "";
    pref_2 = "";
    pref_3 = "";
    for g in range(2):                              #Determines the top three skills' indices and allocates those indices into the array skl
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

    if skl[0] == "Strength":                                #If-else tree to decide first preference
        if skl[1] == "Precision":                           #Decides between Mason and Forrester based on the presense of Woodworking as the 3rd skill
            if skl[2] == "Woodworking":
                pref_1 = "Forrester";
            else:
                pref_1 = "Mason";
        else:
            desc = random.randrange(0, 1);                  #If strength is the first stat but precision is NOT the second skill, it randomly chooses between Miner and Roofer with a weight of 1:1
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
            desc = random.randrange(0, 2);                  #If Business is the first stat but Negotiation is NOT the second skill, it randomly chooses between Merchant and Grocer with a weight of 1:2
            if desc == 0:
                pref_1 = "Merchant";
            else:
                pref_1 = "Grocer";
    elif skl[0] == "Precision":                             #With precision as the first skill, there are 4 jobs it can be and the second skill determines which of the four it will be
        if skl[1] == "Strength":
            pref_1 = "Stonemason";
        elif skl[1] == "Creativity":
            pref_1 = "Weaver";
        elif skl[1] == "Navigation":
            pref_1 = "Watchman";
        elif skl[1] == "Smithing":
            pref_1 = "Locksmith";
        else:
            desc = random.randrange(0, 3);                  #If Precision is the first skill and the second skill is NOT Strength, Creativity, Navigation or Smithing, it randomly chooses between Stonemason, Weaver, Watchman and Locksmith
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
                desc = random.randrange(0, 5);              #If Smithing is the first skill and the second skill is Creativity but the third skill is NOT Business, it randomly chooses between Armourer and Blacksmith weighted 1:5
                if desc == 0:
                    pref_1 = "Blacksmtih";
                else:
                    pref_1 = "Armourer";
        elif skl[1] == "Strength":
            if skl[2] == "Business":
                pref_1 = "Blacksmith";
            else:
                desc = random.randrange(0, 5);              #If Smithing is the first skill and the second skill is Strength but the third skill is NOT Business, it randomly chooses between Armourer and Blacksmith weighted 1:5
                if desc == 0:
                    pref_1 = "Armourer";
                else:
                    pref_1 = "Blacksmith";
        else:
            pref_1 = "Blacksmtih";                          #If Smithing is the first skill but the second skill is NOT Creativity or Strength, it defaults to Blacksmith
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
            desc = random.randrange(0, 1);                  #If Leatherworking is the first skill and the second skill is NOT Precision or Woodworking, it randomly chooses between Belt Maker and Cobbler weighted 1:1
            if desc == 0:
                pref_1 = "Belt Maker";
            else:
                pref_1 = "Cobbler";
    elif skl[0] == "Woodworking":
        if skl[1] == "Precision":
            if skl[2] == "Creavity":
                pref_1 = "Carpenter";
            else:
                desc = random.randrange(0, 2);              #If Woodworking is the first skill and the second skill is Precision but the third skill is not Creativity, it randomly choose between Wheelwright and Carpenter weighted 1:2
                if desc == 0:
                    pref_1 = "Wheelwright";
                else:
                    pref_1 = "Carpenter";
        else:
            desc = random.randrange(0, 2);                  #If Woodworking is the first skill and the second skill is NOT Precision, it randomly choose between Wheelwright and Carpenter weighted 2:1
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
    
    if skl[1] == "Strength":                                #If-else tree to decide second preference
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
    
    if skl[2] == "Strength":                            #If-else tree to decide third preference
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
    
    if pref_3 == pref_1:                        #double checks for duplicates and uses rand_prof() if it finds one
        pref_3 = rand_prof();
    elif pref_2 == pref_3:
        pref_3 = rand_prof();

    T3 = [pref_1,pref_2,pref_3];
    return T3

def job_rat0(R,C):
    default = [28,10,18,5,1,8,2,2,5,3,2,2,1,3,1,1,1,1,1,1,1,1,1,1]          #Default ratio for all current jobs, will have to edit when new professions are added
    Rat = 0
    Jobs_0 = np.zeros((len(default),), dtype=int)             #Creates empty array of zeros that is the size of default
    if R == 0:
        R = default                                     #sets R to default to use default job ratios
        tot = 0
        for i in range(23):
            tot = tot + R[i]                            #tallys up ratio amounts
        for j in range(23):
            Rat = R[j]/tot                  #creates decimal that is the ratio of the number of that job to the overall population size
            n = C*Rat                       #Determines how many vacancies of a particular job there are
            Jobs_0[j] = round(n)            #rounds of the vacancy number to a whole number
            if Jobs_0[j] == 0:
                Jobs_0[j] = 1
        return Jobs_0
    else:
        return

def Job_Sel0(J_0,T_P,J_ls):
    Prof0 = np.zeros((len(T_P), dtype(str))          #initalizes an array of zeros that are strings
    for i in range(len(J_0)):                       #for loop that goes through every index value for J_0
        g = 0                                       #initializes counter for the slots of a given profession
        for j in  range(J_0[i]):                    #loop to fill slots for given profession
            if g == J_0[i]:                         #if the slots are filled, it forces the top loop to tick to the next value of i (not sure if required in python)
                i = i + 1
            else:                           
                for k in range(T_P):                #iterates through list of profession preferences to find a sutible villager to fill a slot
                    if T_P[k,0] == J_ls[i]:
                        if Prof0[k] == "0":         #check to see if that villager has already been given a job
                            Prof0[k] = J_ls[i]
                            g = g + 1               #increases the profession slot counter
                    else:
                        if T_P[k,1] == J_ls[i]:         #check for second job prefernce
                            if Prof0[k] == "0":
                                Prof0[k] = J_ls[i]
                                g = g + 1
                        else:
                            if T_P[k,2] == J_ls[i]:     #check for thrid job preference
                                if Prof0[k] == "0":
                                    Prof0[k] = J_ls[i]
                                    g = g + 1
                            else:
                                k = k + 1               #moves to next villager if the current villager didn't have that job as a preference
                    if k == len(T_P) && g != J_0[i]:
                        for h in range(T_P):
                            if Prof0[h] == "0":
                                Prof0[h] = J_ls[i]
                                g = g + 1
                            if g == J_0[i]:
                                i = i + 1
                                
    return Prof0

print("=======================================================================")
print("-------------------Character Driven Economy Sim v0.1-------------------\n")

print("Give ratios for jobs in this order, \n1.Farmer\n2.Miner\n3.Forrester\n4.Mason\n5.Stonemason\n6.Hunter\n7.Blacksmith\n8.Weaver\n9.Cook\n10.Baker\n11.Butcher\n12.Carpenter\n13.Tanner\n14.Grocer\n15.Merchant\n16.Roofer\n17.Winemaker\n18.Locksmith\n19.Armourer\n20.Watchman\n21.Cobbler\n22.Wheelwright\n23.Belt Maker\n24.Tax Collector")
print("\ninput '0' for a default ratio")
      
Rat_0 = input()
Rat_0 = int(Rat_0)

Cit_0 = input("Set initial number of villagers: ");                            ##Initial population
Cit_0 = int(Cit_0)

Jobs_0 = job_rat0(Rat_0,Cit_0)

#print(Jobs_0)

## Skills:
## 1.Strength
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
     top3 = prof_pref(Cit_s)
     #print(top3)
     for n in range(3):
         TOP_Pref[j][n+1] = top3[n];




