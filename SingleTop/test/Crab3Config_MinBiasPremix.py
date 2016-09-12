from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'PileUpPremix_160908b'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SingleNuE10_cfi_GEN_SIM_RECOBEFMIX_DIGIPREMIX_L1_DIGI2RAW_PU.py'
config.JobType.maxMemoryMB = 2500

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter'
config.Data.outputDatasetTag = 'CRAB3_MC_PileUpPremix_160908b'

config.Site.storageSite = 'T2_UK_London_Brunel'
config.Site.blacklist = ['T2_CH_CERN','T3_US_Colorado','T2_US_MIT','T2_US_Caltech','T2_IT_Legnaro'] # Turns out the majority of jobs fail when running on these sites
