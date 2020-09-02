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

# RACETRACK
# posModel = [0, -0.7, -3]
# render.current_texture = Texture('./textures/racetrack2-2.bmp')
# render.current_shader = phong  
# render.loadModel('./models/race.obj', posModel, [.3, .3, .3], [0, 0, 3])
# render.glFinish('final.bmp')
# print('Terminado')

# MOON
posModel = [-3.5, 3.5, -10]
render.current_texture = Texture('./textures/moon.bmp')
render.current_shader = phong
render.loadModel('./models/moon.obj', posModel, [.01, .01, .01], [0, 0, -5])
render.glFinish('final.bmp')
print('Terminado')

# FERRARI 2017
posModel = [0, -0.7, -2]
render.current_texture = Texture('./textures/formula1.bmp')
render.current_shader = toon
render.loadModel('./models/formula1.obj', posModel, [.005, .005, .005], [0 , 90, 0])
render.glFinish('final.bmp')
print('Terminado')

# # RENAULT
posModel = [1, -0.2, -3]
render.current_texture = Texture('./textures/renault.bmp')
render.current_shader = phong
render.loadModel('./models/renaultF.obj', posModel, [.009, .009, .009], [0, 270, 345])
render.glFinish('final.bmp')
print('Terminado')

# FERRARI 2008
posModel = [-1, -0, -4]
render.current_texture = Texture('./textures/kimi.bmp')
render.current_shader = static  
render.loadModel('./models/kimi.obj', posModel, [.3, .3, .3], [15, 0, 0])
render.glFinish('final.bmp')
print('Terminado')

# JET
posModel = [1, 1.5, -4]
render.current_texture = Texture('./textures/jet.bmp')
render.current_shader = toon  
render.loadModel('./models/jet.obj', posModel, [.03, .03, .03], [0, 90, 90])
render.glFinish('final.bmp')
print('Terminado')