#Write a function ball_collide that takes two balls as parameters and computes if they are  colliding. Your function should return a Boolean representing whether or not the balls are colliding.
#Hint: Represent a ball on a plane as a tuple of (x, y, r), r being the radius If (distance between two  balls centers) <= (sum of their radii) then (they are colliding).

def ball_collide(ball1, ball2):
    (x1, y1, r1) = ball1
    (x2, y2, r2) = ball2
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if distance <= (r1 + r2):
        return True
    else:
        return False

print ("Enter the coordinates of the first ball: ")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
r1 = int(input("r1: "))
print ("Enter the coordinates of the second ball: ")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
r2 = int(input("r2: "))
print ("Whether the balls are colliding: ", ball_collide((x1, y1, r1), (x2, y2, r2)))
