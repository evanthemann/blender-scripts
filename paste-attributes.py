# how to use
# select all clips, and select the source clip last so it's highlighted diffrent
# run the script in blender text editor


import bpy

def copy_all_transform_from_active_to_selected():
    scene = bpy.context.scene

    # Check if there's a sequence editor
    if not scene.sequence_editor:
        print("No sequence editor found.")
        return

    # Get the active strip (reference)
    active_strip = scene.sequence_editor.active_strip
    if not active_strip or not hasattr(active_strip, 'transform'):
        print("No active strip selected or it has no transform.")
        return

    # Get reference values
    ref = active_strip.transform
    ref_crop = active_strip.crop if hasattr(active_strip, 'crop') else None

    ref_data = {
        "scale_x": ref.scale_x,
        "scale_y": ref.scale_y,
        "offset_x": ref.offset_x,
        "offset_y": ref.offset_y,
        "rotation": ref.rotation,
    }

    crop_data = None
    if ref_crop:
        crop_data = {
            "max_x": ref_crop.max_x,
            "max_y": ref_crop.max_y,
            "min_x": ref_crop.min_x,
            "min_y": ref_crop.min_y,
        }

    print(f"📋 Reference {active_strip.name}: {ref_data}")
    if crop_data:
        print(f"📋 Crop: {crop_data}")

    # Apply to all other selected strips
    for strip in scene.sequence_editor.sequences:
        if strip.select and strip != active_strip and hasattr(strip, 'transform'):
            strip.transform.scale_x = ref_data["scale_x"]
            strip.transform.scale_y = ref_data["scale_y"]
            strip.transform.offset_x = ref_data["offset_x"]
            strip.transform.offset_y = ref_data["offset_y"]
            strip.transform.rotation = ref_data["rotation"]

            if crop_data and hasattr(strip, 'crop'):
                strip.crop.max_x = crop_data["max_x"]
                strip.crop.max_y = crop_data["max_y"]
                strip.crop.min_x = crop_data["min_x"]
                strip.crop.min_y = crop_data["min_y"]

            print(f"✅ Applied to {strip.name}")

# Run it
copy_all_transform_from_active_to_selected()
