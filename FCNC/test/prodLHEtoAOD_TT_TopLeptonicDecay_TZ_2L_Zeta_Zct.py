# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: FCNCProd/FastSim/Hadronizer_TTbar_ZToLL_cfi.py --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --filein root://sbgse1.in2p3.fr//store/user/kskovpen/FCNCProdv2/LHE/TT_topLeptonicDecay_zeta_zct_LO/0.lhe --filetype LHE --era Run2_2016 --fast -n 10 --eventcontent AODSIM --datatier AODSIM -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 --pileup_input dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput  --beamspot Realistic25ns13TeV2016Collision --python_filename prodLHEtoAOD_TT_TopLeptonicDecay_TZ_2L_Zeta_Zct.py --datamix PreMix --fileout aod.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('root://sbgse1.in2p3.fr//store/user/kskovpen/FCNCProdv2/LHE/TT_topLeptonicDecay_zeta_zct_LO/0.lhe'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('FCNCProd/FastSim/Hadronizer_TTbar_ZToLL_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('aod.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/007F9F8A-EB14-E611-9918-00259075D72C.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00A7A158-4E14-E611-A2E5-0025905B858E.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00B28D0D-A214-E611-A9FA-0025904C4E28.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00C7136F-8714-E611-9DD4-0025905B8564.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00ECAC4F-5714-E611-ACAC-0CC47A4D76D0.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02053F47-7B14-E611-904C-0025905C53D0.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/020ACED3-8C14-E611-9F4D-0025905B85DC.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0259F967-6915-E611-8908-00304867FE4B.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02600760-4E14-E611-B7D9-0025905B8592.root', '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/027EC271-7714-E611-971C-0025905C5502.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_miniAODv2_v1', '')

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.AODSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.DataMixingModule.customiseForPremixingInput
from SimGeneral.DataMixingModule.customiseForPremixingInput import customiseForPreMixingInput 

#call to customisation function customiseForPreMixingInput imported from SimGeneral.DataMixingModule.customiseForPremixingInput
process = customiseForPreMixingInput(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim 

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions

