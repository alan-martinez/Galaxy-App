from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    line = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print ("INIT W: " + str(self.width) + " HEIGHT: " + str(self.height))
        self.init_vertical_lines()
    def on_parent(self, widget, parent):
        # print ("ON PARENT W: " + str(self.width) + " HEIGHT: " + str(self.height))
        pass

    def on_size(self, *args):
        # print ("ON SIZE W: " + str(self.width) + " HEIGHT: " + str(self.height))
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
    
    def on_perspective_point_x(self, widget, value):
        # print ("PX :" + str(value))
        pass
        
    def on_perspective_point_y(self, widget, value):
        # print ("PY :" + str(value))
        pass
    
    def init_vertical_lines(self):
        with self.canvas:
            Color (1,1,1)
            self.line = Line(points=[100, 8, 100, 100])
            
    def update_vertical_lines(self):
        center_x = int ( self.width/2 )
        self.line.points = [center_x, 0, center_x, 100]
        
class GalaxyApp(App):
    pass


GalaxyApp().run()