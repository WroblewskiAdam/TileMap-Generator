

class InvalidMapDimensionsError(Exception):
    def __init__(self):
        super().__init__('Map dimentions cannot be less than 1!')


class InvalidPercentError(Exception):
    def __init__(self):
        super().__init__('Percent cannot be negative or greater than 100!')


class InvalidIslandSurfaceError(Exception):
    def __init__(self):
        super().__init__('Surface of created island cannot be less than 1!')


class InvalidIslandAreaError(Exception):
    def __init__(self):
        super().__init__('Creation of island without area is impossible!')


class InvalidBiomAreaError(Exception):
    def __init__(self):
        super().__init__('Creation of biom without area is impossible!')


class InvalidBiomNameError(Exception):
    def __init__(self):
        super().__init__('Given biom name is not text!')


class InvalidBiomPatternNameError(Exception):
    def __init__(self):
        super().__init__('Given biom pattern name is not text!')


class InvalidRgbError(Exception):
    def __init__(self, c_code):
        text = (f'Rgb colour code must be list of 3 numbers\n'
                f'0 <= each number <= 255,\ngiven colour code: {c_code}')
        super().__init__(text)
