import pyglet
from map import Tilemap
from pyglet.window import key

window = pyglet.window.Window()
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

image = pyglet.image.load('img.png')
sprite = pyglet.sprite.Sprite(image, x = 50, y = 50)
sprite.velocity_x = 0
sprite.velocity_y = 0
map = Tilemap(128, 128, 32)

def update(dt):
    sprite.velocity_y -= 0.1
    sprite.velocity_x, sprite.velocity_y = map.slide_contact(sprite.x, sprite.y, sprite.width, sprite.height, sprite.velocity_x, sprite.velocity_y)
    sprite.x += sprite.velocity_x
    sprite.y += sprite.velocity_y
    if keys[key.D]:
        sprite.velocity_x += 0.1
    elif keys[key.A]:
        sprite.velocity_x -= 0.1
    else:
        sprite.velocity_x=0


@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
