
# Check if a collides b on the left
def left(a, b):
    return b.centerx > a.right > b.left \
            and b.top - a.bottom < -3 \
            and a.top - b.bottom < -3


# Check if a collides b on the right
def right(a, b):
    return b.centerx < a.left < b.right \
            and b.top - a.bottom < -3 \
            and a.top - b.bottom < -3


# Check if a collides b on the top
def top(a, b):
    return b.centery > a.bottom > b.top \
            and b.left - a.right < -3 \
            and a.left - b.right < -3

# Check if a collides b on the bottom
def bottom(a, b):
    return b.centery < a.top < b.bottom \
            and b.left - a.right < -3 \
            and a.left - b.right < -3