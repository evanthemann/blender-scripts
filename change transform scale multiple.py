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



import bpy

def transform_selected_vse_clips(scale_x=1.0, scale_y=1.0, pos_x=0, pos_y=0):
    """
    Scales and repositions selected VSE clips.
    
    Parameters:
        scale_x (float): Scale in X direction (default = 1.0)
        scale_y (float): Scale in Y direction (default = 1.0)
        pos_x (int): Absolute pixel position on X axis (default = 0)
        pos_y (int): Absolute pixel position on Y axis (default = 0)
    """
    scene = bpy.context.scene
    
    if not scene.sequence_editor:
        print("No sequence editor found.")
        return
    
    for strip in scene.sequence_editor.sequences:
        if strip.select and hasattr(strip, 'transform'):
            # Replace scale and position
            strip.transform.scale_x = scale_x
            strip.transform.scale_y = scale_y
            strip.transform.offset_x = pos_x
            strip.transform.offset_y = pos_y
            print(f"Set {strip.name}: scale=({scale_x}, {scale_y}), pos=({pos_x}, {pos_y})")

# Example usage: Scale to 1.5x and place at X=100px, Y=50px
transform_selected_vse_clips(1.5, 1.5, 100, 50)
