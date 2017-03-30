
# Check if a collides b on the left
def left(a, b):
    return b.rect.centerx > a.rect.right > b.rect.left \
            and b.rect.top - a.rect.bottom <= 0 \
            and a.rect.top - b.rect.bottom <= 0


# Check if a collides b on the right
def right(a, b):
    return b.rect.centerx < a.rect.left < b.rect.right \
            and b.rect.top - a.rect.bottom <= 0 \
            and a.rect.top - b.rect.bottom <= 0


# Check if a collides b on the top
def top(a, b):
    return b.rect.centery > a.rect.bottom > b.rect.top \
            and b.rect.left - a.rect.right <= 0 \
            and a.rect.left - b.rect.right <= 0

# Check if a collides b on the bottom
def bottom(a, b):
    return b.rect.centery < a.rect.top < b.rect.bottom \
            and b.rect.left - a.rect.right <= 0 \
            and a.rect.left - b.rect.right <= 0