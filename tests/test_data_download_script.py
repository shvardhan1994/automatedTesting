import runpy
import os
import shutil

def test_script():

    script_path = os.path.abspath("scripts/download_data.py")    
    runpy.run_path(script_path)

    out_file = os.path.abspath("data/raw/titanic.csv")
    assert os.path.exists(out_file), "File does not exist!"

    shutil.rmtree("data")

    