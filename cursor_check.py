import subprocess
import obspython as S
import os

def script_tick(seconds):
    output = subprocess.check_output("./.cursorcheck.sh")
    print(os.getcwd())

    position = output.split(b",")

    scenes = S.obs_frontend_get_scenes()

    if int(position[0])>1920:
        for scene in scenes:
            name = S.obs_source_get_name(scene)
            if "right" in name:
                S.obs_frontend_set_current_scene(scene)
    else:
        for scene in scenes:
            name = S.obs_source_get_name(scene)
            if "left" in name:
                S.obs_frontend_set_current_scene(scene)
    
