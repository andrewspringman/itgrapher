# itgrapher
Iterative Transformation Grapher - Python-fu math rendering plugin for GIMP

**Copyright / License**
- (c) 2010-2017 Andrew Springman
- GPL 3.0

**Bird's Eye View**
- Grapher because ITGrapher graphs (renders) images of the math entered.
- Transformation because the math entered determines where the points defined by each pixel "moves" to.
- Iterative because the transformations are iterated (repeated).
- The distance each point moves in an iteration determines the value of that pixel.  However, what iteration applies to what color and how to calculate the distance is up to you.

**A Little More**
- All python syntax is allowed (ternary expressions etc) in parameter fields that allow math.  Other fields allow just numbers. 
- If the color layers differ they will blend to create other colors.  If they are the same, the results will be grayscale.
- _oversample_ averages the value of the 16 points surrounding the target pixel in a 4x4 grid.  In essence, it anti-aliases sharp lines.
- _escape threshold_ caps the values produced by the transformations.
- _prep_ will scale the current image to the size specified by _longedge_ (in inches, assuming 300dpi).
- Together, _scale_ and _center_ determine what points in the XY plane each pixel represents.

**Disclaimers**
- Currently this readme is the only manual available.  
- ITGrapher provides no domain protection for your math.  For example, if you divide by zero, it will crash at runtime.  You can usually close the plugin execution and just Re-Show ITGrapher to make adjustments.  Sometimes it will be bad enough that you need to restart GIMP.
- ITGrapher provides no sanitation of Python code entered.  So, don't try to set up a machine as a kiosk that only allows access to GIMP.  It will be completely insecure.
- ITGrapher doesn't do anything to protect against bad or risky programming.  Python syntax errors will make the plugin crash.  You can create infinite loops.  You can run out of memory.  Enjoy your freedom and take responsibility for your own actions.
- ITGrapher doesn't enforce values 0-255 for Red, Green, and Blue.  Why?  For speed.  (It will convert to INT).
- ITGrapher doesn't enforce the range of the Red, Green and Blue iteration entries.  Nor does it convert to INT.
- I have no information about version compatibility between GIMP, Python and this plugin. Input appreciated.
- Yes, that's a distance equation as the default velocity parameter.  Think of it as an instantaneous velocity where the iteration is time.

**Installation**
1. Find out where your plugin directories are in GIMP.  Here's how.  In GIMP Preferences, expand Folders and click on Plug-Ins.  This will list the plugin folders.  Choose one.  Remember it.
2. Copy or move itgrapher.py into that directory.
3. If you are in Linux or MacOS, you need to make itgrapher.py executable with "chmod +x itgrapher.py".
4. Restart GIMP and ITGrapher will appear in Filters/Render (assuming you have an image open).

**Getting Started**

Here are a few tips to get the hang of using ITGrapher.

- You need to open or create a new image for the ITGrapher plugin to appear.  Find ITGrapher in Filters/Render once you have an image open.
- Work with a small image (like 400x400) and mess around until you find something you like.  It will render faster.  Then either use _prep_ to make it bigger or just start with a larger image, which potentially will take a very long time...like overnight for full size images for print.
- The first time you use the plugin, just click OK with all default values.
- Make a change to one of the first two parameters.  Any Python syntax is allowed, but get started with just [math](https://docs.python.org/2/library/math.html).  Click OK again to see how it affected the image.
- Play around with iterations, scale and center and click OK again to see what happens.
- Change the Red, Green and Blue iteration assignments to the same iteration ("iterations" gives you the last iteration).  Click OK and see that the image becomes greyscale.
- Start introducing hard lines to your images with mod (%), thresholds (<) and ternary expressions (which are in the form "x if y or z" in Python), or with floor() or ceil().  
- Clear up the jaggies on your hard lines by turning on _oversample_.
- Introduce an _escape threshold_ (something low, like 2) and click OK to see what happens.
- For more ideas, [see these examples](http://andrewspringman.com/tag/itgrapher/).  The input parameters for each image are included.

**Troubleshooting**
- Crash?  Read the disclaimers above.
- If ITGrapher doesn't appear in Filters/Render, make sure you put it in the right directory, made it executable, and restarted GIMP.  See the Installation instructions above.
Also check to see if any of the default Python-fu plugins are working.
If not, you may have a problem with your GIMP or Python installation.
Filters/Render/Clouds/Fog is such a plugin.

**Questions / Suggestions**
- Contact me at awspringman AT gmail DOT com
- Participate in the project at [GitHub](https://github.com/andrewspringman/itgrapher)

**Parameters**
- _x equation_, _y equation_, _z equation_ and _t equation_ are Python code strings intended to define the new value of x, y, z, and t for each iteration.  That is, they define the transformation.  Note that only x and y correspond to actually pixels in the image.  So, the user needs to define starting points for z and t in the next two parameters.  (If you are trying to render the Mandelbrot set, set the z and t equations to simply z and t respectively.  This will act as C in Z^2+C).
- _starting z_ and _starting t_ define the initial values of z and t respectively.  Any Python code is allowed.  (For the Mandelbrot set, set them to x and y respectively for C in Z^2+C).
- _velocity equation_ is calculated for every point in the image for each iteration.  Any Python code is allowed.  Note the use of old_x, old_y, old_z, and old_t.  These are the values for the previous iteration (or, in the case of the first iteration, the starting values defined by the image, scale and center or starting_z and starting_t).
By the time this code is evaluated, x, y, z, and t have already be transformed.
- _iterations_ is the number of times to iterate the transformation.  It must be an positive integer to work.
scale is the size of each pixel.  A small scale zooms in.  A large scale zooms out.  Any Python code is allowed and the result is interpreted as a floating point number.
- _red_iteration_, _green iteration_, and _blue iteration_ determine which iteration is used to determine the values for each color.  Iterations are numbered starting with 1 and go up to the value entered in _iterations_.  There is no point in setting _iterations_ to something lower than the highest of these three.  It will just be doing extra calculations it never uses.  Making these three the same produces greyscale images.  Otherwise the three colors blend to give other colors in the standard RGB scheme.  Any Python code is allowed, but the result must be an INT.
- _luminosity_ is just a floating point constant available in the value calculations.  By default it makes the image lighter as it goes up and darker as it goes down.  No code is allowed here.
- _red value_, _green value_, and _blue value_ are Python code strings that are intended to convert the velocity into a 0-255 value.  Conversion to INT is done for you.  You can, however, put anything you want here.
- _center_ is an x,y pair determining what point in the XY plane is represented by the center of the image.  It must be floating point numbers separated by a comma.  No code is allowed.
- If selected, _oversample_ calculates the values for the 16 points around the current point in a 4x4 grid and uses the average for the point.  Use this to smooth hard edges.  Not so good for exactly horitontal or vertical lines.
- _escape threshold_ is the maximum number allowed by each transformation calculation.  The calculation is done first and then this limit is applied.  Set to 0 if you don't want to set a threshold.  This must be a floating point number.  No code is allowed.
- if selected, _prep_ resizes the image to be 300 pixels along the longest edge times the value provided in _longedge_.
- _longedge_ is the size in inches at 300dpi that _prep_ should scale the longest edge of the image to.  It will maintain the aspect ratio. This is a floating point number.  No code is allowed.

**Variables**
- _x_, _y_, _z_, and _t_ contain different things at different times.  When _x equation <--_ etc are evaluated, they contain the previous interations values.  They contain new values by the time _velocity equation_ is evaluated.
- Use _old_x_ etc for the previous values in _velocity equation_.
- _luminosity_ is just a user-provided floating point constant.  Use it anywhere Python code is allowed.  By default, it will lighten and darken the image with higher and lower values, respectively.
- _i_ contains the number of the current iteration (starting with 1).  It is useful for causing the transformations to change at different iterations, but can be used anywhere Python code is allowed, except the _starting t_ and _starting z_ parameters.

**Note: I've never used the following variables in parameters, but they should be available everywhere Python code is allowed.**
- _width_ and _height_ are the size of the image in pixels.
- _x_center_ and _y_center_ are the x and y values of the center parameter.
