import pyxel
"""
    Le jeu est simple il y'a deux joueurs les joueurs ont des 
    colisions et peuvent se monter dessus pour passer des 
    obstacles, les boutons téléportent le joueur au bouton
    et il faut arriver à la porte à la fin à deux !
    Et il y'a deux Niveaux

"""
def get_tile(x, y):
    return pyxel.tilemap(0).pget(x//8, y//8)
class page:
    def __init__(self):
        self.page = {}
        pyxel.init(128, 128, title="Pixi et Pixa")
        pyxel.load("skin.pyxres")
        self.page['menu'] = Accueil(self)
        self.page['jeu'] = Jeu(self)
        self.page['jeu2'] = Jeu2(self)
        self.page["niveau"] = Niveau(self)
        self.page["regle"] = Regle(self)
        self.current = 'menu'
        pyxel.run(self.update, self.draw)
    
    def update(self):
        
        self.page[self.current].update()
    
    def draw(self):
        self.page[self.current].draw()   

class Accueil:
    def __init__(self, page):
        global scroll_x

        
        pyxel.mouse(True)

        self.page = page
        self.colid_play = objecte(32,40, 64, 24, 56, 200)
        self.quolid_regle = objecte(32,72, 64, 24, 56, 200)
        self.player1 = objecte(0,96, 8, 8, 32, 112,transparent = 7, imgs = [(32,112),(40,112)])
        self.player2 = objecte(32,96, 8, 8, 32, 48,transparent = 7, imgs = [(32,48),(40,48)])
        self.player1_x_max = self.player1.x + 128
        self.player2_x_max = self.player2.x + 96

        

    

    def update(self):
        print(pyxel.mouse_x,pyxel.mouse_y)
        """mise à jour des variables (30 fois par seconde)"""
        if self.colid_play.collide_mouse((pyxel.mouse_x,pyxel.mouse_y)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            self.page.current = 'niveau'
        if self.quolid_regle.collide_mouse((pyxel.mouse_x,pyxel.mouse_y)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            self.page.current = 'regle'
        # print(pyxel.mouse_x,pyxel.mouse_y)
        if self.player1.x > self.player1_x_max :
            self.player1.x = 0
        if self.player2.x > self.player2_x_max :
            self.player2.x = 0
        self.player1.update( (self.player1.x+1 , self.player1.y))
        self.player1.anime(1)
        self.player2.update( (self.player2.x+1 , self.player2.y))
        self.player2.anime(1)
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, 0, 1856, 128, 128,2)
        self.player1.draw()
        self.player2.draw()
        pyxel.text(39,29,"Pixi et Pixa",7)
        pyxel.text(55,50,"Jouer",7)
        pyxel.text(52,80,"Regles",7)


class Niveau:
    def __init__(self, page):
        global scroll_x

        
        pyxel.mouse(True)

        self.page = page
        self.colid_n1 = objecte(32,40, 64, 24, 56, 200)
        self.colid_n2 = objecte(32,72, 64, 24, 56, 200)
        self.player1 = objecte(0,96, 8, 8, 32, 112,transparent = 7, imgs = [(32,112),(40,112)])
        self.player2 = objecte(32,96, 8, 8, 32, 48,transparent = 7, imgs = [(32,48),(40,48)])
        self.player1_x_max = self.player1.x + 128
        self.player2_x_max = self.player2.x + 96

        

    

    def update(self):
        print(self.player1.x)
        """mise à jour des variables (30 fois par seconde)"""
        if self.colid_n1.collide_mouse((pyxel.mouse_x,pyxel.mouse_y)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            self.page.current = 'jeu'
        if self.colid_n2.collide_mouse((pyxel.mouse_x,pyxel.mouse_y)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            self.page.current = 'jeu2'
        # print(pyxel.mouse_x,pyxel.mouse_y)
        if self.player1.x > self.player1_x_max :
            self.player1.x = 0
        if self.player2.x > self.player2_x_max :
            self.player2.x = 0
        self.player1.update( (self.player1.x+1 , self.player1.y))
        self.player1.anime(1)
        self.player2.update( (self.player2.x+1 , self.player2.y))
        self.player2.anime(1)
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, 0, 1856, 128, 128,2)
        self.player1.draw()
        self.player2.draw()
        pyxel.text(32,26,"Choisir un niveau",7)
        pyxel.text(50,50,"Niveau 1",7)
        pyxel.text(50,82,"Niveau 2",7)

class Regle:
    def __init__(self, page):
        global scroll_x

        
        pyxel.mouse(True)

        self.page = page
        self.player1 = objecte(0,96, 8, 8, 32, 112,transparent = 7, imgs = [(32,112),(40,112)])
        self.player2 = objecte(32,96, 8, 8, 32, 48,transparent = 7, imgs = [(32,48),(40,48)])
        self.player1_x_max = self.player1.x + 128
        self.player2_x_max = self.player2.x + 96

        

    

    def update(self):
        print()
        """mise à jour des variables (30 fois par seconde)"""
        print(pyxel.mouse_x,pyxel.mouse_y)
        if self.player1.x > self.player1_x_max :
            self.player1.x = 0
        if self.player2.x > self.player2_x_max :
            self.player2.x = 0
        self.player1.update( (self.player1.x+1 , self.player1.y))
        self.player1.anime(1)
        self.player2.update( (self.player2.x+1 , self.player2.y))
        self.player2.anime(1)
        if pyxel.btn(pyxel.KEY_RETURN):
            self.page.current = 'menu'
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, 256, 1856, 128, 128,2)
        self.player1.draw()
        self.player2.draw()
        pyxel.text(45,10,"Les Regles",7)
        pyxel.text(6,24,"Joueur 1:",7)
        pyxel.text(6,34,"Droite : D",7)
        pyxel.text(6,44,"Gauche : Q",7)
        pyxel.text(6,54,"Sauter : SPACE",7)
        pyxel.text(67,24,"Joueur 1:",7)
        pyxel.text(67,34,"Droite : =>",7)
        pyxel.text(67,44,"Gauche : <=",7)
        pyxel.text(67,54,"Sauter : Haut",7)
        pyxel.text(6,74, "C'est simple il faut finir ",7)
        pyxel.text(6,84, "les niveaux en s'entraidant ",7)
        pyxel.text(6,94, "(Appuyer sur Entrer pour Menu) ",7)
        


class Jeu:
    def __init__(self, page):
        global scroll_x
        self.page = page
        self.player1 = player(80,88,touche = [pyxel.KEY_D,pyxel.KEY_Q,pyxel.KEY_SPACE])
        self.player2 = player(64,88,image=(32, 112),name='joueur2',touche = [pyxel.KEY_RIGHT,pyxel.KEY_LEFT,pyxel.KEY_UP])
        self.collid = [(0,9),(1,9),(2,9),(1,10), (0, 10)]
        self.scroll_x = ((self.player1.x+self.player2.x)/2)-64 
        self.scroll_y = self.player1.y - 64
        self.b1 = [objecte(160,88,8,8,0,216,transparent = 7),True]
        self.porte = [objecte(263,88,8,8,56,48,transparent = 7),True]
        self.img_p1 = self.player1.player.v - 8
        self.img_p2 = self.player2.player.v - 8
        self.img_p1_n = self.player1.player.v
        self.img_p2_n = self.player2.player.v

    

    def update(self):
        print(self.player1.x, self.player2.x)
        """mise à jour des variables (30 fois par seconde)"""
        self.player1.move(self.collid,self.player2,[self.img_p2, self.img_p2_n])
        self.player2.move(self.collid,self.player1, [self.img_p1, self.img_p1_n])
        if ((self.player1.x+self.player2.x)/2)-64 > 0:
            self.scroll_x = ((self.player1.x+self.player2.x)/2)-64 
        self.scroll_y = (self.player1.y)-64 
        if self.b1[1]:
            if self.b1[0].collide(self.player1):
                self.player2.x = self.b1[0].x
                self.b1[1] = False
            elif self.b1[0].collide(self.player2):
                self.player1.x = self.b1[0].x
                self.b1[1] = False
        if self.player1.x > 250 and self.player2.x > 250:
            self.page.current = 'menu'
            


           
    
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, self.scroll_x, self.scroll_y, 128, 128,8)
        pyxel.camera(self.scroll_x, self.scroll_y)
        self.player1.draw() 
        self.player2.draw()
        self.b1[0].draw()
        self.porte[0].draw()

class Jeu2:
    def __init__(self, page):
        global scroll_x
        self.page = page
        self.player1 = player(80,384,touche = [pyxel.KEY_D,pyxel.KEY_Q,pyxel.KEY_SPACE])
        self.player2 = player(64,384,image=(32, 112),name='joueur2',touche = [pyxel.KEY_RIGHT,pyxel.KEY_LEFT,pyxel.KEY_UP])
        self.collid = [(1,17),(0,17),(2,17),(1,18), (0, 18)]
        self.scroll_x = ((self.player1.x+self.player2.x)/2)-64 
        self.scroll_y = self.player1.y - 64
        self.b1 = [objecte(112,384,8,8,0,216,transparent = 7),True]
        self.porte = [objecte(263,408,8,8,56,48,transparent = 7),True]
        self.img_p1 = self.player1.player.v - 8
        self.img_p2 = self.player2.player.v - 8
        self.img_p1_n = self.player1.player.v
        self.img_p2_n = self.player2.player.v

    

    def update(self):
        print(self.player1.x, self.player2.x)
        """mise à jour des variables (30 fois par seconde)"""
        self.player1.move(self.collid,self.player2,[self.img_p2, self.img_p2_n])
        self.player2.move(self.collid,self.player1, [self.img_p1, self.img_p1_n])
        if ((self.player1.x+self.player2.x)/2)-64 > 0:
            self.scroll_x = ((self.player1.x+self.player2.x)/2)-64 
        self.scroll_y = (self.player1.y)-64 
        if self.b1[1]:
            if self.b1[0].collide(self.player1):
                self.player2.x = self.b1[0].x
                self.player2.y = self.b1[0].y
                self.b1[1] = False
            elif self.b1[0].collide(self.player2):
                self.player1.x = self.b1[0].x
                self.player1.y = self.b1[0].y
                self.b1[1] = False
        if self.player1.x > 245 and self.player2.x > 245:
            self.page.current = 'menu'
            


           
    
    
    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        pyxel.bltm(0, 0, 0, self.scroll_x, self.scroll_y, 128, 128,8)
        pyxel.camera(self.scroll_x, self.scroll_y)
        self.player1.draw() 
        self.player2.draw()
        self.b1[0].draw()
        self.porte[0].draw()




class objecte:
    def __init__(self, x, y, w, h, u, v,obj = 0, transparent=1, imgs=[]) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.u = u
        self.v = v
        self.obj = obj
        self.trans = transparent
        self.imgs = imgs
        self.anime_frame = 0
    
    def update(self, coord : tuple = None):
        if coord != None:
            self.x = coord[0]
            self.y = coord[1]
        
    
    def collide_mouse(self, mousepos : tuple):
        if (self.x < mousepos[0] < self.x + self.w) and (self.y < mousepos[1] < self.y + self.h):
            return True
    
    def anime(self,speed):
        self.anime_frame += speed
        if self.anime_frame > len(self.imgs) - 1:
            self.anime_frame = 0
        elif self.anime_frame < 0:
            self.anime_frame = len(self.imgs)
        self.u = self.imgs[int(self.anime_frame)][0]
    
    def collide(self, player):
        if (self.x <= player.x+8 <= self.x + self.w) and (self.y <= player.y <= self.y + self.h):
            return True
    
    def draw(self):
        pyxel.blt(self.x, self.y, self.obj, self.u, self.v,self.w, self.h, self.trans)

class player():
    def __init__(self, x, y, image = (32, 48), name='player', touche = [pyxel.KEY_D,pyxel.KEY_Q,pyxel.KEY_SPACE]):
        self.player = objecte(x,y, 8, 8, image[0], image[1],transparent = 7, imgs = [image,(image[0]+8, image[1]), (image[0]+16, image[1])])
        self.x = x
        self.y = y
        self.speed = 1.5
        self.air_time = 0
        self.decent = False
        self.inair = False
        self.can_jump = True
        self.movement = None
        self.touche = touche
        self.name = name
    
    
    
    def move(self,wall,player, img_porter):
        
        if self.collision_player(player) =="bas":
            player.player.v = img_porter[0]
        else:
            player.player.v = img_porter[1]
        if self.inair and not self.decent:
            self.y -= 1
            self.air_time += 1
        if self.decent:
            self.y += 1

        if self.collision(wall) == 'bas' or self.collision_player(player) == "bas" :
            self.inair = False
            self.can_jump = True
            if self.air_time == 0:
                self.decent = False
            self.air_time = 0
        
        elif self.collision(wall) == 'haut':
            self.air_time = 0
            self.decent = True
            
        elif (self.collision(wall) != 'bas' and self.collision_player(player) != "bas") and self.inair == False:
            print("je suis en l'air")
            self.decent = True
            
        if self.air_time > 10:
            self.air_time = 0
            self.decent = True
        if pyxel.btn(self.touche[0]) and self.collision_coter(wall) != "gauche" and self.collision_player(player) != "droite":
            self.player.anime(1)
            self.x += self.speed
            self.movement = 'right'
            if player.collision_player(self) == "bas":
                player.x += self.speed
        if pyxel.btn(self.touche[1]) and self.collision_coter(wall) != "droite" and self.collision_player(player) != "gauche":
            self.player.anime(1)
            self.movement = 'left'
            self.x -= self.speed
            if player.collision_player(self) == "bas":
                    player.x-= self.speed
        if pyxel.btn(self.touche[2])  and not self.inair:
            self.can_jump = False
            self.decent = False
            self.inair = True
    
    def collision(self, walls):
        if get_tile(self.x+0.1,self.y+7.9) in walls or get_tile(self.x+7.9,self.y+8) in walls:
            return 'bas'
        if get_tile(self.x+0.1,self.y+7.9) in walls or get_tile(self.x+7.9,self.y+0.1) in walls:
            return 'haut'
        
    def collision_coter(self, walls):
        if get_tile(self.x+9,self.y+7.9) in walls :
            return 'gauche'
        elif get_tile(self.x-1,self.y+7.9) in walls:
            return 'droite'
        
    def collision_player(self,player):
        if (self.x - 8 < player.x  < self.x + self.player.w) and (self.y - 8< player.y < self.y + 8 ):
            
            if self.x+7 <= player.x <= self.x + 9:
                return 'droite' 
            if self.x-1 <= player.x+8 <= self.x+1:
                return 'gauche'
            if self.y - 2 <= player.y-8 <= self.y + 2 :
                print("bas")
                return 'bas' 
               
    
    def draw(self):
        self.player.update((self.x,self.y))
        self.player.draw()


if __name__ == "__main__":
    page()