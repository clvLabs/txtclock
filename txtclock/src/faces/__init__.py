import sys
import importlib
import pathlib

def get(face_name):

    module_name = f"src.faces.{face_name}"

    try:
        tmp_module = __import__(module_name, fromlist=[''])
        importlib.reload(tmp_module)

        try:
            return tmp_module.Face
        except AttributeError:
            # print(f"EXCEPTION: {sys.exc_info()}")
            return None

    except:
        # print(f"EXCEPTION: {sys.exc_info()}")
        return None


