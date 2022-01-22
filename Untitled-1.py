import string


introduction = "Hello, welcome to the adventure survival game. During the game you will make several desicions and answer questions which will determine the outcome of your advenuture"
instruction = "You will now get to decide what youre character will be, please enter youre gender: male or female"
print(introduction + instruction)
gender = input().lower()

if gender == "male":
    print("You have picked male")
else:
    print("You have picked female")
print("You are stranded on an island. There are 4 biomes to choose from and whichever biome you choose will affect your game so choose wisely.\n Youre choices are: Jungle, Desert, Grass land, Coast line")
biome_choice = input().lower()

if biome_choice == "jungle":
    print("You have picked the jungle biome. This biome has a lot of biodervisity but is very humid.")
    print("You look around your surroundings and see that you are completely surrounded by thick vegetation.")
    print("You have 2 options. You could find food and water or you could try find a shelter for the night.\n Please pick youre option: Shelter or Food")
    food_or_shelter_jungle = input().lower()

    if food_or_shelter_jungle == "shelter":
        print("You have picked shelter")
        print("You start making your way through the thick vegitation and then you see a great mountain in youre way. You could go around the Mountain and carry on looking for shelter or you could go ontop and try find a way out. Please pick youre option: \n Way out or shelter")
        shelter_or_way_out = input().lower()

        if shelter_or_way_out == "way out":
            print("You have decided to go up the mountain to try find a way out")
        else:
            print("You have decided to carry on youre objective to find shelter")
    else:
        print("You have picked to find food and water")
        print("You make youre way through the vegitation and then see in the distance a great waterfall....But there are tigers in the way. You could try sneek past the tigers or go around them. Please pick your option: \n Sneek or Go around")
        sneek_or_go_around_jungle = input().lower()

        if sneek_or_go_around_jungle == "sneek":
            print("You have decided to try sneek around the tigers")
        else:
            print("You decided to go around the tigers")    
    

if biome_choice == "desert":
    print("You have picked the Desert biome. This biome is a challenge to survive in and has little food and water ")
    print("You look around your surroundings to see that you are surrounded by endless desert with no water or food in site")
    print("You see that there are a few dead trees around. Do you try make shelter from the dead trees or go on a journey to try find food and water. Please pick your option: \n Shelter or Food and water")
    shelter_or_food_and_water_desert = input().lower()

    if shelter_or_food_and_water_desert == "food and water":
        print("You have decided to try go on a journey to find food and water")
        print("You start walking, not knwoing where to go but after several hours of walking you see a shimmering oasis.... But there are wild Oryx drinking from it already. You have two options you could either go to the oasis and hope they dont attack you or wait until they are done which could be hours. Please pick your option: \n Go to the Oasis or wait")
        oasis_or_wait_desert = input().lower()
        
        if "oasis" in oasis_or_wait_desert:
            print("You have decided to go to the oasis and risk being attacked to get water")
            print("You could either try sneak up to the Oasis or run over to it because of dehydration. Please pick your option:\n Sneak up or Run")
            sneak_up_or_run = input().lower()

            if sneak_up_or_run == "sneak up":
                print ("You have chosen to sneak up to the Oasis so The wil Oryx don't realise you're there")
            else:
                print("You have decided to run to the oasis because you are dehydrating ")    
        else:
            print("You have decided to wait until the wild Oryx go so you don't risk getting attacked")
            print("You was waitin for hours but they have now left so you run to the oasis and start quickly drinking the water.")    

    else:
        print("You have decided to make a shelter from the dead trees")
        print("You start gathering branches from the trees until you have enough to build a shelter with")
        print("You dont know what to do because there isnt anything to attach the wood together")
        print("You could use your t-shirt to tie it together but then you wouldnt have protection from the sun and sandstorms.Please pick your option:\n Protection from sun or tie your wood together")
        protection_from_sun_or_tie_wood = input().lower()
        
        if "protection" in protection_from_sun_or_tie_wood:
            print("You have chosen to keep your t-shirt and keep rotected from the sun but that mean u have to abanddon your shelter")
        else:
            print("You have chosen to use your t shirt to tie the Wood together for a shelter")

if biome_choice == "Grass land":
    print("You have picked the grass land biome. This is an average biome and has food and little fluctation in weather")
    print("You look around your surrondings and see thick grass, trees and hills surrounding you")
    print("You start thinking about what to do first. You have come to 2 options you could go look for some food and water or you could try find a good shelter for the night. Please pick your option:\n Find food and water or find shelter for the night")
    find_water_or_shelter = input().lower()
   
    if "water" in find_water_or_shelter or "food" in find_water_or_shelter == "food and water":
        print("You have chosen to find food and water")
    else:
        print("You have chosen to find shelter for the night")
    

#if biome_choice == "Coast line":
    #print ("You have picked the coast line biome. This biome has ood food and water but you are at risk of storms") 


