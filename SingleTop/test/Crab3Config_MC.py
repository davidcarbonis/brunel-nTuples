from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'tqZ_4flavour_3leptons'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_cfg.py'
config.JobType.inputFiles = ['pileup_MC_Summer12.root', 'run2012C_v2.root', 'run2012A_13Jul.root', 'run2012B_13Jul.root']


config.Data.inputDataset = '/tZq_4f_3leptons_8TeV-amcatnlo-pythia8_TuneCUETP8M1/Summer12DR53X-PU_S10_START53_V19-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/nTuples/tqZ_4flavour_3lepton/150817/MC/test' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.publishDataName = 'CRAB3_MC_nTuplisation_tqZ_4flavour_3leptons_170815'

config.Site.storageSite = 'T2_UK_London_Brunel'

