import pyglet
from map import Tilemap

window = pyglet.window.Window()

image = pyglet.image.load('img.png')
sprite = pyglet.sprite.Sprite(image, x = 50, y = 50)
sprite.velocity_x = 0
sprite.velocity_y = 0
map = Tilemap(640, 480, 32)

def update(dt):
    sprite.velocity_y -= 0.1
    sprite.velocity_x, sprite.velocity_y = map.slide_contact(sprite.x, sprite.y, sprite.width, sprite.height, sprite.velocity_x, sprite.velocity_y)
    sprite.x += sprite.velocity_x
    sprite.y += sprite.velocity_y
    print(sprite.x, sprite.y, sprite.width, sprite.height)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
