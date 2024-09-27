from ursina import *
from sample import color,Texture
from typing import Callable

class Pion(Entity):
    def __init__(self,color,texture) -> None:
        #Base du pion
        super().__init__(model=Cylinder(resolution=50,radius=0.25*0.5,start=0,height=0.05), color=color,texture=texture)
        self.model_body = Entity(model=Cylinder(resolution=50,radius=0.05,start=0.05,height=0.3), color=color,texture=texture,parent=self)
        self.model_head = Entity(model="sphere", color=color,texture=texture,scale=0.2,parent=self)
        self.model_head.position = Vec3(0,0.35,0)
        self.offset = Vec3(0,0,0)
    
    def set_offset(self,offset):
        if isinstance(offset,Vec3):
            self.offset = offset
        else:
            raise Exception()
        
    def teleport(self,destination):
        if isinstance(destination,Vec3):
            self.position = destination + self.offset
        else:
            raise Exception()
    
    def animate_to(self,list_position, call_on_end_anim):
        #TODO: Trouver comment avoir accès à un delegate quand l'animation est terminée.
        if isinstance(list_position,list) and len(list_position) > 0 and isinstance(list_position[-1],Vec3):
            animator = self.animate_position(list_position[-1] + self.offset, duration=1, curve=curve.in_out_expo)
        else:
            raise Exception()
        
        if isinstance(call_on_end_anim,Callable): 
            call_on_end_anim()
        else:
            raise Exception()
    
    def compute_rule(self): 
        return tuple(1,6)
     
#if __name__ == "__main__": 
app = Ursina()
application.hot_reloader.hotreload = True
p = Pion(color=color.blue_flame,texture=Texture.lava)
p.teleport(Vec3(5,0,0))

def patate():
    pass

p.animate_to([Vec3(0,0,0)],patate)

EditorCamera()
app.run()