#!/usr/bin/env python

__author__ = '{{cookiecutter.author_email}}'


from d3r.celppade.custom_protein_prep import ProteinPrep


class {{cookiecutter.prot_prep_class_name}}(ProteinPrep):
    """Abstract class defining methods for a custom docking solution
    for CELPP
    """
    
    def prepare_protein(self, protein_file, prepared_protein_file, info_dic={}):
        
        return super({{cookiecutter.prot_prep_class_name}},self).prepare_protein(protein_file, prepared_protein_file, info_dic=info_dic)



    
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

    prot_prepper = {{cookiecutter.prep_prep_class_name}}()
    prot_prepper.proteinprep(challenge_data_path, pdb_location, prep_result_path)

    #move the final log file to the result dir
    commands.getoutput("mv %s %s"%(log_file_path, prep_result_path))
