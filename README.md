# blender-scripts

A collection of Python scripts for Blender's Video Sequence Editor (VSE). These are meant to be pasted into Blender's built-in Text Editor and run directly.

## Scripts

### import_videoclip_blender_5_loopdir_getframe_context_add_setplayhead.py

Batch-imports all video clips from a directory into the VSE. Clips are added sequentially starting at the current playhead position, with each clip placed after the previous one ends. Edit the `input_directory` and file extension filter before running.

**Note:** Keep directories to 20 files or fewer to avoid "too many files open" errors.

### change transform scale multiple.py

Two utilities for adjusting transform properties on selected VSE strips:

- `scale_selected_vse_clips` -- sets scale X/Y on all selected strips.
- `transform_selected_vse_clips` -- sets scale and position (offset) on all selected strips.

Edit the values at the bottom of the file before running.

### paste-attributes.py

Copies transform and crop properties from the active strip to all other selected strips. Select all target clips first, then select the source clip last (so it becomes the active strip), then run the script.

### redo proxies.py

Rebuilds 25% proxies for all selected strips with overwrite enabled.

### editmarkers.py

Two small utilities for timeline markers:

- Prints the total number of markers and a loop count for use with Keyboard Maestro.
- Removes all timeline markers from the scene.

### blender import files how to.txt

Brief instructions for using the import script.

## Usage

1. Open Blender and switch to the Text Editor area.
2. Click "New" to create a new text block.
3. Paste in the desired script.
4. Edit any hardcoded paths or values as needed.
5. Run the script (Text > Run Script, or Alt+P).
