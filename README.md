cookiecutter-pycustomdock
==============================

cookiecutter-pycstomdock is a [cookiecutter](https://github.com/audreyr/cookiecutter) template to create
Python packages to perform custom docking for Drug Design Data Resource (D3R)
CelppRunner.

This template is based off of the excellent template by Louis Taylor found here:
https://github.com/kragniz/cookiecutter-pypackage-minimal


Usage
-----

    pip install cookiecutter
    cookiecutter https://github.com/drugdata/cookiecutter-pycustomdock.git


Quick and dirty example
-----------------------

Below is a super fast way to try things out. The commands below use all default values for generating the new source tree (named cookiecutter-custom-celpp-contestant)

    pip install cookiecutter
    cookiecutter --no-input https://github.com/drugdata/cookiecutter-pycustomdock.git
    cd cookiecutter-custom-celpp-contestant

    # To test
    python setup.py test

    # To build wheel file for distribution/installation
    python setup.py bdist_wheel

    # To install
    sudo pip install dist/cookiecutter_custom_celpp_contestant-0.1.0-py2-none-any.whl
    
    # Above installs these 3 programs
    custom_celpp_contestant_protein_prep.py
    custom_celpp_contestant_ligand_prep.py
    custom_celpp_contestant_dock.py

  
    

