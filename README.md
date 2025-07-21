# multi-sla

PURE SOFTWARE SIDE:
Takes in multiple .stl files of CAD models, runs a slicer, generates two zip folders of .pngs. 
Generates one zip folder (alternating .png images from the zip folders) until one runs out, complete the stack with the rest. 

CONTROL STEPPER MOTORS:
y-axis. 
- set starting y-axis depth.
- set depth height of each layer
- set dist in btw the center of each bath. 

- lower build platform.
- display first image.
- lift build platform.
- wait to let drip? or incorporate rinse station.
- increase the set y-axis depth after every two displays by setting step height
- fully leave bath (raise above the rim).

- slide x-axis to the next to bath.
- lift build platform
- move back. 

CONTROL LCD DISPLAY:
- display images from zip file one by one and wait. 

*For any potential overlap between the models, I assume that the the first CAD model will take precedence. (we can print a ven diagram like test)
