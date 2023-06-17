import numpy as np


class Flood:
    """
    Brute-force algorithm which scans rows in order to find firts non-white pixel. Then it continues to search for rest of
    line pixels. We mark top pixel for each column. After the time we found all top pixels of the line we mark that line with
    value of WHITE_THRESHOLD and save those pixels into lines list. We repeat search from the begging, but image now doesn't
    contain line which we found.
    * Note * - Lines should be separeted in order to work correctly. Line clearing method works until it finds white pixel.
    """

    WHITE_THRESHOLD = 200

    def flood_algorithm(self, image):
        lines = []
        line = np.empty(len(image[0]), dtype=object)
        while True:
            found_line = False
            for row_index in range(len(image)):
                for col_index in range(len(image[row_index])):
                    cell_val = image[row_index][col_index]

                    if cell_val < self.WHITE_THRESHOLD and not line[col_index]:
                        line[col_index] = {"x": col_index, "y": row_index}

                    if self.__is_line_finished(line):
                        lines.append(line)
                        image = self.__clear_line_values(line, image)
                        line = np.empty(len(image[0]), dtype=object)
                        found_line = True
                        break
                else:
                    continue
                break
            if not found_line:
                break
        return lines, image

    def __is_line_finished(self, line):
        finished = True
        for cell in line:
            if cell is None:
                finished = False
                break
        return finished

    def __clear_line_values(self, line, image):
        for cell in line:
            col = cell["x"]
            row = cell["y"]
            image[row][col] = self.WHITE_THRESHOLD
            increase = 1
            if row + increase < len(image):
                while image[row + increase][col] < self.WHITE_THRESHOLD:
                    try:
                        image[row + increase][col] = self.WHITE_THRESHOLD
                        increase += 1
                    except:
                        pass
        return image
