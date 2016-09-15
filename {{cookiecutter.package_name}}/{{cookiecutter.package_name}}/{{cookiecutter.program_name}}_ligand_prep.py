#!/usr/bin/env python

__author__ = '{{cookiecutter.author_email}}'

from d3r.celppade.custom_ligand_prep import LigandPrep

class {{cookiecutter.lig_prep_class_name}}(LigandPrep):
    """Abstract class defining methods for a custom ligand docking solution
    for CELPP
    """
    def ligand_scientific_prep(self, lig_smi_file, out_lig_file, info_dic={}):
        """Ligand scientific preparation
        :param sci_prepped_lig: Scientifically prepared ligand file
        :returns: This implementation merely returns the value of
        `sci_prepped_lig` in a list
        """
        return super({{cookiecutter.lig_prep_class_name}},
                     self).lig_scientific_prep(sci_prepped_lig)







if ("__main__") == (__name__):
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p", "--pdbdb", metavar = "PATH", help = "PDB DATABANK which we will dock into")
    parser.add_argument("-c", "--challengedata", metavar="PATH", help = "PATH to the unpacked challenge data package")
    parser.add_argument("-o", "--prepdir", metavar = "PATH", help = "PATH to the output directory")
    logger = logging.getLogger()
    logging.basicConfig( format  = '%(asctime)s: %(message)s', datefmt = '%m/%d/%y %I:%M:%S', filename = 'final.log', filemode = 'w', level = logging.INFO )
    opt = parser.parse_args()
    pdb_location = opt.pdbdb
    challenge_data_path = opt.challengedata
    prep_result_path = opt.prepdir

    #running under this dir
    abs_running_dir = os.getcwd()
    log_file_path = os.path.join(abs_running_dir, 'final.log')
    log_file_dest = os.path.join(os.path.abspath(prep_result_path), 'final.log')

    lig_prepper =  {{cookiecutter.lig_prep_class_name}}()
    lig_prepper.run_scientific_ligand_prep(challenge_data_path, pdb_location, prep_result_path)

    #move the final log file to the result dir
    commands.getoutput("mv %s %s"%(log_file_path, prep_result_path))

