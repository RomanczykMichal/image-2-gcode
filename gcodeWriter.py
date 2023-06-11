"""
This class contains logic responsible for writing gcode commands to file.
Full command list with explenation you can find here:
https://www.thomasnet.com/articles/custom-manufacturing-fabricating/g-code-commands/
"""

class gcodeWriter: 

    commands = {
        'positioning': 'G0 ',
        'linear_interpolation': 'G1 ',
        'circural_interpolation': 'G2 ',
        'circural_interpolation_couterclockwise': 'G3 ',
        'x': ' X',
        'y': ' Y',
        'z': ' Z',
        'i': ' I', #Used in circular interpolation to define center point from current position
        'j': ' J', #Used in circular interpolation to define center point from current position
        'feed': 'F0 ',
        'units': 'G21 ', #milimeters
        'plane': 'G17 ', #XY plane
        'home': 'G28 ',
        'relative_mode': 'G90 ',
        'end_of_program': 'M30 ',
        'new_line': '\n'
    }
    new_line = '\n'
    gcode = """````
    Hi! This gcode was generated using image-2-gcode python script.
    Credits RomanczykMichal @ github.com
````

"""

    def __init__(self, output_file) -> None:
        self.output_file = output_file
        self.__write_init_line()

    def write_line(self, options):
        for option in options: 
            self.gcode += option
        self.gcode += self.new_line

    def save_file(self):
        self.__write_last_line()
        with open('image.gcode', 'w') as file:
            file.write(self.gcode)
            
    def __write_init_line(self):
        self.gcode += self.commands['units'] + self.commands['plane'] + self.commands['relative_mode'] + self.commands['feed'] + self.commands['home'] + self.new_line

    def __write_last_line(self):
        self.gcode += self.commands['end_of_program']
