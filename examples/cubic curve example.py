import matplotlib.pyplot as plt
import numpy as np


def mid(a,b):
    return ((a[0] + b[0])//2 , (a[1] + b[1])//2)

def de_casteljau_numpy(pts,depth):
    stack = [pts]
    #yield (p0,p3)
    while(depth > 0):
        new_entries = []
        while stack:
            points = stack.pop()
            midpoints_1 = (points[:-1] + points[1:])//2
            midpoints_2 = (midpoints_1[:-1] + midpoints_1[1:])//2
            p0123 = (midpoints_2[0]+midpoints_2[1]) // 2
            new_entries.append(np.array((points[0],midpoints_1[0],midpoints_2[0],p0123)))
            new_entries.append(np.array((p0123, midpoints_2[1], midpoints_1[2], points[3])))
        stack = new_entries
        depth -=1
    for pts in stack:
        yield (pts[0],pts[3])


import tkinter as tk


class BezierCanvas(tk.Canvas):
    def __init__(self, master, p0, p1, p2, p3, depth, **kwargs):
        super().__init__(master, **kwargs)
        self.depth = depth
        self.control_points = np.array([p0, p1, p2, p3])
        self.point_radius = 10
        self.draw_curve()
        self.selected = None
        self.bind("<Button-1>", self.select)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<Button-2>", self.start_drag_all)
        self.bind("<B2-Motion>", self.drag_all)
        self.drag_point = None
        #self.bind("<Configure>", self.on_resize)

    def draw_curve(self):
        self.delete("all")
        for p0, p3 in de_casteljau_numpy(self.control_points, self.depth):
            self.create_line(p0[0], p0[1], p3[0], p3[1], fill="blue")
        r = self.point_radius
        for x, y in self.control_points:
            self.create_oval(x - r, y - r, x + r, y + r,
                             fill="red", tags="control")

    def drag(self, event):
        if self.selected is not None:
            self.control_points[self.selected] = [event.x, event.y]
            #self.update_points()
            self.draw_curve()


    def select(self,event):
        for idx, (x, y) in enumerate(self.control_points):
            if abs(event.x - x) < self.point_radius and abs(event.y - y) < self.point_radius:
                self.selected = idx
                return
        self.selected = None

    def start_drag_all(self,event):
        self.drag_point = [event.x,event.y]

    def drag_all(self,event):
        dx = event.x-self.drag_point[0]
        dy = event.y-self.drag_point[1]
        for point in self.control_points:
            point[0] +=dx
            point[1] +=dy

        self.drag_point = [event.x, event.y]
        self.draw_curve()





    def on_resize(self,event):
        #not working
        # determine the ratio of old width/height to new width/height
        #wscale = float(event.width)/self.width
        #hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        #self.scale("all",0,0,wscale,hscale)


    def update_points(self):
        self.p0, self.p1, self.p2, self.p3 = self.control_points


def de_casteljau_integer(p0, p1, p2, p3, depth):
    stack = [(p0, p1, p2, p3)]
    while depth > 0:
        new_entries = []
        while stack:
            p0, p1, p2, p3 = stack.pop()
            p01 = [(p0[0] + p1[0]) // 2, (p0[1] + p1[1]) // 2]
            p12 = [(p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2]
            p23 = [(p2[0] + p3[0]) // 2, (p2[1] + p3[1]) // 2]
            p012 = [(p01[0] + p12[0]) // 2, (p01[1] + p12[1]) // 2]
            p123 = [(p12[0] + p23[0]) // 2, (p12[1] + p23[1]) // 2]
            p0123 = [(p012[0] + p123[0]) // 2, (p012[1] + p123[1]) // 2]
            new_entries.append((p0, p01, p012, p0123))
            new_entries.append((p0123, p123, p23, p3))
        stack = new_entries
        depth -= 1
    for p0, p1, p2, p3 in stack:
        yield (p0, p3)


if __name__ == "__main__":
    root = tk.Tk()
    p0 = [100, 300]
    p1 = [150, 100]
    p2 = [250, 100]
    p3 = [300, 300]
    depth = 4
    canvas = BezierCanvas(root, p0, p1, p2, p3, depth, width=400, height=400)
    canvas.pack(fill="both", expand=True)
    root.mainloop()
