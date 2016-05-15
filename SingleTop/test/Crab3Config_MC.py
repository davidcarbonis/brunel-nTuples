from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'tZq_FCNC_Zut_160513'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'

config.Data.inputDataset = '/ST_TZ_3L_Kappa_Zut/kskovpen-kskovpen_ST_TZ_3L_Kappa_Zut_d9e699b508ed3d8a263b49d27c43520e_USER-945eeaf2bbc1c170dee4cc02592a5272/USER'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_MC_nTupilisation_tZq_FCNC_Zut_160513'

config.Site.storageSite = 'T2_UK_London_Brunel'
