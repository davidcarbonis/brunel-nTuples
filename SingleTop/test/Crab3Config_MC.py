from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 't-chan_5f_MC_150928'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'

config.Data.inputDataset = '/ST_t-channel_5f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/user/almorton/nTuples/t-chan_5f/150928/MC/'

#config.Data.outLFN = '/store/user/<subdir>' # or '/store/group/<subdir>'

config.Data.publication = False
config.Data.publishDataName = 'CRAB3_MC_nTupilisation_t-chan_5f_150928'

config.Site.storageSite = 'T2_UK_London_Brunel'

