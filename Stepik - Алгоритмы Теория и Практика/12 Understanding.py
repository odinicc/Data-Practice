lin = [
    [1,5],
    [2,8],
    [4,9],
    [6,8],
    [8,12],
    [6,9],
]

right_side_righter = 0
right_side_lefter = 0
left_side_lefter = 0
left_side_righter = 0
t = 8
for h in lin:
    if h[1] >= t:
        right_side_righter += 1
    else:
        right_side_lefter +=1
    if h[0] <= t:
        left_side_lefter += 1
    else:
        left_side_righter += 1


print("right_side_righter = ", right_side_righter)
print("right_side_lefter = ", right_side_lefter)
print("left_side_lefter = ", left_side_lefter)
print("left_side_righter = ", left_side_righter)
print("n1 = ", right_side_righter - left_side_righter)
print("n2 = ", right_side_lefter - left_side_lefter)