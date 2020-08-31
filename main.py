##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR6: TRANSFORMATIONS
##  LUIS PEDRO CUÉLLAR - 18220
##


from gl import Render, color
from object import Object, Texture
from shaders import *

render = Render(2048, 2048)


posModel = [1, 1, 1]
render.current_texture = Texture('./textures/moon.bmp')
render.current_shader = phong
render.loadModel('./models/moon.obj', posModel, [.01, .01, .01], [0, 0, 0])
render.glFinish('final.bmp')
print('Terminado')

# render.current_texture = Texture('./textures/moon.bmp')
# render.current_shader = phong
# render.lookAt(posModel, [0, -1.2, -1])
# render.loadModel('./models/moon.obj', posModel, [.0005, .0005, .0005], [1, 1, 10])
# render.glFinish('final.bmp')
# print('Terminado')
#
# render.current_texture = Texture('./textures/moon.bmp')
# render.current_shader = phong
# render.lookAt(posModel, [0, -1.2, -1])
# render.loadModel('./models/moon.obj', posModel, [.0005, .0005, .0005], [1, 1, 10])
# render.glFinish('final.bmp')
# print('Terminado')
#
# render.current_texture = Texture('./textures/moon.bmp')
# render.current_shader = phong
# render.lookAt(posModel, [0, -1.2, -1])
# render.loadModel('./models/moon.obj', posModel, [.0005, .0005, .0005], [1, 1, 10])
# render.glFinish('final.bmp')
# print('Terminado')
