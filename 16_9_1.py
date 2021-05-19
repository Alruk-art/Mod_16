print ('\t Задание 16_9_1')
class Figure:
    def __init__(self, height, width):
        self.x = height
        self.y = width
    def get_tip_fig(self):
        if self.x == self.y: fig = 'square'
        else:
            fig = 'rectangle'
        return fig
    def par_fig(self):
        xx = self.x
        yy = self.y
        return xx,yy

fig_1 = Figure(50,50)
fig_2 = Figure(6,7)

print (fig_1.get_tip_fig(),fig_1.par_fig())
print (fig_2.get_tip_fig(),fig_2.par_fig())