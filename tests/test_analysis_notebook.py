import subprocess
import os
import shutil

def test_notebook():
    subprocess.check_output(['jupyter', 'nbconvert', '--to', 'notebook', '--execute','notebooks/analyze_data.ipynb'])

    out_file = os.path.abspath('results/survival_rate.jpg')
    assert os.path.exists(out_file), "File does not exist"
    shutil.rmtree("results")