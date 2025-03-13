import bpy

def scale_selected_vse_clips(scale_x=1.0, scale_y=1.0):
    # Get the current scene
    scene = bpy.context.scene
    
    # Check if there's a sequence editor
    if not scene.sequence_editor:
        print("No sequence editor found.")
        return
    
    # Iterate through selected strips
    for strip in scene.sequence_editor.sequences:
        if strip.select and hasattr(strip, 'transform'):
            strip.transform.scale_x = scale_x
            strip.transform.scale_y = scale_y
            print(f"Scaled {strip.name} to ({scale_x}, {scale_y})")
    
# Example usage: Change the scale of selected clips to 1.5x in both directions
scale_selected_vse_clips(1.5, 1.5)
