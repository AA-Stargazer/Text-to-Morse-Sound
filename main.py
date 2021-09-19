import pyglet
from morse_sound_generator import MorseSoundGenerator


while True:

    player = pyglet.media.Player()

    morse_input = input("write what you want that to turn into morse sound, for closing the program, write 'endendend'")

    if morse_input == "endendend":
        break
    else:
        morse = MorseSoundGenerator()
        morse_list = morse.morse_list(morse_input)

        player.queue(morse_list)
        player.play()

        pyglet.app.run()
        pyglet.app.exit()

        continue