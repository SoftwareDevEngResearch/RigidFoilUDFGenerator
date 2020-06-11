from RigidFoilSimer import Parameters, talkToAnsys, CFile_Generation, processWallshear
import sys
import shutil

def yesNo(prompt):
    if Parameters.query_yes_no(prompt) == False:
        sys.exit("Done.")

def main(FilePath, FoilGeo, FoilDyn):
    """Runs simulation from reading in input form to processing end data"""
  
    ## Generate C File
    FilePath = CFile_Generation.genCFile(FilePath, FoilGeo, FoilDyn)

    ## Generate Mesh Files
    talkToAnsys.generateMesh_wbjn(FilePath, FilePath.wbjnMesh_path, FoilGeo)
    yesNo("Generate project file and mesh file?")
    talkToAnsys.run_wbjn(FilePath.WB_path, FilePath.wbjnMesh_path, '-B')

    ## Generate Fluent Files
    yesNo("Project with Mesh file has been generated. Begin simulation? (This will take a long time)")
    talkToAnsys.generateFluent_wbjn(folder_path, project_path, wbjnFluent_path, FoilDyn)
    # talkToAnsys.run_wbjn(WB_path, wbjnFluent_path, '-B')

    # ## Process Wall shear data
    # processWallshear.processWallshear.process_wallshear_data(FilePath.FFF_path, FoilDyn)
