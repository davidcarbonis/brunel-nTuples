from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'ST_TZ_2L_Kappa_Zct_160905'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'prodLHEtoAOD_ST_TZ_2L_Kappa_Zct.py'
config.JobType.maxMemoryMB = 2500

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC_ST_TZ_2L_Kappa_Zct_160905'

config.Site.storageSite = 'T2_UK_London_Brunel'
config.Site.blacklist = ['T2_CH_CERN','T3_US_Colorado','T2_US_MIT','T2_US_Caltech','T2_IT_Legnaro'] # Turns out the majority of jobs fail when running on these sites
