from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'tqZ_4flavour_3leptons_ext1'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_cfg.py'
config.JobType.inputFiles = ['pileup_MC_Summer12.root', 'run2012A_13Jul.root', 'run2012B_13Jul.root', 'run2012C_v2.root']

config.Data.inputDataset = '/tZq_4f_3leptons_8TeV-amcatnlo-pythia8_TuneCUETP8M1/Summer12DR53X-PU_S10_START53_V19_ext1-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_MC_nTupilisation_tqZ_ext_160126'

config.Site.storageSite = 'T2_UK_London_Brunel'

