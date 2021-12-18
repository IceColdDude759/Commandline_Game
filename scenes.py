from random import randint
from sys import exit

"""centralcorridor-left/right/north/south==empty,monster_with_reward,
main boss and escape,armory"""
#for now upto this.....


#some of the global shit here

inventory=[]
phealth=100
mhealth=1000
y=1

class Scene(object):
    """PARENT CLASS"""
    def enter(self):
        print("fuck this shit,how do u execute this ?/")
        exit(1)


class CentralCorridor(Scene):
    def enter(self):

        print("The corridor seem to be very long,\nit was dark and you cant make out what at end? ")
        print("There is a door to  your Right.")
        print("There is a door to  your left .")
        print("Which door do u take?")
        door=input("> ")
        if not (door =="left"or door=="right"or door=="forward"or door=="front" or door=="walk stright" or door=="stright"or door=="go stright" or door=="go back"or door=="back" or door=="run"):
            print("\nA hole appear in the ground and you fall through the hole in the ground and die....")
            return "dead"
        elif(door=="go back"or door=="back" or door=="run"):
            print("You can not go back as some rock blocking the path behind you.")
            return "main"
        elif (door=="forward"or door=="front" or door=="walk stright" or door=="stright" or door=="go stright"):
            print("After few turns and Corridor became narrower and you came\n to a dead end and as you were going to turn back,two doors magically appear.")
            print("There is a door to  your Front .")
            print("There is a door to  your left .")
            print("Which door do u take?")
            door=input("> ")
            if not (door=="front" or door =="left"or door=="forward"):
                print("\nA hole appear in the ground and you fall\n through the hole in the ground and die...")
                return "dead"
            elif(door=="go back"or door=="back" or door=="run"):
                return "main"
            elif (door=="left"):
                return"left2"
            elif(door=="forward"or door=="front"):
                print("The door seem to be locked")
                print("The left door suddenly open ")
                print("Do You go in?")
                door=input("> ")
                if (door=="yes"):
                    return "left2"
                else:
                    return "main"
        return door






class dead(Scene):
#more later
    roast=["You suck at this so much,that it is incomprehensible.",
            " Your mom would be proud.......of your dumb-ness",
            "I have a puppy that do this better than you",
            "Is your brain made up of shit??"]
    def enter(self):
        print(dead.roast[randint(0,3)])
        exit(1)






class EmptyRoom(Scene):

    def enter(self):
        print("You opened the door ,it opened with a cracking sound.")
        print("""Inside of the room is candel-lit, with some weird
marking on the wall, WITH BLOOD!!!""")
        print("It was like something from a Horror movie......")
        print("You search the room for sometime and found nothing.")
        print("What do you do ?")
        door=input("> ")
        if not(door=="stay" or door == "go back" or door == "back"):
            print("Suddenly a dark poisenous fog sorrounds you ,and you fainted \n later you woke up in heaven......... ")
            return "dead"
        elif (door == "stay"):
            return "left"
        else :
            return "main"



#health and combat system later
class Sm_room(Scene):

    def enter(self):
        print("The door open smoothly like it was weight-less")
        print("The rooom is very dark ,but it was a big room")
        print("Cause you saw somthing shining in the back of the big darkness")
        print("After a few step you saw a candel and lighter")
        print("what do You do?")
        door=input("> ")
        if (door == "go back" or door == "back"):
            return "main"
        elif (door=="stay"):
            return "right"
        elif(door=="light candel" or door=="candel" or door=="light lighter" or door=="light" or door=="candel"):
            print("\nThe whole room became lighted,The wall became shiny")
            print("You understand that the wall are reflective ")
            print("There is a huge bear lying in middle of the room. ")
            print("""The bear woke up and look at you with furious eye
you quickly look around the room and
Saw a bottle of honey in the corner of the room
What do you do ?""")
            door=input("> ")
            if (door=="give honey" or door=="honey" or door=="take honey and give to bear"):
                print("The bear take the honey from you and drink it ")
                print("Then the bear fall to sleep and revail the heap of gold coin behind him")
                print("what do you do ?")
                door =input("> ")
                if (door=="take gold"or door=="gold"or door=="take"):
                    print("how much?")
                    door =input("> ")
                    if int(door)<1000000:
                        print("Now you are rich.....\nThere is a magical portal \nDo you take it? ")
                        inventory.append(str(door)+" Gold")
                        door=input("> ")
                        if (door=="yes"):
                            return "main"
                        else:
                            print("A trap activate and you DIE....")
                            return"dead"
                    else:
                        print("A trap activates and you DIE....")
                        return"dead"
                elif (door == "go back" or door == "back"):
                    return "main"
                elif (door=="stay"):
                    return "right"
                else :
                    print("A trap activates and you DIE....")
                    return"dead"

            elif (door == "go back" or door == "back"):
                return "main"
            elif (door=="stay"):
                return "right"
            else :
                print("The bear slap your Head Off....")
                return "dead"
        else:
            print("A huge bear comes and slap your head off.....")
            return "dead"



class Armory(Scene):
    def enter (self):
        print("It is a heavy metal door.It opened slowly")
        print("The room is sci-fi ,all around Neon light ")
        print("Instrument and tools all around.")
        print("There are some weapon lying around.")
        print(" AK47 , LaserGun ,RocketLauncher,Pokeball")
        print("You can carry only 2 ,what will be your first weapon?")
        door=input("> ")
        inventory.append(door)
        print("what will be you second weapon?")
        door=input("> ")
        inventory.append(door)
        print("After taking the weapons , the haevy meatal door shut with a \"THUD\" sound!!")
        print("It is totally locked ,no way to open")
        print("You started to look around")
        print("You saw a note under the weapon you took..")
        print("""The Note :IF YOU WANT TO GET OUT OF HERE ,YOU HAVE \nTO DEFEAT THE GARGENCHUYA MOSTER AND GO THROUGH THE PATH IT GUARDS""")
        print("There is a teleport in the corner of the room . \nDo you take it?")
        door=input("> ")
        if (door=="yes"):
            return "front"
        elif (door=="no"):
            print("\nSuddenly a trap activates and your body get disintrigated into atoms")
            return "dead"
        else:
            print("\nSuddenly a trap activates and your body get disintrigated into atoms")
            return "dead"



class BossRoom(Scene):
    def enter(self):
        phealth=100
        mhealth=1000
        y=1
        print("The scary Door behind you atomatically closed.")
        print("The room is huge as a basketball court and is candel-lit \nIt has a medival feel to it.")
        print("At the end of the room is a room with stairs going up")
        print("It has a strange glow to it ,like sunlight not this dull candel-light")
        print("After looking closely you see a EXIT sign on it!!")
        print("As you are going towards it,A huge monsters appear \"\"\"The GARGENCHUYA\"\"\" !!!")
        print("IT was huge and fat, taller than 10 elephants stacked on top of each other,\nit was ugly as a hag \n and most disgusting it had saliva droping all over from its mouth ,\nif that hole in the neck can even be consider as a mouth")
        print("The monster started doing what they do best : ATTACKING you")
        print("In your inventory you have : "+", ".join(inventory))
        a1="\nThe monster raise it hand in the air and wants to squach you"
        a2="\nThe monster seem to do noting for now"
        a3="\nIt has tenticle coming from it body toward you"
        lis=[a1,a2,a3]
        fa="\nIt spread something from its mouth,it spread all over the room,\n IT IS POISEN ,you will take damage from now on"
        dead="\nThe monster kills you and tear you from limb to limb and eats you"
        print("\n\nYou can do the following actions :dodge  0R attact with you weapon\n to attack with weapon just type in the weapon name...\nps- use small letters and no space in the gun name")
        print("\n\t\tBATTLE START")
        while (phealth>0 and mhealth>0):
            pd=0
            md=0
            if (mhealth<100 and y==1):
                print(fa)
                y=0
            else:
                b1=lis[randint(0,2)]
                print(b1)
                print("what do you do?")
                door=input("> ")
                if (b1==a1):
                    if (door=="dodge"):
                        print("\nYou dodged it and you are safe.")
                        pd=0
                    else:
                        pd=60
                elif(b1==a3):
                    if (door=="dodge"):
                        print("\nYou cant dodged it,it was very fast and you are hurt.")
                        pd=8
                    else:
                        pd=8
                if (door=="ak47"):
                    md=175
                elif(door=="lasergun"):
                    md=200
                elif (door=="rocketlauncher"):
                    md=230
                elif(door=="pokeball"):
                    print("\nMew appear from the pokeball and attack the monster and went back into the pokeball")
                    md=300

                if (y==0):
                    pd=pd+5
                phealth=phealth-pd
                mhealth=mhealth-md
                pdd=str(pd)
                mdd=str(md)
                mh=str(mhealth)
                ph=str(phealth)
    #correct concat shit
                print("\nYou took "+pdd+" damage"+"     \t   Your health = "+ph)
                print("Monster took "+mdd+" damage"+"\t   Monster health = "+mh)
        if(phealth<=0):
            print(dead)
            return "dead"
        if(mhealth<=0):
            print("\nYOU WIN and got out of the dungen alive")
            q=inventory[0].split(" ")
            p=q.pop(-1)
            if (p=="Gold"):
                print("ANd you are rich with "+inventory[0])
            print("Good job now your mom would be really proud...")
            exit(1)
