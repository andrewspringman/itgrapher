#!/usr/bin/env python
#This software is licensed under the CC-GNU GPL.  See http://creativecommons.org/licenses/GPL/3.0/
#Under Windows, put me in the lib/gimp/2.0/plug-ins directory under your GIMP installation.
#Under Linux: put me in ~/.Gimp-2.4/plugins

from gimpfu import *

def python_itgrapher(image,            
                     drawable,         
                     x_equation,       
                     y_equation,  
                     z_equation,       
                     t_equation,
                     starting_z,       
                     starting_t,
                     velocity_equation,
                     iterations,       
                     scale,            
                     red_iteration,    
                     green_iteration,  
                     blue_iteration,
                     luminosity,                     
                     red_value_equation,
                     green_value_equation,
                     blue_value_equation,
                     center,
#                     use_mpmath,
                     oversample,
                     escape_threshold,
                     prep,
                     long_edge):
  exec("\
#if use_mpmath:\n\
#  from mpmath import *\n\
#else:\n\
from math import *\n\
fscale = eval(scale)\n\
if prep:\n\
  #resize image so that longest edge is becomes specified long_edge in inches\n\
  bigger = drawable.width if (drawable.width > drawable.height) else drawable.height\n\
  ratio = (long_edge * 300) / bigger\n\
  pdb.gimp_image_resize(image,(drawable.width * ratio),(drawable.height * ratio),0,0)\n\
  pdb.gimp_layer_resize_to_image_size(drawable)\n\
  fscale = fscale / ratio\n\
width = drawable.width\n\
height = drawable.height\n\
half_width = width/2\n\
half_height = height/2\n\
tile_width = gimp.tile_width()\n\
tile_height = gimp.tile_height()\n\
tiles_x = (width+tile_width-1)/tile_width\n\
tiles_y = (height+tile_height-1)/tile_height\n\
\n\
x_center, y_center = " + center + "\n\
\n\
for tile_x in range(tiles_x):\n\
  for tile_y in range(tiles_y):\n\
    tile = drawable.get_tile(0, tile_y, tile_x)\n\
    this_tile_width  = tile.ewidth\n\
    this_tile_height = tile.eheight\n\
    for in_tile_x in range(this_tile_width):\n\
      for in_tile_y in range(this_tile_height):\n\
        image_x = tile_x * tile_width + in_tile_x\n\
        image_y = tile_y * tile_height + in_tile_y\n\
        if oversample:\n\
            red = 0\n\
            green = 0\n\
            blue = 0\n\
            for k in range(4):\n\
                for l in range(4):\n\
                    x = (((float(image_x) - half_width ) * fscale) + x_center) + ((fscale/4) * (k-1.5))\n\
                    y = ((((float(image_y) - half_height) * fscale) + y_center) * (-1)) + ((fscale/4) * (l-1.5))\n\
                    z = " + starting_z + "\n\
                    t = " + starting_t + "\n\
                    for i in range(iterations):\n\
                      old_x = x\n\
                      old_y = y\n\
                      old_z = z\n\
                      old_t = t\n\
                      new_x = (" + x_equation + ")\n\
                      new_y = (" + y_equation + ")\n\
                      new_z = (" + z_equation + ")\n\
                      new_t = (" + t_equation + ")\n\
                      x     = new_x\n\
                      y     = new_y\n\
                      z     = new_z\n\
                      t     = new_t\n\
                      if (escape_threshold == 0):\n\
                        escape = 0\n\
                      else:\n\
                        escape = (abs(x) > escape_threshold or abs(y) > escape_threshold) \n\
                      if i+1 == (" + red_iteration + ") or i+1 == (" + green_iteration + ") or i+1 == (" + blue_iteration + ") or escape:\n\
                        velocity = (" + velocity_equation + ")\n\
                        if i+1 == (" + red_iteration + ") or (escape and i+1 < (" + red_iteration + ")):\n\
                          red += (" + red_value_equation + ")\n\
                        if i+1 == (" + green_iteration + ") or (escape and i+1 < (" + green_iteration + ")):\n\
                          green += (" + green_value_equation + ")\n\
                        if i+1 == (" + blue_iteration + ") or (escape and i+1 < (" + blue_iteration + ")):\n\
                          blue += (" + blue_value_equation + ")\n\
                      if escape:\n\
                        break\n\
            red /= 16\n\
            green /= 16\n\
            blue /= 16\n\
            red = int(red)\n\
            green = int(green)\n\
            blue = int(blue)\n\
        else:\n\
            x = ((float(image_x) - half_width ) * fscale) + x_center\n\
            y = (((float(image_y) - half_height) * fscale) + y_center) * (-1)\n\
            z = " + starting_z + "\n\
            t = " + starting_t + "\n\
            for i in range(iterations):\n\
              old_x = x\n\
              old_y = y\n\
              old_z = z\n\
              old_t = t\n\
              new_x = (" + x_equation + ")\n\
              new_y = (" + y_equation + ")\n\
              new_z = (" + z_equation + ")\n\
              new_t = (" + t_equation + ")\n\
              x     = new_x\n\
              y     = new_y\n\
              z     = new_z\n\
              t     = new_t\n\
              if (escape_threshold == 0):\n\
                escape = 0\n\
              else:\n\
                escape = (abs(x) > escape_threshold or abs(y) > escape_threshold) \n\
              if i+1 == (" + red_iteration + ") or i+1 == (" + green_iteration + ") or i+1 == (" + blue_iteration + ") or escape:\n\
                velocity = (" + velocity_equation + ")\n\
                if i+1 == (" + red_iteration + ") or (escape and i+1 < (" + red_iteration + ")):\n\
                  red = int((" + red_value_equation + "))\n\
                if i+1 == (" + green_iteration + ") or (escape and i+1 < (" + green_iteration + ")):\n\
                  green = int((" + green_value_equation + "))\n\
                if i+1 == (" + blue_iteration + ") or (escape and i+1 < (" + blue_iteration + ")):\n\
                  blue = int((" + blue_value_equation + "))\n\
              if escape:\n\
                break\n\
        tile[in_tile_x, in_tile_y] = chr(red) + chr(green) + chr(blue)\n\
    gimp.progress_update((float(tile_x*tiles_x+tile_y)+1)/(tiles_y*tiles_x*2+1))\n\
tile.flush()\n\
gimp.progress_update(0.80)\n\
image.flatten()\n\
gimp.progress_update(1.0)\n\
")
  
register( 
  "python_fu_itgrapher", 
  "Iterative Transformation Grapher", 
  "Iterative Transformation Grapher", 
  "Andrew Springman", 
  "Andrew Springman / CC-GNU GPL.  See http://creativecommons.org/licenses/GPL/2.0/", 
  "2008-2010", 
  "<Image>/Filters/Render/_ITGrapher...", 
  "RGB*", 
  [
    (PF_STRING , "x_equation"           , "x <--"           , "x**2-y**2-1"                                        ),
    (PF_STRING , "y_equation"           , "y <--"           , "2*x*y"                                              ),
    (PF_STRING , "z_equation"           , "z <--"           , "0"                                                  ),
    (PF_STRING , "t_equation"           , "t <--"           , "0"                                                  ),
    (PF_STRING , "starting_z"           , "z"               , "0"                                                  ),
    (PF_STRING , "starting_t"           , "t"               , "0"                                                  ),
    (PF_STRING , "velocity_equation"    , "velocity <--"    , "sqrt(abs((x - old_x)**2 + (y - old_y)**2 + (z - old_z)**2 + (t - old_t)**2))" ),
    (PF_INT    , "iterations"           , "iterations"      , 4                                                    ),
    (PF_STRING , "scale"                , "scale"           , "0.025"                                              ),
    (PF_STRING , "red_iteration"        , "red iteration"   , "iterations"                                         ),
    (PF_STRING , "green_iteration"      , "green iteration" , "iterations-1"                                       ),
    (PF_STRING , "blue_iteration"       , "blue iteration"  , "iterations-2"                                       ),
    (PF_FLOAT  , "luminosity"           , "luminosity"      , 1                                                    ),    
    (PF_STRING , "red_value_equation"   , "red value <--"   , "((velocity + 256)/(velocity / luminosity + 1)) - 1" ),
    (PF_STRING , "green_value_equation" , "green value <--" , "((velocity + 256)/(velocity / luminosity + 1)) - 1" ),
    (PF_STRING , "blue_value_equation"  , "blue value <--"  , "((velocity + 256)/(velocity / luminosity + 1)) - 1" ),
    (PF_STRING , "center"               , "center"          , "0,0"                                                ),
#    (PF_BOOL   , "use_mpmath"           , "use mpmath"      , 0                                                    ),
    (PF_BOOL   , "oversample"           , "oversample"      , 0                                                    ),
    (PF_FLOAT  , "escape_threshold"     , "escape threshold (0 for disabled)", 0                                   ),
    (PF_BOOL   , "prep"                 , "prep"            , 0                                                    ),
    (PF_FLOAT  , "long_edge"            , "long_edge"       , 10                                                   )    
  ], 
  [], 
  python_itgrapher)

main()

