import bpy
import os

scene = bpy.context.scene
sequence_editor = scene.sequence_editor
area_type = 'SEQUENCE_EDITOR' # change this to use the correct Area Type context you want to process in
areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]

if len(areas) <= 0:
    raise Exception(f"Make sure an Area of type {area_type} is open or visible in your screen!")

with bpy.context.temp_override(
    window=bpy.context.window,
    area=areas[0],
    region=[region for region in areas[0].regions if region.type == 'WINDOW'][0],
    screen=bpy.context.window.screen
):

    def add_clip(file_path):

        # Read current frame and set variable
        current_frame = bpy.context.scene.frame_current
        # Add movie strip to the sequencer
        bpy.ops.sequencer.movie_strip_add(filepath=file_path,frame_start=current_frame)
        # Create a proxy for the given video file.
        # bpy.ops.sequencer.rebuild_proxy()
        # bpy.ops.sequencer.enable_proxies(proxy_25=True, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=True)
        # Set frame to end of clip
        active_strip = sequence_editor.active_strip
        bpy.context.scene.frame_set(active_strip.frame_final_end)


    # Set the directory containing video files
    # the directory should not have bl_proxy folder or it probably won't work
    input_directory = '/Users/evanmann/Desktop/VIDEO_bikepack_nrt_shinleaf/media/video/goproevan/DCIM/100GOPRO/New Folder With Items'

    # Get a sorted list of video files in the directory
    video_files = sorted(file for file in os.listdir(input_directory) if file.endswith('.MP4'))

    # Iterate through each file in alphabetical order
    for file_name in video_files:
        file_path = os.path.join(input_directory, file_name)
        
        # Check if the file is a valid video file
        if os.path.isfile(file_path):
            # Process the file and create a proxy
            add_clip(file_path)

