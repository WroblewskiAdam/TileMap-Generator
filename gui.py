from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMainWindow, QListWidgetItem, QGraphicsScene
from PySide2.QtGui import QPixmap, QColor
from ui_tilemap import Ui_MainWindow
import sys
from tilemap_generator import TileMap
import numpy as np


class TileMapWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #  SETTING DEAFULT PROGRAM PARAMETERS/ APPEARANCE  #
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.stack.setCurrentIndex(0)
        self.ui.biomButton.hide()
        self.ui.deleteBiomButton.hide()
        self.ui.deleteIslandButton.hide()
        self.ui.biomListLabel.hide()
        self.ui.biomList.hide()
        self.ui.newBiomName.hide()
        self.ui.newBiomNameLabel.hide()
        self.ui.addBiomPatternButton.hide()
        self.ui.deleteBiomPatternButton.hide()
        self.ui.saveButton.hide()
        self.ui.biomTermFrame.hide()
        #  BUTTON CONNECTIONS  #
        self.ui.generateButton.clicked.connect(self._generateMap)
        self.ui.biomButton.clicked.connect(self._addBioms)
        self.ui.deleteBiomButton.clicked.connect(self._deleteBioms)
        self.ui.deleteIslandButton.clicked.connect(self._deleteIsland)
        self.ui.addBiomPatternButton.clicked.connect(self._addBiomPattern)
        self.ui.deleteBiomPatternButton.clicked.connect(self._delBiomPattern)
        self.ui.saveButton.clicked.connect(self._saveFileDialog)
        self.ui.changeWaterRGBButton.clicked.connect(self._changeWaterRGB)
        self.ui.changeIslandRGBButton.clicked.connect(self._changeIslandRGB)
        #  SETTING SLIDERS AND SPINBOX CONNECTIONS
        self.ui.biomSliderRGB1.valueChanged.connect(self._updateBiomRGB1)
        self.ui.biomRBG1.valueChanged.connect(self._updateBiomSlider1)
        self.ui.biomSliderRGB2.valueChanged.connect(self._updateBiomRGB2)
        self.ui.biomRBG2.valueChanged.connect(self._updateBiomSlider2)
        self.ui.biomSliderRGB3.valueChanged.connect(self._updateBiomRGB3)
        self.ui.biomRBG3.valueChanged.connect(self._updateBiomSlider3)
        #  SETTING LIST CONNECTIONS
        self.ui.biomList.itemDoubleClicked.connect(self._delBiomPattern)
        self.ui.biomList.itemClicked.connect(self._choosen_biom_pattern)

        self.ui.islandList.itemClicked.connect(self._selectIsland)
        self.ui.islandList.itemClicked.connect(self._highlightIsland)
        self.ui.islandList.itemDoubleClicked.connect(self._deleteIsland)
        self.ui.highlightCheck.stateChanged.connect(self._unhighlightIsland)

    def _generateMap(self):
        #  BUTTON ACTIONS  #
        self.ui.deleteIslandButton.hide()
        self.ui.biomButton.hide()
        self.ui.deleteBiomButton.hide()
        self.ui.biomButton.blockSignals(False)
        #  CREATING TILEMAP OBJECT  #
        rows = self.ui.height.value()
        columns = self.ui.width.value()
        percent = self.ui.density.value()
        self.my_tilemap = TileMap(rows, columns, percent)
        self.my_tilemap.water_rgb = self._get_water_colour_code()
        self.my_tilemap.island_rgb = self._get_island_colour_code()
        self.my_tilemap.min_island_surface = self.ui.minIslandSurface.value()
        #  GENERATING IMAGE  #
        self.my_tilemap.initialize_map()
        self.my_tilemap.apply_islands_on_map()
        self._updateImage()
        #  OTHER ACTIONS  #
        self._setupIslandsList()
        self.ui.biomListFrame.show()
        self._setupBiomList()
        self.ui.saveButton.show()
        self.ui.biomTermFrame.show()
        self.ui.islandInfo.clear()
        self.ui.mapInfo.setText(str(self.my_tilemap))
        self.ui.biomListLabel.show()
        self.ui.biomList.show()
        self.ui.newBiomName.show()
        self.ui.newBiomNameLabel.show()
        self.ui.addBiomPatternButton.show()
        self.ui.deleteBiomPatternButton.show()

    def _updateImage(self):
        # function generates preview of the map
        self._scene = QGraphicsScene()
        self._scene
        self.ui.islandMap.setScene(self._scene)
        image_data = self.my_tilemap.return_image()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.stack.setCurrentIndex(1)
            self._scene.addPixmap(pixmap)

    def _get_water_colour_code(self):
        # returns water colour code from settings panel
        rgb1 = self.ui.waterRBG1.value()
        rgb2 = self.ui.waterRBG2.value()
        rgb3 = self.ui.waterRBG3.value()
        return [rgb1, rgb2, rgb3]

    def _get_island_colour_code(self):
        # returns island colour code from settings panel
        rgb1 = self.ui.islandRBG1.value()
        rgb2 = self.ui.islandRBG2.value()
        rgb3 = self.ui.islandRBG3.value()
        return [rgb1, rgb2, rgb3]

    def _setupIslandsList(self):
        self.ui.islandList.clear()
        for island in self.my_tilemap.islands:
            item = QListWidgetItem(str(island))
            item.island = island
            self.ui.islandList.addItem(item)
        if len(self.my_tilemap.islands) > 0:
            self.ui.deleteIslandButton.show()
            self.ui.biomButton.show()
        self.selected_island = None

    def _selectIsland(self, item):
        # displays info about selected island
        self.ui.islandInfo.clear()
        self.ui.islandInfo.setText(item.island.description())
        self.selected_island = item.island

    def _deleteIsland(self):
        # deletes island from map
        island = self.selected_island
        if self.selected_island:
            self.my_tilemap.delete_island(island)
            self._updateImage()
            self._setupIslandsList()

    def _highlightIsland(self, item):
        # responsible for highliting selected island on the preview
        if self.ui.highlightCheck.checkState() == 2:
            copy = self.my_tilemap.map.copy()
            for tile in item.island.area:
                self.my_tilemap.map[tile] = np.array([255, 5, 5])
            self._updateImage()
            self.my_tilemap.map = copy

    def _unhighlightIsland(self):
        # returns normal image view
        if self.selected_island:
            island = self.selected_island
            self.my_tilemap.restore_island(island)
            self._updateImage()

    # BIOM FUNCTIONS:
    def _addBioms(self):
        # applyes bioms on islands
        self._deleteBioms()
        self.my_tilemap.biom_term = self.ui.biomTerm.value()
        islands_num = len(self.my_tilemap.islands)
        if len(self.my_tilemap.biom_patterns) > 0 and islands_num > 0:
            self.my_tilemap.apply_biom()
            self._updateImage()
            self.ui.deleteBiomButton.show()
            self.ui.islandInfo.clear()

    def _deleteBioms(self):
        # deletes all the bioms from every islands
        for island in self.my_tilemap.islands:
            self.my_tilemap.delete_biom(island)
        self._updateImage()

    def _setupBiomList(self):
        # creates list of bioms which might be applyed on island in settings
        self.ui.biomList.clear()
        for biom_name in self.my_tilemap.biom_patterns:
            c_code = self.my_tilemap.biom_patterns[biom_name]
            rgb1, rgb2, rgb3 = tuple(c_code)
            item = QListWidgetItem()
            item.setText(biom_name)
            item.setBackground(QColor(rgb1, rgb2, rgb3))
            item.biom_name = biom_name
            self.ui.biomList.addItem(item)
        self.choosen_biom_pattern = None  # required to delete biom pattern

    def _choosen_biom_pattern(self, item):
        #  saves the name of the clicked biom on biom list to variable
        self.choosen_biom_pattern = item.biom_name

    def _addBiomPattern(self):
        # ads biom patter to biom patter list
        rgb1 = self.ui.biomRBG1.value()
        rgb2 = self.ui.biomRBG2.value()
        rgb3 = self.ui.biomRBG3.value()
        c_code = [rgb1, rgb2, rgb3]
        name = self.ui.newBiomName.text()
        self.my_tilemap.add_biom_pattern(name, c_code)
        self._setupBiomList()

    def _delBiomPattern(self):
        # deletes biom pattern from list
        biom = self.choosen_biom_pattern
        self.my_tilemap.biom_patterns.pop(biom)
        self._setupBiomList()

    def _saveFileDialog(self):
        # displays save dialog, acquires file path,
        # and saves the map after clickig save button
        dialog = QFileDialog(self)
        filename = dialog.getSaveFileName(self, 'Save File')
        print(filename)
        path = filename[0]
        self.my_tilemap.save_image(path)

    # SILDERS AND SPINBOX UPDATE FUNCTIONS:
    def _updateBiomRGB1(self, value):
        self.ui.biomRBG1.setValue(value)
        self._updateColourDisplay()

    def _updateBiomSlider1(self, value):
        self.ui.biomSliderRGB1.setValue(value)
        self._updateColourDisplay()

    def _updateBiomRGB2(self, value):
        self.ui.biomRBG2.setValue(value)
        self._updateColourDisplay()

    def _updateBiomSlider2(self, value):
        self.ui.biomSliderRGB2.setValue(value)
        self._updateColourDisplay()

    def _updateBiomRGB3(self, value):
        self.ui.biomRBG3.setValue(value)
        self._updateColourDisplay()

    def _updateBiomSlider3(self, value):
        self.ui.biomSliderRGB3.setValue(value)
        self._updateColourDisplay()

    def _updateColourDisplay(self):
        rgb1 = self.ui.biomRBG1.value()
        rgb2 = self.ui.biomRBG2.value()
        rgb3 = self.ui.biomRBG3.value()
        scene = QGraphicsScene()
        scene.setBackgroundBrush(QColor(rgb1, rgb2, rgb3))
        self.ui.colourDisplay.setScene(scene)

    def _changeWaterRGB(self):
        self.ui.waterRBG1.setValue(self.ui.biomRBG1.value())
        self.ui.waterRBG2.setValue(self.ui.biomRBG2.value())
        self.ui.waterRBG3.setValue(self.ui.biomRBG3.value())

    def _changeIslandRGB(self):
        self.ui.islandRBG1.setValue(self.ui.biomRBG1.value())
        self.ui.islandRBG2.setValue(self.ui.biomRBG2.value())
        self.ui.islandRBG3.setValue(self.ui.biomRBG3.value())


def guiMain(args):
    app = QApplication(args)
    window = TileMapWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
