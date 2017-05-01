### Kaleid
---
Kaleid is a 2D visual feedback loop. Originally created by workSPACE for mobile devices:
https://play.google.com/store/apps/details?id=com.workSPACE.Fraksl&hl=en_GB

This project is not associated with the original project by workSPACE, but instead my own implementation of the presented effect. 
The current aim for this project is to enable external manipulation of the pattern using audio to produce an audio visualiser.

---
##Construction
Currently, the project is written in Python, using the PyGame as a front-end to display the visuals. This implementation is successful and produces the desired effect, However, a complete re-write is planned to reimplement the entire project using OpenGL or Vulkan. By directly addressing a graphics library, the project can benefit from features such as anti-aliasing and motion blur. 

The current implementation makes use of several renderig surfaces in PyGame; A base surface A, which contains a small surface C, there is an additional surface B, which is directly adjacent to surface A, which projects the contents of A, flipped allong the vertical axis. The rendering surface D (Display Output) is captured, each pixel is inverted (black to white & white to black) and then rendered onto Surface C. When surface D is rendered, it creates a feedback loop, similar to pointing a camera at it's own live display output. As this is performed in software, it can be represented without loss of quality. By mirroring one side of the screen onto another, the feedback loop will produce a fractal-like pattern on the screen.

---
### Requirements
### BEFORE RUNNING THIS PROJECT PLEASE READ:
The isplay output of this application produces very fast flashing scenes on the screen. This application therefore presents a very real threat of an Epilepsy trigger. Additionally, it can also produce headaches and other eye strain issues. Even if you don't have Epilepsy, i'd still be careful spending long periods of time staring at it. Your soul might get sucked into it or something scary.

This project requires Python 2.7 and PyGame (Whatever version supports P2.7, Can't remember right now)
Simply put on sunglasses, run the project with the required dependancies present and all should be good.
