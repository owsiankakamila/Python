

width = int(input("Width: "))
height = int(input("Height: "))

screen = 0
if height%2 ==0:
    height_center = height//2
if height%2 ==1:
    height_center = (height//2) +1

display =0

while screen <=10:

    if display== height_center:
        display=0

    for w in range(0,height):
        for k in range(0,width):
            if (w==display) or (w==height-1-display):
                if (k<display) or (k> width -1 - display):
                    print("o", end="")
                else:
                    print("x", end="")
            elif (w>display) and (w<height-1-display):
                if (k==display) or (k== width -1 - display):
                    print("x", end="")
                else:
                    print("o", end="")
            else:
                    print("o", end="")
        print("")

    print("")

    screen+=1
    display+=1