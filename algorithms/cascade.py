class Cascade:
    """
    Algorithm search first column until it finds first line. Then we proceed with searching in right direction. Algorithm
    checks all pixels to the top, top-right, right, bottom-right, bottom from place where it is currently. Then it goes to the
    most top one. Imagine

            W W W W W
            W W B B B
            S C B B W
            B B B W W (W - white pixel
                       B - black pixel
                       S - already searched
                       C - current pixel)

    In case described above algorithm have 3 options: top-right, right, bottom-right. It will chose top-right, because it is 
    higher than other pixels.           
    """

    WHITE_THRESHOLD = 200

    def cascade_algorithm(self, image):
        pass