from tilemap_generator import TileMap, Island, Biom
import numpy as np
import pytest

from errors import InvalidMapDimensionsError, InvalidPercentError
from errors import InvalidIslandSurfaceError, InvalidIslandAreaError
from errors import InvalidBiomAreaError, InvalidBiomNameError
from errors import InvalidBiomPatternNameError, InvalidRgbError


def test_create_map():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    assert mapa.map.shape == (40, 40, 3)
    assert mapa.rows == 40
    assert mapa.columns == 40
    assert mapa.final_surface == 256
    assert mapa.biom_patterns == {
            'snow': [255, 255, 255],
            'desert': [250, 214, 107],
            'jungle': [22, 71, 11]}
    assert mapa.islands == []


def test_change_island_and_water_colour():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.island_rgb = ([22, 123, 45])
    mapa.water_rgb = ([34, 124, 200])
    assert mapa.water_rgb == [34, 124, 200]
    assert mapa.island_rgb == [22, 123, 45]


def test_add_biom_patterns():
    mapa = TileMap(40, 40, 40)
    assert len(mapa.biom_patterns) == 3
    mapa.add_biom_pattern('bagno', [11, 11, 11])
    assert len(mapa.biom_patterns) == 4
    assert mapa.biom_patterns['bagno'] == [11, 11, 11]


def test_first_tile(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()

    def get_tile(t, f):
        return 5
    monkeypatch.setattr('tilemap_generator.randint', get_tile)
    first_tile = mapa.first_tile()
    assert first_tile == (5, 5)
    assert all(c_code in mapa.water_rgb for c_code in mapa.map[(first_tile)])


def test_calculate_close_neighbours():
    mapa = TileMap(40, 40, 40)
    tiles = [(4, 5), (6, 5), (5, 4), (5, 6)]
    assert mapa.calculate_close_neighbours((5, 5)) == tiles


def test_calculate_extended_neighbours():
    mapa = TileMap(40, 40, 40)
    tiles = [(4, 4), (4, 6), (6, 4), (6, 6)]
    assert mapa.calculate_extended_neighbours((5, 5)) == tiles


def test_split_surface_if_surface_is_correct():
    mapa = TileMap(40, 40, 40)
    mapa.min_island_surface = 20
    islands = mapa.split_surface_beetwen_islands()
    total_surface = sum(list(islands.values()))
    assert len(islands) > 0
    assert total_surface == mapa.final_surface
    for island in islands:
        assert islands[island] >= 20


def test_split_surface_min_island_surface_greater_than_total():
    mapa = TileMap(40, 40, 40)
    mapa.min_island_surface = 10000
    islands = mapa.split_surface_beetwen_islands()
    total_surface = sum(list(islands.values()))
    assert len(islands) == 1
    assert total_surface == mapa.final_surface == 256


def test_apply_island_on_map(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()

    def surfaces(f):
        return {1: 175, 2: 8, 3: 56, 4: 17}
    monkeypatch.setattr('tilemap_generator.TileMap.split_surface_beetwen_islands', surfaces)
    mapa.apply_islands_on_map()
    assert len(mapa.islands) == 4
    assert mapa.islands[0].surface == 175
    assert mapa.islands[1].surface == 8
    assert mapa.islands[2].surface == 56
    assert mapa.islands[3].surface == 17

    f = None
    for island in mapa.islands:
        assert island.surface == surfaces(f)[island.index]
        assert island.surface == len(set(island.area))
        rgb = mapa.island_rgb
        for tile in island.area:
            assert all(c_code in rgb for c_code in mapa.map[(tile)])


def test_create_land_correct_colour_code():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    area = mapa.create_land(123, (20, 20))
    assert len(area) == 123
    assert (20, 20) in area
    for tile in area:
        assert all(c_code in mapa.island_rgb for c_code in mapa.map[(tile)])


def test_useless_tile_True():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.map[7, 7] = np.array([10, 138, 22])  # island, central tile
    mapa.map[6, 7] = np.array([10, 138, 22])  # island, up
    mapa.map[8, 7] = np.array([10, 138, 22])  # island, down
    mapa.map[7, 6] = np.array([10, 138, 22])  # island, left
    mapa.map[7, 8] = np.array([10, 138, 22])  # island, right
    assert mapa.useless_tile((7, 7)) is True


def test_useless_tile_False():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.map[7, 7] = np.array([10, 138, 22])  # island, central tile
    mapa.map[6, 7] = np.array([10, 138, 22])  # island, up
    mapa.map[8, 7] = np.array([10, 138, 22])  # island, down
    mapa.map[7, 6] = np.array([10, 138, 22])  # island, left
    mapa.map[7, 8] = np.array([10, 65, 148])  # island, right
    assert mapa.useless_tile((7, 7)) is False


def test_separate_islands(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    island_1 = Island(1, [(20, 20)], 1, 20, 50)
    mapa.islands.append(island_1)

    assert mapa.separate_islands((19, 19)) is False
    assert mapa.separate_islands((19, 20)) is False
    assert mapa.separate_islands((19, 21)) is False
    assert mapa.separate_islands((20, 19)) is False
    assert mapa.separate_islands((20, 21)) is False
    assert mapa.separate_islands((21, 19)) is False
    assert mapa.separate_islands((21, 20)) is False
    assert mapa.separate_islands((21, 21)) is False


def test_get_island_by_index():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.apply_islands_on_map()
    for island in mapa.islands:
        assert island.area == mapa.get_island_by_index(island.index).area


def test_delete_island(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()

    def surfaces(f):
        return {1: 175, 2: 8, 3: 56, 4: 17}
    monkeypatch.setattr('tilemap_generator.TileMap.split_surface_beetwen_islands', surfaces)
    mapa.apply_islands_on_map()
    for island in mapa.islands:
        island_area = island.area
        mapa.delete_island(island)
        for tile in island_area:
            assert all(c_code in mapa.water_rgb for c_code in mapa.map[(tile)])


def test_restore_island():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.apply_islands_on_map()
    island = mapa.islands[0]
    for tile in island.area:
        mapa.map[tile] = np.array([255, 5, 5])
        assert all(c_code in [255, 5, 5] for c_code in mapa.map[tile])
    mapa.restore_island(island)
    for tile in island.area:
        assert not any(c_code in [255, 5, 5] for c_code in mapa.map[tile])


def test_apply_biom(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()

    def surfaces(f):
        return {1: 175, 2: 8, 3: 56, 4: 17}
    monkeypatch.setattr('tilemap_generator.TileMap.split_surface_beetwen_islands', surfaces)

    def my_choice():
        return 0.5
    monkeypatch.setattr('tilemap_generator.random', my_choice)

    mapa.apply_islands_on_map()
    mapa.apply_biom()
    assert len(mapa.get_island_by_index(1).bioms) == 1
    assert len(mapa.get_island_by_index(2).bioms) == 0
    assert len(mapa.get_island_by_index(3).bioms) == 1
    assert len(mapa.get_island_by_index(4).bioms) == 1

    for island in mapa.islands:
        for biom in island.bioms:
            for tile in biom.area:
                assert all(c_code in biom.c_code for c_code in mapa.map[tile])
                assert tile in island.area
            assert len(biom.area) == len(set(biom.area))
            assert len(biom.area) == int(island.surface * 0.5)


def test_create_biom_correct_colour_code():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.apply_islands_on_map()
    island = mapa.islands[0]
    first_tile = island.area[0]
    mapa.create_biom(20, first_tile, [123, 45, 22])
    biom_surface = 0
    for tile in island.area:
        if all(c_code in [123, 45, 22] for c_code in mapa.map[tile]):
            biom_surface += 1
    assert biom_surface == 20


def test_delete_biom(monkeypatch):
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()

    def surfaces(f):
        return {1: 175, 2: 8, 3: 56, 4: 17}
    monkeypatch.setattr('tilemap_generator.TileMap.split_surface_beetwen_islands', surfaces)

    mapa.apply_islands_on_map()
    mapa.apply_biom()
    assert len(mapa.get_island_by_index(1).bioms) == 1
    assert len(mapa.get_island_by_index(2).bioms) == 0
    assert len(mapa.get_island_by_index(3).bioms) == 1
    assert len(mapa.get_island_by_index(4).bioms) == 1

    for island in mapa.islands:
        mapa.delete_biom(island)
        assert len(island.bioms) == 0
        for tile in island.area:
            assert all(c_code in mapa.island_rgb for c_code in mapa.map[tile])


def test_str():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    mapa.apply_islands_on_map()
    text = f'{"TileMap: 1600 tiles"}\n'
    text += f'{"Total islands surface: 256 tiles"}'
    assert str(mapa) == text


def test_return_image():
    mapa = TileMap(40, 40, 40)
    mapa.initialize_map()
    assert type(mapa.return_image()) == bytes


def test_Island_create():
    island = Island(2, [(20, 10), (21, 10)], 1, 0.2, 1)
    assert island.surface == 2
    assert island.area == [(20, 10), (21, 10)]
    assert island.index == 1
    assert island.bioms == []
    assert island.percent_map == 0.2 * 100
    assert island.percent_island == 1 * 100


def test_Island_description():
    biom = Biom('pustynia', [(1, 2)], None, [12, 12, 12])
    island = Island(2, [(20, 10), (21, 10)], 1, 0.2, 1)
    island.bioms.append(biom)

    text = ''
    text += f'{"This is the biggest island on map"}\n'
    text += f'{"Surface of an island is 2 tile/s"}\n'
    text += f'{"The island fills 20.00% of whole map"}'
    text += f'{" and 100.00% of all islands"}\n'
    text += f'There is a biom "pustynia" on the island\n'
    text += f'{"Surface of the biom is 1 tile/s"}\n'
    text += f'{"The biom takes 50.00% of the island"}\n'
    assert text == island.description()


def test_Island_str():
    island = Island(2, [(20, 10), (21, 10)], 1, 0.2, 1)
    assert str(island) == f'{"Island No. 1"}'


def test_Biom_create():
    island = Island(2, [(20, 10), (21, 10)], 1, 0.2, 1)
    biom = Biom('pustynia', [(1, 2)], island, [234, 12, 45])
    assert biom.name == 'pustynia'
    assert biom.area == [(1, 2)]
    assert biom.island == island
    assert biom.c_code == [234, 12, 45]

# ERRORS TESTING


def test_create_map_negative_dimentions():
    with pytest.raises(InvalidMapDimensionsError):
        TileMap(-20, 30, 20)


def test_create_map_negative_density_percent():
    with pytest.raises(InvalidPercentError):
        TileMap(20, 30, -20)


def test_add_biom_pattern_not_str_name():
    mapa = TileMap(20, 30, 20)
    with pytest.raises(InvalidBiomPatternNameError):
        mapa.add_biom_pattern(3, [233, 23, 24])


def test_add_biom_pattern_rbg_colour_code_negative():
    mapa = TileMap(20, 30, 20)
    with pytest.raises(InvalidRgbError):
        mapa.add_biom_pattern('a', [12, -22, 10])


def test_add_biom_pattern_rbg_colour_code_not_list():
    mapa = TileMap(20, 30, 20)
    with pytest.raises(InvalidRgbError):
        mapa.add_biom_pattern('a', (10, 22, 33))


def test_add_biom_pattern_rbg_colour_code_Invalid_component_number():
    mapa = TileMap(20, 30, 20)
    with pytest.raises(InvalidRgbError):
        mapa.add_biom_pattern('a', [12, 10])


def test_create_island_negative_surface():
    with pytest.raises(InvalidIslandSurfaceError):
        Island(-2, [(20, 10), (21, 10)], 1, 0.2, 1)


def test_create_island_surface_not_int():
    with pytest.raises(InvalidIslandSurfaceError):
        Island([20], [(20, 10), (21, 10)], 1, 0.2, 1)


def test_create_island_empty_area():
    with pytest.raises(InvalidIslandAreaError):
        Island(2, [], 1, 0.2, 1)


def test_create_island_area_not_list():
    with pytest.raises(InvalidIslandAreaError):
        Island(2, (20, 32), 1, 0.2, 1)


def test_create_biom_name_not_str():
    with pytest.raises(InvalidBiomNameError):
        Biom(1, [(1, 2)], None, [234, 12, 45])


def test_create_biom_area_not_list():
    with pytest.raises(InvalidBiomAreaError):
        Biom('a', (23, 24), None, [234, 12, 45])


def test_create_biom_area_empty_list():
    with pytest.raises(InvalidBiomAreaError):
        Biom('a', [], None, [234, 12, 45])


def test_create_biom_c_code_negative():
    with pytest.raises(InvalidRgbError):
        Biom('a', [23, 24], None, [-234, 12, 45])


def test_create_biom_c_code_not_list():
    with pytest.raises(InvalidRgbError):
        Biom('a', [23, 24], None, (-234, 12, 45))


def test_create_biom_c_code_list_invalid_components_number():
    with pytest.raises(InvalidRgbError):
        Biom('a', [23, 24], None, [12, 45])
