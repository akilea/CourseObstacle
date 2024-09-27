from ursina import *
from sample import color,Texture
from typing import Callable

class Board(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.tiles = list()
        size_x = 6
        size_z = 6
        self.max_board_index = (size_x * size_z) - 1
        for i in range(0,size_x):
            for j in range(0,size_z):
                cur_color = color.white if (i+j)%2 else color.black66
                new_tile = Entity(model="cube", color=cur_color,parent=self)
                new_tile.position = Vec3(i,j,0)
                self.tiles.append(new_tile)
                
    def tile_to_pos(self,board_index):
        pass
    
    def get_state(self,board_index):
        pass
    
    def is_winning(self,board_index):
        return board_index == self.max_board_index
    
    def is_at_start(self,board_index):
        return board_index == 0
    
    def can_move_to(self,board_index):
        return board_index >= 0 and board_index <= self.max_board_index


     
#if __name__ == "__main__": 
app = Ursina()
application.hot_reloader.hotreload = True

b = Board()

EditorCamera()
app.run()