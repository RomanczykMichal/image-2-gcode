"""
TODO Pierwsza wersja algorytmu bedzie opierać się na zasadzie powodzi. Można wyobrazić sobie obraz 200x200px, 
     który przedstawia poziome linie wraz z pewnymi przegięciami. Algorytm skanuje pixele od góry, szukając
     pierwszego napotkanego pixela w danej kolumnie. Wszystkie napotkane pixele stanowią jeden 'wiersz' dla
     algorytmu. Algorytm przejdzie tak przez wszyskie wiersze kolumny, aż do jej maksymalnej wysokości. W ten
     sposób uzyskamy zbiór 'wierszy', który następnie zostanie przetłumaczony na komendy gcode.

TODO Wymyślić algorytm przeszukiwania macierzy

"""
import cv2
from algorithms.flood import Flood
from algorithms.cascade import Cascade
from gcodeWriter import GcodeWriter


class GcodeGenerator:
    def __init__(self, file, save, dimensions) -> None:
        self.file = file
        self.is_jpg = str(file).endswith('jpg')
        self.writer = GcodeWriter(save)
        self.dimensions = dimensions.split(";")
        self.lines = []
        self.options = []

    def generate_gcode(self, algorithm):
        self.cv2_image = self.__read_image(self.file)
        self.cv2_image = cv2.flip(self.cv2_image, -1)
        if self.is_jpg:
            self.__find_lines(algorithm)
            self.__optimize_lines()
            self.__generate_gcode_options()
            cv2.imwrite("./images/test.png", self.cv2_image)
            self.writer.save_file()
        else:
            self.__convert_svg()

    def __convert_svg(self):
        pass

    def __find_lines(self, option):  # making room for new algorithms.
        match option:
            case "flood":
                self.lines, self.cv2_image = Flood().flood_algorithm(self.cv2_image)
            case "cascade":
                #self.lines, self.cv2_image = Cascade().cascade_algorithm(self.cv2_image)
                pass
            case "_":
                print("This option doesn't exist.")

    def __optimize_lines(self):
        """
        Method is responsible for optimization of lines. For now it only translates dimensions from pixels to mm.
        TODO optimization of points to plot e.g. if we have straight line there is no need to plot all the points,
             but we can take first and last point between it.
        """
        optimized_lines = []
        height, width = self.cv2_image.shape
        for line in self.lines:
            optimized_line = []
            point = {"x": 0, "y": 0}
            skip_flag = False
            for index in range(len(line) - 2):
                if skip_flag:
                    skip_flag = False
                    continue

                if index == 0:
                    optimized_line.append(
                        {
                            "x": (line[index]["x"] / width) * float(self.dimensions[0]),
                            "y": (line[index]["y"] / height)
                            * float(self.dimensions[1]),
                        }
                    )
                    continue

                if not self.__is_on_the_same_line(
                    line[index], line[index + 1], line[index + 2]
                ):
                    optimized_line.append(
                        {
                            "x": (line[index + 1]["x"] / width)
                            * float(self.dimensions[0]),
                            "y": (line[index + 1]["y"] / height)
                            * float(self.dimensions[1]),
                        }
                    )
                    optimized_line.append(
                        {
                            "x": (line[index + 2]["x"] / width)
                            * float(self.dimensions[0]),
                            "y": (line[index + 2]["y"] / height)
                            * float(self.dimensions[1]),
                        }
                    )
                    skip_flag = True

            optimized_lines.append(optimized_line)
        self.lines = optimized_lines

    def __is_on_the_same_line(self, point_a, point_b, point_c):
        """
        Calculates linear equation from point_a and point_b. Then checks if point_c is on the line
        """
        a = (point_b["y"] - point_a["y"]) / (point_b["x"] - point_a["x"])
        b = point_a["y"] - a * point_a["x"]
        return point_c["y"] == a * point_c["x"] + b

    def __read_image(self, file):
        return cv2.imread(file, flags=cv2.IMREAD_GRAYSCALE)

    def __generate_gcode_options(self):
        """
        Generate gcode for each line.
        Returns:
            List of gcode commands for each line.
        """
        return [self.__generate_gcode_option(line) for line in self.lines]

    def __generate_gcode_option(self, line):
        """
        Generate gcode for one line.
        Arguments:
            line: numpay array of points which reflects line.
        """
        self.writer.lift()
        self.writer.move_to_point(line[0])
        self.writer.lower()
        for point_index in range(1, len(line)):
            self.writer.draw_line(line[point_index])
