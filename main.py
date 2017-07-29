import pyglet

window = pyglet.window.Window()

image = pyglet.image.load('img.png')
sprite = pyglet.sprite.Sprite(image, x = 50, y = 50)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()
