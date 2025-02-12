import bpy 
scene = bpy.context.scene
markers = str(len(scene.timeline_markers))
print("Number of markers: " + markers)
loopNumber = str(len(scene.timeline_markers)/2-1)
print("Loop the Keyboard Maestro macro " + loopNumber + " times.")



# remove markers
import bpy
scene = bpy.context.scene
for marker in scene.timeline_markers:
    scene.timeline_markers.remove(marker)
