def repeat():

introduction ="Hello, welcome to the adventure survival game. During the game you will make several desicions and answer questions which will determine the outcome of your advenuture"
instruction = "You will now get to decide what youre character will be, please enter youre gender: male or female"

print(introduction)
input("Press Enter to continue")
print(instruction)
gender = input().lower()                                                                                     

if "male" in gender:
    print("You have picked male")
else:
    print("You have picked female")
print("You are stranded on an island. There are 4 biomes to choose from and whichever biome you choose will affect your game so choose wisely.\n Youre choices are: \n Jungle 3/5 difficulty \n Desert 5/5 difficulty \n Grass land 1/5 difficulty \n Coast line 2/5 difficulty")
biome_choice = input().lower()

if "jungle" in biome_choice:
    print("You have picked the jungle biome. This biome has a lot of biodervisity but is very humid.")
    print("You look around your surroundings and see that you are completely surrounded by thick vegetation.")
    print("You have 2 options. You could find food and water or you could try find a shelter for the night.\n Please pick youre option: Shelter or Food")
    food_or_shelter_jungle = input().lower()

    if "shelter" in food_or_shelter_jungle:
        print("You have picked shelter")
        print("You start making your way through the thick vegitation and then you see a great mountain in youre way. You could go around the Mountain and carry on looking for shelter or you could go ontop and try find a way out. Please pick youre option: \n Way out or shelter")
        shelter_or_way_out = input().lower()

        if "way out" in shelter_or_way_out:
            print("You have decided to go up the mountain to try find a way out")
            print("You make the trek up the mountain and then see endless jungle but see a nice patch of open land about 1km away.Please pick your option:\n walk or try find shelter")
            walk_or_shelter = input().lower()
            
            if "walk" in walk_or_shelter:
                print("You have decided to walk over to the patch of land so you start your walk")
                print("After an hou you made your way to the open patch of land and find out that it is perfect to setup a place to live")
                print("You have many natural resources around you so you start gathering up trees and vines and make a quick simple structure to cover yourself from rain")
                print("It becomes night and you didnt geg hit by the rain but your legs had mosquito bites on them and figured out that you would have to find a way to not get bitten")
                print("You see some bugs on the floor, they are nutritious but could have bacteria on them. Do you eat them or not Yes or No?")       
                yes_or_no_jungle_worms = input().lower()
                
                if "yes" in yes_or_no_jungle_worms:
                    print("You have decided to eat the jungle worms")
                    print("The worms tasted horrible and chewy but gave you enough energy for the day but you need water before the end of the day")
                    print("It starts raining. You can either collect the rain water or try find a fresh water source which could be miles.")
                    print("Please pick your option:Collect water or find Water source")
                    collect_rain_water_or_find_water_source = input().lower()
                    
                    if "rain" in collect_rain_water_or_find_water_source:
                        print("You have decided to collect the rain water")
                    else:
                        print("You have decided to try find a water source")
        else:
            print("You have decided to carry on youre objective to find shelter")
            print("You find an overhang where you would be protected from the rain.")
            print("it becomes night and you get a good sleep but your back was aching from sleeping on stone")
                
            
    else:
        print("You have picked to find food and water")
        print("You make youre way through the vegitation and then see in the distance a great waterfall....But there are tigers in the way. You could try sneek past the tigers or go around them. Please pick your option: \n Sneek or Go around")
        sneek_or_go_around_jungle = input().lower()

        if "sneek" in sneek_or_go_around_jungle:
            print("You have decided to try sneek around the tigers")
            print("You get close to the waterful. But the tigers were hungryand needed some food to live")
            print("They quickly jump at you pinning you to the ground and start eating your body eventually killing you. Unfortunatly you have died due to your desicions")
            check = input("To restart enter Y or if you want to exit any other key")
            if check == "Y": #loops back
              repeat() print("Bye...")
            else: quit() 
            
            
            
        else:
            print("You decided to go around the tigers")
            print("it took awhile to cut through the vegitation but after awhile you manage to get to the water source and hydrate again")
            print("You are also very dirty but there could be dangerous animals in the water. Should you jump in and wash up. Yes or No")
            wash_up_or_not_jungle = input().lower()
            
            if "yes" in wash_up_or_not_jungle:
                print("There was viscious piranhas in the pool. You tried to escape but there was too many of them. You ended up dying because of your choices.") 
                quit()
   

if "desert" in biome_choice:
    print("You have picked the Desert biome. This biome is a challenge to survive in and has little food and water ")
    print("You look around your surroundings to see that you are surrounded by endless desert with no water or food in site")
    print("You see that there are a few dead trees around. Do you try make shelter from the dead trees or go on a journey to try find food and water. Please pick your option: \n Shelter or Food and water")
    shelter_or_food_and_water_desert = input().lower()

    if "food" in shelter_or_food_and_water_desert or "Water" in shelter_or_food_and_water_desert:
        print("You have decided to try go on a journey to find food and water")
        print("You start walking, not knwoing where to go but after several hours of walking you see a shimmering oasis.... But there are wild Oryx drinking from it already. You have two options you could either go to the oasis and hope they dont attack you or wait until they are done which could be hours. Please pick your option: \n Go to the Oasis or wait")
        oasis_or_wait_desert = input().lower()
        
        if "oasis" in oasis_or_wait_desert:
            print("You have decided to go to the oasis and risk being attacked to get water")
            print("You could either try sneak up to the Oasis or run over to it because of dehydration. Please pick your option:\n Sneak up or Run")
            sneak_up_or_run = input().lower()

            if "sneak" in sneak_up_or_run:
                print ("You have chosen to sneak up to the Oasis so The wil Oryx don't realise you're there")
                print("They don't see you and you manage to sneak up and get a drink")
                print("There are some bananas on a tree but they are very high up. Do you risk going up and hurting yourself or try find another food source. Please pick your option:\n Climb  up or find other food")
                climb_up_or_find_another_food_source = input().lower()
                
                if "climb" in climb_up_or_find_another_food_source:
                    print("You have chosen to climb up the tree, you start climbing and then suddenly you loose grip about 10 meters above the ground do you let go. Yes or No?")
                    do_you_let_go_of_banana_tree_or_not = input().lower()
                    
                    if "yes" in do_you_let_go_of_banana_tree_or_not:
                        print("You let go of the tree and fell onto the floor. It was a big drop and you sprained your ankle and didn't even get the food")
                    
                    else:
                        print("You manage to gain your drip and now you are climbing up more careful")
                        print("Eventually you get to the top of the banana tree and get 5 bananas which filled you up.")
                        print("You also see a banana leaves do you risk taking some and falling down or climb down safetly. Do you get the Banana leaves. Yes or No")
                        get_banana_leaves_or_not = input().lower()
                    
                        if "yes" in get_banana_leaves_or_not:
                            print("Your sprained ankle was healed for the next morning to start building your shelter")
                        else:
                            print("You managed to get down the tree safetly but it was starting to turn dark...")
                            print("You had to sleep on the floor and you got to sleep well but in the middle of the night a scorpian came from the ground and injected its venom in you so you never woke up...GAME OVER")
                            quit()
                            
                else:
                    print("You look around and see a stone and start trying to throw it up and hit a banana. After a while you manage to get one banana but still hungry and now it is becoming night")
                    print("You go to sleep next to the oasis under a tree but a scorpian comes when your sleeping and injects you with it venom so you never wake up...\n GAME OVER")
                    quit()
                      
                           
                      
            else:
                print("You have decided to run to the oasis because you are dehydrating ") 
                print("The wild Oryx see you and suddenly got scared and run straight at you. They knocked you out and you layed on the floor and eventually died of heat.\n GAME OVER ")
                quit()
        else:
            print("You have decided to wait until the wild Oryx go so you don't risk getting attacked")
            print("You was waiting for hours but they have now left so you run to the oasis and start quickly drinking the water.")
            print("You get some nearby leaves and put them on the floor so you dont die.")
            print("You get a good night sleep but are very hungry so the next day you need to find food so you dont die from starvation")

    else:
        print("You have decided to make a shelter from the dead trees")
        print("You start gathering branches from the trees until you have enough to build a shelter with")
        print("You dont know what to do because there isnt anything to attach the wood together")
        print("You could use your t-shirt to tie it together but then you wouldnt have protection from the sun and sandstorms.Please pick your option:\n Protection from sun or tie your wood together")
        protection_from_sun_or_tie_wood = input().lower()
        
        if "protection" in protection_from_sun_or_tie_wood:
            print("You have chosen to keep your t-shirt and keep rotected from the sun but that mean u have to abanddon your shelter")
            print("you dont have water or food and no shelter eventually you collapse of dehydration and too much heat.\n GAME OVER ")          
        else:
            print("You have chosen to use your t shirt to tie the Wood together for a shelter")
            print("Although you had shelter you havent had food or water ina desert for 24 hours so you pass away in your sleep that night. GAME OVER")

if "grass" in biome_choice:
    print("You have picked the grass land biome. This is an average biome and has food and little fluctation in weather")
    print("You look around your surrondings and see thick grass, trees and hills surrounding you")
    print("You start thinking about what to do first. You have come to 2 options you could go look for some food and water or you could try find a good shelter for the night. Please pick your option:\n Find food and water or find shelter for the night")
    find_water_or_shelter = input().lower()
   
    if "water" in find_water_or_shelter or "food" in find_water_or_shelter:
        print("You have chosen to find food and water")
        print("You start walking through the grass and see some berries on a tree which would be good nutrition for you. You have two options you could either eat the beries and risk getting ill or try find another food source. Please pick your option:\n Eat them or find other food")
        eat_berries_or_eat_other_food = input().lower()
        
        if "berries" in eat_berries_or_eat_other_food:
            print("You have choosen to eat the mystery berries")
            print("You felt fine at first but the next morning your body is aking so you cannot travel as fast anymore")
            
        else:
            print("You have chosen to try find another food supply")
        
        
    else:
        print("You have chosen to find shelter for the night")
    

if "coast" in biome_choice:
    print("You have picked the coast line biome. This biome has ood food and water but you are at risk of storms") 
    print("You look around there are clips and rocks around you and you feel the sof touch of sand beneath your feet")
    print("You suddenly tralise that you have no food, water or shelter")
    print("You have gwo options you could either try find a shelter or food and water. Please pick your option now:\n Food and water or shelter")
    food_and_water_or_shelter_seaside = input().lower()
    
    if "food" in food_and_water_or_shelter_seaside or "water" in food_and_water_or_shelter_seaside:
        print("You have chosen to try find food and water ")
        print("You start looking for food and come to the desicion that the best way to get food is to catch fish but theres two different options. Please pick your option:\n Use hands or Make weapon")
        weapon_or_hands = input().lower()
       
        if "weapon" in weapon_or_hands:
            print("You have chosen to try make a weapon to try catch some fish")
            print("You find a sharp stone and a sharp stick. You could use either of these items to catch the fish.Please pick your option:\n Stone or Wood")
            stone_or_wood = input().lower()
            
            if "stone" in stone_or_wood:
                print("You have chosen to use the sharp stone to try catch fish which is heavier to carry but more dangerous then the stick")
                print("You used the stone but couldn't move quickly so you only caught a few fish")
                print("You had to sleep on the sand but got a reasonable seat as you had a bit of food")
            else:
                print("You have chosen to use the sharp wood which is lighter then the stone but not as dangerous")
                print("You managed to catch lots of fishas you could move quickly through the water and catch the fish")
                print("You had to sleep on the sand but got a good sleep as you caught a lot of fish")
        else:
            print("You have chosen to try use your hands to catch the fish")
            print("You ran into the sea. There was several fish but they were to quick for you so you gave up when it came dark.")
            print("You ended up having to sleep on the sand and didnt get a good sleep")
    else:
        print("You have chosen to try find shelter")
        print("Where will you start looking for shelter. There is the remains of an old boat or theres a cave. Pick your option now:\n Boat or Cave")
        boat_or_cave = input().lower()
        
        if "boat" in boat_or_cave:
            print("You have chosen to go look for shelter at the abandoned boat")
            print("You walk over to the Abandoned boat and go outside. Its nicely shaded and has good protection from the wind")
            print("It turns into night and you get a good sleep and are ready for the day ahead")
        else:
            print("You have decided to look for shelter in the cave")
            print("You go into the cave and everything seems great. Its nicely protected from the wind and cool.")
            print("Day turns into night and you get to sleep well but....\n you wake up and your body is covered in bites and you are covered in sweat. You try to get up but your legs are aking horribly. Thi         is puts you in a disadvantage for the next day")


