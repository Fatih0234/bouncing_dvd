
"""Bouncing DVD logo, by Fatih Karahan
A bouncing DVD logo animation. You have to be "of a certain age " to appreciate this.
Press Ctrl-C top stop. 
Note: Do not resize the terminal window while this program is running.
Tags: short, artistic, bext """

import sys, random, time

try: 
    import bext
except ImportError:
    print("This program requires the bext module, which you can install following the instructions at https://pypi.org/project/Bext/")

width, height = bext.size()

# we cannot print to the last column on Windows without it adding a 
# newline automatically, so reduce the width by one:

width -= 1

number_of_logos = 5
pause_amount = 0.0001

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

up_right    = "ur"
up_left     = "ul"
down_right  = "dr"
down_left   = "dl"
directions  = (up_right, up_left, down_left, down_right)

# key names for logo dictionaries:

color = "color"
x = "x"
y = "y"
dir = "directions"

def main():
    bext.clear()


    # Generate some logos. 

    logos = []

    # Let's generate the logos
    for i in range(number_of_logos):
        logos.append({
                color: random.choice(colors),
                x: random.randint(1,width-4),
                y: random.randint(1,height -4),
                dir: random.choice(directions)
        })

        if logos[-1][x] % 2 == 1:
            logos[-1][x] -= 1
    corner_counting = 0
    while True:
        for logo in logos: 
            
            bext.goto(logo[x], logo[y])
            print("   ", end="")
            original_direction = logo[dir]
            # Let's check whether it hits the corner.
            if logo[x] == 0 and logo[y] == 0:
                corner_counting += 1
                logo[dir] = down_right
            elif logo[x] == width - 3 and logo[y] == 0:
                corner_counting += 1
                logo[dir] = down_left
            elif logo[x] == 0 and logo[y] == height - 1:
                corner_counting += 1
                logo[dir] = up_right
            elif logo[x] == width - 3 and logo[y] == height - 1:
                corner_counting += 1
                logo[dir] = up_left

            # Check whether it hits the edges

            # left
            elif logo[x] == 0 and logo[dir] == up_left:
                logo[dir] = up_right
            elif logo[x] == 0 and logo[dir] == down_left:
                logo[dir] = down_right
            # right
            elif logo[x] == width - 3 and logo[dir] == down_right:
                logo[dir] = down_left
            elif logo[x] == width - 3 and logo[dir] == up_right:
                logo[dir] = up_left
            # top
            elif logo[y] == 0 and logo[dir] == up_left:
                logo[dir] = down_left
            elif logo[y] == 0 and logo[dir] == up_right:
                logo[dir] = down_right
            # bottom
            elif logo[y] == height-1 and logo[dir] == down_left:
                logo[dir] = up_left
            elif logo[y] == height-1 and logo[dir] == down_right:
                logo[dir] = up_right

            if logo[dir] != original_direction:
                logo[color] = random.choice(colors)
            # Move the logo

            if logo[dir] == up_left:
                logo[x] -= 2
                logo[y] -= 1
            elif logo[dir] == up_right:
                logo[x] += 2
                logo[y] -= 1
            elif logo[dir] == down_left:
                logo[x] -= 2
                logo[y] += 1
            elif logo[dir] == down_right:
                logo[x] += 2
                logo[y] += 1
        
        # Write the counter_bounces
        bext.goto(5,0)
        bext.fg("white")
        print("Number of corner counting:", corner_counting, end="")

        for logo in logos:
            bext.goto(logo[x], logo[y])
            print("DVD", end="")
            bext.fg(random.choice(colors))

        bext.goto(0, 0)

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(pause_amount)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD logo, by al sweigart")
        sys.exit() # When ctrl-c is pressed, end the program.


















