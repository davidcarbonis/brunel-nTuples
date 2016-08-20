from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'tZq_160820'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'

config.Data.inputDataset = '/tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_MC_nTupilisation_tZq_160820'

config.Site.storageSite = 'T2_UK_London_Brunel'

