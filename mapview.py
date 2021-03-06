from PySide2.QtWidgets import QGraphicsView


class MapView(QGraphicsView):

    def wheelEvent(self, event):
        super().wheelEvent(event)
        if event.delta() > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(0.8, 0.8)
