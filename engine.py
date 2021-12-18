from scenes import *
#scenes contain all the scenes file and is written in the other file for further expantions

class Map(object):
    """A dictionary of all the scenes and their calls"""
    scenes={'main': CentralCorridor(),
            'dead': dead(),
            'left': EmptyRoom(),
            'right': Sm_room(),
            'left2': Armory(),
            'front': BossRoom()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n- - - - - - - - ")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
#for later
class Inventory(object):
    inv=[]
    def add(self):
        inv.append(self)




print("\n\n\n\t\tMy first Game")
print("\t\t\t\t\tby Anirban Majumder")


print("""\n\nYou were roaming around in an unknown place ,\nsuddenly the ground starts to shake \nand the ground broke apart .
You fell throught the crack in the ground!!!
AND EVERYTHING BECAME DARK.
When you woke up ,you see youself in a dimly lit corridor.""")
a_map = Map("main")
a_game = Engine(a_map)
a_game.play()
