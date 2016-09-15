#!/usr/bin/env python

__author__ = '{{cookiecutter.author_email}}'


from d3r.celppade.custom_dock import Dock

class {{cookiecutter.dock_class_name}}(Dock):
    """Abstract class defining methods for a custom docking solution
    for CELPP
    """
    Dock.SCI_PREPPED_LIG_SUFFIX = '_prepared.smi'
    Dock.SCI_PREPPED_PROT_SUFFIX = '_prepared.pdb'


    def lig_technical_prep(self, sci_prepped_lig):
        """Technical preparation" is the step immediate preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        :param sci_prepped_lig: Scientifically prepared ligand file
        :returns: This implementation merely returns the value of
        `sci_prepped_lig` in a list
        """
        return super({{cookiecutter.dock_class_name}},
                     self).lig_technical_prep(sci_prepped_lig)

    def receptor_technical_prep(self, sci_prepped_receptor, pocket_center):
        """Technical preparation" is the step immediately preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        """

        # Finally, we return the filenames that will be needed in the
        # docking step. This list is passed to the dock() function as the
        # tech_prepped_receptor_list argument. Here we pass the docking
        # box file (for the docking) and the original scientifically
        # prepped ligand pdb, as that's the easiest way to return the
        # final receptor conformation.
        return super({{cookiecutter.dock_class_name}},
                     self).receptor_technical_prep(sci_prepped_receptor, pocket_center)

    def dock(self, tech_prepped_lig_list, tech_prepped_receptor_list, output_receptor_pdb, output_lig_mol):
        """# The dock step needs to run the actual docking algorithm. Its first two
        # arguments are the return values from the technical preparation
        # functions for the ligand and receptor. The outputs from this
        # step must be two files - a pdb with the filename specified in
        # the output_receptor_pdb argument, and a mol with the filename
        # specified in the output_ligand_mol argument.
        :returns: Always returns False
        """
        return super({{cookiecutter.dock_class_name}},
                     self).dock(tech_prepped_lig_list,
                                tech_prepped_receptor_list,
                                output_receptor_pdb, output_lig_mol)


if ("__main__") == (__name__):
    import os
    import logging
    import shutil
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-l", "--ligsciprepdir", metavar="PATH", help = "PATH where we can find the scientific ligand prep output")
    parser.add_argument("-p", "--protsciprepdir", metavar="PATH", help = "PATH where we can find the scientific protein prep output")
    parser.add_argument("-o", "--outdir", metavar = "PATH", help = "PATH where we will put the docking output")
    # Leave option for custom logging config here
    logger = logging.getLogger()
    logging.basicConfig( format  = '%(asctime)s: %(message)s', datefmt = '%m/%d/%y %I:%M:%S', filename = 'final.log', filemode = 'w', level   = logging.INFO )
    opt = parser.parse_args()
    lig_sci_prep_dir = opt.ligsciprepdir
    prot_sci_prep_dir = opt.protsciprepdir
    dock_dir = opt.outdir
    #running under this dir
    abs_running_dir = os.getcwd()
    log_file_path = os.path.join(abs_running_dir, 'final.log')
    log_file_dest = os.path.join(os.path.abspath(dock_dir), 'final.log')
    docker = {{cookiecutter.dock_class_name}}()
    docker.run_dock(prot_sci_prep_dir,
                    lig_sci_prep_dir,
                    dock_dir)
    #move the final log file to the result dir
    shutil.move(log_file_path, log_file_dest)
