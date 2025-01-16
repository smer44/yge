from yge.turnbased.yboxplacer import yBoxPlacer

box = yBoxPlacer("test",3,0,100)

box.place_start((0,0,1920,1080))
print("-- to right dir --")
for _ in range(3):
    print(box.place_next())

box = yBoxPlacer("test2",3,1,100)

box.place_start((0,0,1920,1080))
print("-- to bottom dir --")
for _ in range(3):
    print(box.place_next())


box = yBoxPlacer("test3",3,2,100)

box.place_start((0,0,1920,1080))
print("-- to left dir --")
for _ in range(3):
    print(box.place_next())

box = yBoxPlacer("test4",3,3,100)

box.place_start((0,0,1920,1080))
print("-- to top dir --")
for _ in range(3):
    print(box.place_next())

