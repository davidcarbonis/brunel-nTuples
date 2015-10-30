from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'ZZ2l2nu_151029'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'
config.JobType.inputFiles = ['pileup_MC_Summer12.root', 'run2012A_13Jul.root', 'run2012B_13Jul.root', 'run2012C_v2.root']

config.Data.inputDataset = '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.publishDataName = 'CRAB3_MC_nTupilisation_ZZ2l2nu_151029'

config.Site.storageSite = 'T2_UK_London_Brunel'

