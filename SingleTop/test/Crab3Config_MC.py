from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'ttZ_160224'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'
config.JobType.inputFiles = ['pileup_MC_Summer12.root', 'run2012A_13Jul.root', 'run2012B_13Jul.root', 'run2012C_v2.root']

config.Data.inputDataset = '/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_MC_nTupilisation_ttZ_16024'

config.Site.storageSite = 'T2_UK_London_Brunel'

