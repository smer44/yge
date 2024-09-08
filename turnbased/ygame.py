import pygame

class yGame:

    def __init__(self,w,h,item):
        #self.scenes = scenes
        self.item = item
        self.set_mode(w,h)
        self.key_acts = dict()
        self.clock = pygame.time.Clock()


    #def redraw(self):
    #    self.item.redraw(self.display)
    def set_mode(self,w,h):
        self.display = pygame.display.set_mode((w, h))


    #args and kwargs must be inboxed
    def add_key_action(self, key,fn,*args,**kwargs):
        self.key_acts[key]=(fn,args,kwargs)
        #print(self.acts)

    def run(self):

        while True:
            self.clock.tick(60)
            if self.item.dirty():
                self.item.redraw(self.display)
                pygame.display.update()
            for event in pygame.event.get():
                #print("event : " , event.type)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                #check keydown events:
                if event.type == pygame.KEYDOWN:
                    action = self.key_acts.get(event.key, None)
                    if action:
                        fn, args,kwargs = action
                        fn(*args,**kwargs)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print("yGame.run: MOUSEBUTTONDOWN pressed at ", event.pos)
                    mouse_pos = event.pos
                    self.item.mouse_react(self,mouse_pos)
