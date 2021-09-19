import pyglet


class MorseSoundGenerator:

    def __init__(self):
        self.morse_code_list = {"0": r"morse_codes/0_number_morse_code.mp3",
                                "1": r"morse_codes/1_number_morse_code.mp3",
                                "2": r"morse_codes/2_number_morse_code.mp3",
                                "3": r"morse_codes/3_number_morse_code.mp3",
                                "4": r"morse_codes/4_number_morse_code.mp3",
                                "5": r"morse_codes/5_number_morse_code.mp3",
                                "6": r"morse_codes/6_number_morse_code.mp3",
                                "7": r"morse_codes/7_number_morse_code.mp3",
                                "8": r"morse_codes/8_number_morse_code.mp3",
                                "9": r"morse_codes/9_number_morse_code.mp3",
                                "A": r"morse_codes/A_morse_code.mp3",
                                "B": r"morse_codes/A_morse_code.mp3",
                                "C": r"morse_codes/A_morse_code.mp3",
                                "D": r"morse_codes/B_morse_code.mp3",
                                "E": r"morse_codes/A_morse_code.mp3",
                                "F": r"morse_codes/A_morse_code.mp3",
                                "G": r"morse_codes/A_morse_code.mp3",
                                "H": r"morse_codes/A_morse_code.mp3",
                                "I": r"morse_codes/A_morse_code.mp3",
                                "J": r"morse_codes/A_morse_code.mp3",
                                "K": r"morse_codes/A_morse_code.mp3",
                                "L": r"morse_codes/A_morse_code.mp3",
                                "M": r"morse_codes/A_morse_code.mp3",
                                "N": r"morse_codes/A_morse_code.mp3",
                                "O": r"morse_codes/A_morse_code.mp3",
                                "P": r"morse_codes/A_morse_code.mp3",
                                "Q": r"morse_codes/A_morse_code.mp3",
                                "R": r"morse_codes/A_morse_code.mp3",
                                "S": r"morse_codes/A_morse_code.mp3",
                                "T": r"morse_codes/A_morse_code.mp3",
                                "U": r"morse_codes/A_morse_code.mp3",
                                "V": r"morse_codes/A_morse_code.mp3",
                                "W": r"morse_codes/A_morse_code.mp3",
                                "X": r"morse_codes/A_morse_code.mp3",
                                "Y": r"morse_codes/A_morse_code.mp3",
                                "Z": r"morse_codes/A_morse_code.mp3",
                                " ": r"morse_codes/Silent.wav"
                                }

    def morse_list(self, subtext):

        char_list = [char.upper() for char in subtext]
        sound_list = []

        for char in char_list:
            try:
                if char != " ":
                    char_sound_file = pyglet.resource.media(f"morse_codes/{char}_morse_code.mp3", streaming=False)
                    sound_list.append(char_sound_file)
                else:
                    char_sound_file = pyglet.resource.media(f"morse_codes/Silent.wav", streaming=False)
                    sound_list.append(char_sound_file)
            except:
                pass

        return sound_list
