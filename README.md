# itgrapher
Iterative Transformation Grapher - Python-fu math rendering plugin for GIMP

**Copyright / License**
- (c) Andrew Springman
- GPL 3.0

**Bird's Eye View**
- Grapher because ITGrapher graphs (renders) images of the math entered.
- Transformation because the math entered determines where the point define by each pixel "moves" to.
- Iterative because the transformations are iterated (repeated).
- The distance each point moves in an iteration determines the value of that pixel.  However, what iteration applies to what color and how to calculate the distance is up to you.

**A Little More**
- All python syntax is allowed (ternary expressions etc).  
- If the color layers differ they will blend to create other colors.  If they are the same, the results will be grayscale.
- _Oversample_ averages the value of the 16 points surronding the target pixel in a 4x4 grid.  In essence, it anti-aliases sharp lines.
- _Escape Threshold_ caps the values produced by the transformations.
- _Prep_ will scale the current image to one of the size specified by _Longedge_ (in inches, assuming 300dpi).
- Together, _scale_ and _center_ determine what points each pixel represents.

**Disclaimers**
- Currently this readme is the only manual available.  
- ITGrapher provides no domain protection on your math.  For example, if you divide by zero, it will crash at runtime.  You can usually close the plugin execution and just Re-Show ITGrapher to make adjustments.  Sometimes it will be bad enough that you need to restart GIMP.
- ITGrapher provides no sanitation of Python code entered.  So, don't try to set up a machine as a kiosk that only allows access to GIMP.  It will be completely insecure.
- ITGrapher doesn't do anything to protect against bad or risky programming.  Python syntax errors will make the plugin crash.  You can create infinite loops.  You can run out of memory.  Enjoy your freedom and take responsibility for your own actions.
- ITGrapher doesn't enforce values 0-255 for Red, Green, and Blue.
- ITGrapher doesn't enforce the range of the Red, Green and Blue iteration entries.
- I have no information about version compatibility between GIMP, Python and this plugin. Input appreciated.
- Yes, that's a distance equation as the default velocity parameter.  Think of it as an instantaneous velocity where the iteration is time.

**Installation**
1. Find out where your plugin directories are in GIMP.  In GIMP Preferences, expand Folders and click on Plug-Ins.  This will list the plugin folders.  Choose one.  Remember it.
2. Copy or move itgrapher.py into that directory.
3. If you are in Linux or MacOS, you need to make itgrapher.py executable with "chmod +x itgrapher.py".
4. Restart GIMP and ITGrapher will appear in Filters/Render (assuming you have an image open).

**Getting Started**
- You need to open an image for the ITGrapher plugin to appear.  Find ITGrapher in Filters/Render once you have an image open.
- Work with a small image (like 400x400) and mess around until you find something you like.  It will render faster.  Then either use _Prep_ to make it bigger or just start with a larger image, which will take a very long time...like overnight.
- The first time you use the plugin, just click OK with all default values.
- Make a change to one of the first two parameters.  Any Python syntax is allowed, but get started with just [math] (https://docs.python.org/2/library/math.html).  Click OK again to see how it affected the image.
- Play around with iterations, scale and center and click OK again to see what happens.
- Change the Red, Green and Blue iteration assignments to the same iteration ("iterations" gives you the last iteration).  Click OK and see that the image becomes greyscale.
- Start introducing hard lines to your images with mod (%), thresholds (<) and ternary expressions (which are in the form "x if y or z" in Python), or with floor() or ceil().  
- Clear up the jaggies on your hard lines by turning on Oversample.
- Introduce an escape threshold (something low like 2) and click OK to see what happens.
- For ideas, [see these examples](http://andrewspringman.com/tag/itgrapher/).  The input parameters for each image are included.

**Troubleshooting**
- Crash?  Read the disclaimers above.
- If ITGrapher doesn't appear in Filters/Render, make sure you put it in the right directory, make it executable and restarted GIMP.  See the Installation instructions above.

**Questions / Suggestions**
- Contact me at awspringman AT gmail DOT com
- Participate in the project at [GitHub](https://github.com/andrewspringman/itgrapher)
