import bpy

def recreate_proxies():
    # Get the current scene
    scene = bpy.context.scene
    
    # Check if there's a sequence editor
    if not scene.sequence_editor:
        print("No sequence editor found.")
        return
    
    # Iterate through selected strips
    for strip in scene.sequence_editor.sequences:
        if strip.select and hasattr(strip, 'proxy'):
            strip.proxy.build_25 = True  # Enable 25% proxy
            strip.proxy.build_50 = False
            strip.proxy.build_75 = False
            strip.proxy.build_100 = False
            strip.proxy.use_overwrite = True  # Enable overwrite
            bpy.ops.sequencer.rebuild_proxy()
            print(f"Recreated proxy for {strip.name} at 25% with overwrite enabled")
    
# Run the function
recreate_proxies()
