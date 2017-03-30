

# Check if a collides b on the left
def left(a, b):
    return b.rect.right > a.rect.right >= b.rect.left \
            and b.rect.top - a.rect.bottom <= 0 \
            and a.rect.top - b.rect.bottom <= 0


# Check if a collides b on the right
def right(a, b):
    return b.rect.left < a.rect.left <= b.rect.right \
            and b.rect.top - a.rect.bottom <= 0 \
            and a.rect.top - b.rect.bottom <= 0


# Check if a collides b on the top
def top(a, b):
    return b.rect.top < a.rect.bottom <= b.rect.bottom \
            and b.rect.right - a.rect.left <= 0 \
            and a.rect.right - b.rect.left <= 0

# Check if a collides b on the bottom
def bottom(a, b):
    return b.rect.bottom > a.rect.top >= b.rect.top \
            and b.rect.right - a.rect.left <= 0 \
            and a.rect.right - b.rect.left <= 0