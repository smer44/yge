import tkinter as tk
import time
from math import sin,cos, radians
# Data for 5 frames of the walk cycle (hip, knee1, foot1, knee2, foot2 positions)


a_stickman_2 = [30,15,45,30,60]
a_stickman_4 = [135,80,47,120,130]

a_stickman_1 = [130,150,150,110,50]
a_stickman_3 = [140,190,210,190,180]

aas_stickman = [a_stickman_1,a_stickman_2,a_stickman_3,a_stickman_4]
def to_angles(a1,a2,a3,a4):
    aa1 = a1 + a2
    aa2 = a2 + a1
    aa3 = a3 + a4
    aa4 = a4 + a3
    angles = [aa1, aa2, aa3, aa4]
    return angles

##angles2 = [75,85,95,110,120,]
#angles4 = [85,95,105,120,130,]

#angles1 = [130,110,90,75,60]
#angles3 = [190,230,180,165,140]

#angles1 = [120,110,75,50,40,]
#angles3 = [230,195,185,160,50,]


#Stand then run sequence:
angles2 = [100,105,110,120,90,]
angles4 = [105,110,150,190,230,]

angles1 = [45,20,25,60,80]
angles3 = [160,110,95,90,85]

a_stand_then_go2 = [89,85,80,70,55] + angles1+ angles2 + angles1 + angles2
a_stand_then_go4 = [91,120,140,150,155] + angles3+ angles4 + angles3 + angles4

a_stand_then_go1 = [85,89,91,95,97] +angles2 + angles1 + angles2 + angles1
a_stand_then_go3 = [95,91,93,97,100] +angles4 + angles3 + angles4 + angles3

#skateboard sequence:

a_skate1 = [40,40,40,40,40,40,40] * 4
a_skate3 = [95,95,95,95,95,95,95] * 4

a_skate2 = [60,20,10,60,105,150,130] * 4
a_skate4 = [190,130,85,70,115,155,195] * 4

aas = [angles1,angles2,angles3,angles4]
aas_stand_then_go = [a_stand_then_go1, a_stand_then_go2, a_stand_then_go3, a_stand_then_go4]

aas_skate = [a_skate1,a_skate2,a_skate3,a_skate4]

angles = aas_skate#aas_stand_then_go

#angles1 = [0] * 5
#angles3 = [0] * 5

#angles = to_angles(*aas_stickman)
#angles = to_angles(*aas)
#angles = to_angles(*aas_stand_then_go)
def frames_from_angles(xy0,r1,r2,as1, as2, as3, as4):


    lena = len(as1)
    assert lena == len(as2) and lena == len(as3) and lena == len(as4) , f"frames_from_angles : lens of angles arrays are unequal {lena} , {len(as2)} , {len(as3)} , {len(as4)}"
    frames = []

    for n,(x0,y0) in enumerate(xy0):
        na = n % lena
        a1, a2, a3, a4 = as1[na], as2[na], as3[na], as4[na]

    #for (x0,y0),a1,a2,a3,a4 in zip(xy0,angles1, angles2, angles3, angles4):

        frame = [(x0,y0)]
        frames.append(frame)
        x1 = x0 + r1 * cos(radians(a1))
        y1 = y0 + r1 * sin(radians(a1))
        frame.append((x1,y1))
        x2 = x1 + r2 * cos(radians(a3))
        y2 = y1 + r2 * sin(radians(a3))
        frame.append((x2, y2))
        x3 = x0 + r1 * cos(radians(a2))
        y3 = y0 + r1 * sin(radians(a2))
        frame.append((x3, y3))
        x4 = x3 + r2 * cos(radians(a4))
        y4 = y3 + r2 * sin(radians(a4))
        frame.append((x4, y4))
    return frames

def to_bottom(ymax,frame):
    frame_ymax = max(t[1] for t in frame)
    diff = ymax - frame_ymax
    ret = [(t[0], t[1]+diff) for t in frame]
    return ret


def to_left(fr_start,fr_end,point_nr,frames):
    pass




frames = [
    # Frame 1
    [(200, 300), (180, 350), (160, 400), (220, 350), (240, 400)],
    # Frame 2
    [(210, 300), (185, 345), (170, 390), (215, 355), (235, 410)],
    # Frame 3
    [(220, 300), (190, 340), (180, 380), (210, 360), (230, 420)],
    # Frame 4
    [(230, 300), (185, 345), (170, 390), (215, 355), (235, 410)],
    # Frame 5
    [(240, 300), (180, 350), (160, 400), (220, 350), (240, 400)]
]

y0s_stickman = [230,220,220,230,240] * 4
y0s_run = [205,205,205,205,205] *4

y0s_start = [200,200,200,200,200]
#stand then go:
y0s = y0s_start +y0s_run
x_run_start = 120

#for start run:
x0s = [100,105,110,115] + [(x_run_start + 50*n) for n in range(len(y0s_run))]
xy0 = [(x,y) for x,y in zip(x0s,y0s) ]

#for skate:
y0s_skate = [205,205,205,205,205] *4
xy0 = [(120+50*n, y) for n, y in enumerate(y0s_skate)]



#xy0 = [(200,230), (250,200), (300,200),(400,230),(500,240),(600,230), (700,200), (800,200),(900,230),(1000,240)]

frames = frames_from_angles(xy0,100,100,*angles)


bottom = 400

#frames = [to_bottom(400,f) for f in frames]

class WalkAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=2400, height=500, bg='white')
        self.canvas.pack()
        self.frame_index = 0

        # Draw initial skeleton
        self.joint_size = 5
        self.hip = self.canvas.create_oval(195, 295, 205, 305, fill='black')
        self.knee1 = self.canvas.create_oval(175, 345, 185, 355, fill='black')
        self.foot1 = self.canvas.create_oval(155, 395, 165, 405, fill='black')
        self.knee2 = self.canvas.create_oval(215, 345, 225, 355, fill='black')
        self.foot2 = self.canvas.create_oval(235, 395, 245, 405, fill='black')

        self.skate = self.canvas.create_line(200, 300, 180, 350, width=5, fill = "blue")

        # Lines for the legs
        self.leg1_upper = self.canvas.create_line(200, 300, 180, 350, width=2)
        self.leg1_lower = self.canvas.create_line(180, 350, 160, 400, width=2)
        self.leg2_upper = self.canvas.create_line(200, 300, 220, 350, width=2, fill = "red")
        self.leg2_lower = self.canvas.create_line(220, 350, 240, 400, width=2, fill = "red")


        self.ground = self.canvas.create_line(0, 400, 2400, 400, width=5, fill = "gray")
        # Start the animation loop
        self.update_frame()

    def update_frame(self):
        # Get joint positions for the current frame
        positions = frames[self.frame_index]
        hip_pos, knee1_pos, foot1_pos, knee2_pos, foot2_pos = positions

        # Update joints (circles)
        self.canvas.coords(self.hip, hip_pos[0] - self.joint_size, hip_pos[1] - self.joint_size,
                           hip_pos[0] + self.joint_size, hip_pos[1] + self.joint_size)
        self.canvas.coords(self.knee1, knee1_pos[0] - self.joint_size, knee1_pos[1] - self.joint_size,
                           knee1_pos[0] + self.joint_size, knee1_pos[1] + self.joint_size)
        self.canvas.coords(self.foot1, foot1_pos[0] - self.joint_size, foot1_pos[1] - self.joint_size,
                           foot1_pos[0] + self.joint_size, foot1_pos[1] + self.joint_size)
        self.canvas.coords(self.knee2, knee2_pos[0] - self.joint_size, knee2_pos[1] - self.joint_size,
                           knee2_pos[0] + self.joint_size, knee2_pos[1] + self.joint_size)
        self.canvas.coords(self.foot2, foot2_pos[0] - self.joint_size, foot2_pos[1] - self.joint_size,
                           foot2_pos[0] + self.joint_size, foot2_pos[1] + self.joint_size)

        # Update legs (lines)
        self.canvas.coords(self.leg1_upper, hip_pos[0], hip_pos[1], knee1_pos[0], knee1_pos[1])
        self.canvas.coords(self.leg1_lower, knee1_pos[0], knee1_pos[1], foot1_pos[0], foot1_pos[1])
        self.canvas.coords(self.leg2_upper, hip_pos[0], hip_pos[1], knee2_pos[0], knee2_pos[1])
        self.canvas.coords(self.leg2_lower, knee2_pos[0], knee2_pos[1], foot2_pos[0], foot2_pos[1])

        self.canvas.coords(self.skate, foot1_pos[0]-100, foot1_pos[1],foot1_pos[0]+100, foot1_pos[1])

        # Move to the next frame, looping back at the end of the cycle
        self.frame_index = (self.frame_index + 1) % len(frames)

        # Schedule the next frame update
        self.root.after(500, self.update_frame)

# Run the Tkinter app
root = tk.Tk()
animation = WalkAnimation(root)
root.mainloop()
