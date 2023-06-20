from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
import warnings
from svg_to_gcode.geometry import Vector


class CustomInterface(interfaces.Gcode):
    def __init__(self):
        super().__init__()
        self.fan_speed = 0

    def linear_move(self, x=None, y=None, z=None, is_start=False):
        if self._next_speed is None:
            raise ValueError(
                "Undefined movement speed. Call set_movement_speed before executing movement commands."
            )

        # Don't do anything if linear move was called without passing a value.
        if x is None and y is None and z is None:
            warnings.warn("linear_move command invoked without arguments.")
            return ""

        # Todo, investigate G0 command and replace movement speeds with G1 (normal speed) and G0 (fast move)
        if is_start:
            command = "G0 Z5\n"
            command += "G0"
        else:
            command = "G1"

        if self._current_speed != self._next_speed:
            self._current_speed = self._next_speed
            command += f" F{self._current_speed}"

        # Move if not 0 and not None
        command += f" X{x:.{self.precision}f}" if x is not None else ""
        command += f" Y{y:.{self.precision}f}" if y is not None else ""
        command += f" Z{z:.{self.precision}f}" if z is not None else ""

        if self.position is not None or (x is not None and y is not None):
            if x is None:
                x = self.position.x

            if y is None:
                y = self.position.y

            self.position = Vector(x, y)

        if is_start:
            command += "\nG0 Z0"

        return command 


class SvgConverter:
    def __init__(self) -> None:
        pass

    def conver_image(self, file_path, save_path):
        gcode_compiler = Compiler(
            CustomInterface, movement_speed=0, cutting_speed=0, pass_depth=0
        )
        curves = parse_file(file_path)
        gcode_compiler.append_curves(curves)
        gcode_compiler.compile_to_file(f'{save_path}/drawing.gcode')
        pass
