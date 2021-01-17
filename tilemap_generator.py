from PIL import Image as im
import numpy as np
from random import randint, choice, random
from io import BytesIO
from errors import InvalidMapDimensionsError, InvalidPercentError
from errors import InvalidIslandSurfaceError, InvalidIslandAreaError
from errors import InvalidBiomAreaError, InvalidBiomNameError
from errors import InvalidBiomPatternNameError, InvalidRgbError

#################################################################
# c_code => colour code (one of the rbg code component)
# area => specific tiles where the island/biom is located on map,
#         (list tuples containing coordinates of single tile)
# surface => number of tiles of island/biom
################################################################


class TileMap:
    """
    Class Tilemap. Contains atributes:
    :rows - number of rows of generated map
    :columns - number of columns of generated map
    :final_surface - total surface of islands which will be generated
    :islands - list of islands generated on map
    :biom_patterns - dictionary containing biom names and their rgb colours
                 these bioms definitions are used to appply bioms on islands
    :water_rgb - water rgb colour code
    :island_rgb - island rgb colour code
    :map - numpy array object representing map
    """

    def __init__(self, n, m, percent):
        if n <= 1 or m <= 1:
            raise InvalidMapDimensionsError()
        if percent < 0 or percent > 100:
            raise InvalidPercentError()
        self.rows = n
        self.columns = m
        percent_converted = percent * 40 / 100  # limits the max % of islands
        self.final_surface = int((percent_converted / 100) * n * m)
        self.islands = []
        self.biom_patterns = {
            'snow': [255, 255, 255],
            'desert': [250, 214, 107],
            'jungle': [22, 71, 11]
        }
        self.water_rgb = [10, 65, 148]
        self.island_rgb = [10, 138, 22]
        self.map = None
        self.min_island_surface = 5
        self.biom_term = 10  # determines on how big island bioms appears

    def initialize_map(self):
        n = self.rows
        m = self.columns
        self.map = np.full((n, m, 3), (tuple(self.water_rgb)))

    def add_biom_pattern(self, name, c_code):
        if type(name) != str:
            raise InvalidBiomPatternNameError()
        if type(c_code) != list or len(c_code) != 3:
            raise InvalidRgbError(c_code)
        if not all((rgb_code >= 0 and rgb_code <= 255) for rgb_code in c_code):
            raise InvalidRgbError(c_code)
        self.biom_patterns[name] = c_code

    def first_tile(self):  # picks a locaton of the first tile of new island
        seek = True
        while seek:
            row = randint(0, self.rows-1)
            column = randint(0, self.columns-1)
            array = self.map[row, column]
            water_term = (list(array) == self.water_rgb)
            if self.separate_islands((row, column)) and water_term:
                seek = False
        return (row, column)

    def calculate_close_neighbours(self, tile):
        row = tile[0]
        column = tile[1]
        neighbours = []
        up = (row - 1, column)
        down = (row + 1, column)
        left = (row, column - 1)
        right = (row, column + 1)
        # adding only these neighbours tiles whisch are in the map boundaries:
        if row != 0:
            neighbours.append(up)
        if row != self.rows-1:
            neighbours.append(down)
        if column != 0:
            neighbours.append(left)
        if column != self.columns-1:
            neighbours.append(right)
        return neighbours

    def calculate_extended_neighbours(self, tile):
        # function returns onyl diagonall neighbours ot the given tile
        row = tile[0]
        column = tile[1]
        extended_neighbours = []
        up_left = (row - 1, column - 1)
        up_right = (row - 1, column + 1)
        bottom_left = (row + 1, column - 1)
        bottom_right = (row + 1, column + 1)
        # adding only these neighbours tiles whisch are in the map boundaries:
        if row != 0 and column != 0:
            extended_neighbours.append(up_left)
        if row != 0 and column != self.columns-1:
            extended_neighbours.append(up_right)
        if row != self.rows - 1 and column != 0:
            extended_neighbours.append(bottom_left)
        if row != self.rows - 1 and column != self.columns - 1:
            extended_neighbours.append(bottom_right)
        return extended_neighbours

    def split_surface_beetwen_islands(self):
        # functions splits total/final islands surface between isands
        surface_left = self.final_surface
        minimal_island_surface = self.min_island_surface
        number_of_islands = 0
        islands_surfaces = []
        islands_surfaces_dict = {}
        while surface_left != 0:
            if surface_left < minimal_island_surface:
                if len(islands_surfaces) == 0:
                    islands_surfaces.append(surface_left)
                    surface_left -= surface_left
                else:
                    islands_surfaces[-1] += surface_left
                    surface_left -= surface_left
            else:
                island_surface = randint(minimal_island_surface, surface_left)
                surface_left -= island_surface
                number_of_islands += 1
                islands_surfaces.append(island_surface)

        # creating dict from sorted islands list
        islands_surfaces.sort(reverse=True)
        for i in range(len(islands_surfaces)):
            islands_surfaces_dict[i+1] = islands_surfaces[i]

        return islands_surfaces_dict

    def create_land(self, surface, first_tile):
        # function responsible for choosing island tiles from map tiles and
        # overwriting map_array cells with colour code of island
        # (applies island on map)

        colour_code = self.island_rgb

        self.map[first_tile[0], first_tile[1]] = np.array(colour_code)
        actual_island_surface = 1
        area = [first_tile]  # contains coordinates of every tile of island
        verified_tiles = [first_tile]  # needed to boost performance

        while actual_island_surface < surface:
            mother_tile = choice(verified_tiles)
            neighbours = self.calculate_close_neighbours(mother_tile)
            for neighbour in neighbours:
                if list(self.map[neighbour]) == colour_code:
                    neighbours.remove(neighbour)
            tile = choice(neighbours)

            c_term = (list(self.map[tile]) == colour_code)
            # (colour_term)is false if choosen tile colour is different
            # than colour of the currently generated island
            # prevents island to grow on itself

            if self.separate_islands(tile) and not c_term:
                self.map[tile] = np.array(colour_code)
                area.append(tile)
                verified_tiles.append(tile)
                actual_island_surface += 1

            if self.useless_tile(mother_tile):
                verified_tiles.remove(mother_tile)
        return area

    def apply_islands_on_map(self):
        # responslbile for adding islands with specyfic surfaces to map
        islands_surfaces = self.split_surface_beetwen_islands()
        for index in islands_surfaces:
            surface = islands_surfaces[index]
            first_tile = self.first_tile()  # generates first tile of island
            area = self.create_land(surface, first_tile)
            percent_map = surface / (self.rows * self.columns)
            percent_is = surface / self.final_surface
            island = Island(surface, area, index, percent_map, percent_is)
            self.islands.append(island)

    def useless_tile(self, tile):
        # returns true is if close neighbours of the given tile
        # are the same colour as the tile
        bool_list = []
        for neighbour in self.calculate_close_neighbours(tile):
            value = (list(self.map[tile]) == list(self.map[neighbour]))
            bool_list.append(value)
        return all(bool_list)

    def separate_islands(self, tile):
        #  functions checks if a neighbourhood of a given tile
        #  is in the area of other island, returns true if isn't
        neighbours = self.calculate_close_neighbours(tile)
        neighbours.extend(self.calculate_extended_neighbours(tile))
        neighbours.append(tile)
        for island in self.islands:
            check = any(tile in island.area for tile in neighbours)
            if check:
                return False
        return True

    def get_island_by_index(self, index):
        for island in self.islands:
            if island.index == index:
                return island

    def delete_island(self, island):
        # deletes island from map
        for tile in island.area:
            self.map[tile] = np.array(self.water_rgb)
        self.islands.remove(island)

    def restore_island(self, island):
        # can restore island and bioms on map if sth overwrite map
        bioms_area = []
        for biom in island.bioms:
            for tile in biom.area:
                self.map[tile] = np.array(biom.c_code)
                bioms_area.append(tile)
        for tile in island.area:
            if tile in bioms_area:
                pass
            else:
                self.map[tile] = np.array(self.island_rgb)

    #########################
    #      BIOM SECTION    #
    ########################

    def apply_biom(self):
        # applies bioms on every island > self.biom_term value
        bioms = self.biom_patterns
        for island in self.islands:
            if island.surface >= self.biom_term:
                name = choice(list(bioms.keys()))  # name of biom to be applied
                c_code = self.biom_patterns[name]  # rgb code attached to name
                surface = int(random() * island.surface)
                first_tile = choice(island.area)
                area = self.create_biom(surface, first_tile, c_code)
                island.bioms.append(Biom(name, area, island.index, c_code))

    def create_biom(self, surface, first_tile, colour_code):
        self.map[first_tile[0], first_tile[1]] = np.array(colour_code)
        actual_biom_surface = 1
        area = [first_tile]
        while actual_biom_surface < surface:
            mother_tile = choice(area)
            neighbours = self.calculate_close_neighbours(mother_tile)
            tile = choice(neighbours)

            water_term = (list(self.map[tile]) == self.water_rgb)
            island_term = (list(self.map[tile]) == self.island_rgb)
            #  water_term True if tile is water
            #  island_term True if tile is island
            if not water_term and island_term:
                self.map[tile] = np.array(colour_code)
                area.append(tile)
                actual_biom_surface += 1
        return area

    def delete_biom(self, island):
        # deletes bioms from given island
        for biom in island.bioms:
            island.bioms.remove(biom)
            for tile in biom.area:
                self.map[tile] = np.array(self.island_rgb)

    def __str__(self):
        # returns basic description about created Tilemap
        text = f'TileMap: {self.rows * self.columns} tiles\n'
        text += f'Total islands surface: {self.final_surface} tiles'
        return text

    def save_image(self, path):
        # saves image on given path
        array = self.map
        map_image = im.fromarray(array.astype(np.uint8))
        map_image.save(path)

    def return_image(self):
        # returns map image as BytesIO
        array = self.map
        buffer = BytesIO()
        map_image = im.fromarray(array.astype(np.uint8))
        map_image.save(buffer, 'png')
        return buffer.getvalue()


class Island:
    """
    Class Island. Contains atributes:
        :index
        :area - tiles of map where the island is located
        :surface - surface of island
        :bioms - list of bioms which are on the island
        :percent_map - percentage of map ocupation by island
        :percent_island - number describing how much of
                          total islands surface is captured by island
    """
    def __init__(self, surface, area, index, percent_map, percent_island):
        if type(surface) != int or surface < 1:
            raise InvalidIslandSurfaceError()
        if area == [] or type(area) != list:
            raise InvalidIslandAreaError()
        self.surface = surface  # size of the island
        self.area = area  # tiles where the island is located on the map
        self.index = index
        self.bioms = []
        self.percent_map = percent_map * 100
        self.percent_island = percent_island * 100

    def description(self):
        # returns detailed description of the island
        text = ''
        if self.index == 1:
            text += f'{"This is the biggest island on map"}\n'
        if self.index == 2:
            text += f'{"This is the second biggest island on map"}\n'
        text += f'Surface of an island is {self.surface} tile/s\n'
        text += f'The island fills {self.percent_map:.2f}% of whole map'
        text += f' and {self.percent_island:.2f}% of all islands\n'

        for biom in self.bioms:
            text += f'There is a biom "{biom.name}" on the island\n'
            text += f'Surface of the biom is {len(biom.area)} tile/s\n'
            percent = len(biom.area)/self.surface * 100
            text += f'The biom takes {percent:.2f}% of the island\n'
        return text

    def __str__(self):
        # returns the index number of island
        return f'Island No. {self.index}'


class Biom:
    """
    Class Biom. Contains atributes:
    :name - name of the biom
    :area - tiles of map where the biom is located
    :island - island on which biom is located
    :c_code - rgb colour code of the biom
    """

    def __init__(self, name, area, island, c_code):
        if type(name) != str:
            raise InvalidBiomNameError()
        if area == [] or type(area) != list:
            raise InvalidBiomAreaError()
        if type(c_code) != list or len(c_code) != 3:
            raise InvalidRgbError(c_code)
        if not all((rgb_code >= 0 and rgb_code <= 255) for rgb_code in c_code):
            raise InvalidRgbError(c_code)
        self.name = name
        self.area = area
        self.island = island
        self.c_code = c_code
