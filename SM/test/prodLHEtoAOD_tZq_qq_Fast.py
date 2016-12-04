# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: cmsDriver.py Hadronizer_TuneCUETP8M1_13TeV_aMCatNLO_FXFX_LHE_pythia8_cff.py --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --filein file:/scratch/data/SMProdv1/tZq_qq_4f/0.lhe --filetype LHE --era Run2_2016 --fast -n 1000 --eventcontent AODSIM --datatier AODSIM -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 --pileup_input dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput --beamspot Realistic25ns13TeV2016Collision --python_filename prodLHEtoAOD_tZq_qq_Fast.py --datamix PreMix --fileout aod.root --no_exec
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
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
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
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:/scratch/data/SMProdv1/tZq_qq_4f/0.lhe'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('cmsDriver.py nevts:1000'),
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
process.mixData.input.fileNames = cms.untracked.vstring([
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/007F9F8A-EB14-E611-9918-00259075D72C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00A7A158-4E14-E611-A2E5-0025905B858E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00B28D0D-A214-E611-A9FA-0025904C4E28.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00C7136F-8714-E611-9DD4-0025905B8564.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00ECAC4F-5714-E611-ACAC-0CC47A4D76D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02053F47-7B14-E611-904C-0025905C53D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/020ACED3-8C14-E611-9F4D-0025905B85DC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0259F967-6915-E611-8908-00304867FE4B.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02600760-4E14-E611-B7D9-0025905B8592.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/027EC271-7714-E611-971C-0025905C5502.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/029D19A1-4514-E611-ACD3-001517E73360.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02B46E59-4E14-E611-82AF-0CC47A4D7604.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02C50D59-4E14-E611-B199-0090FAA577A0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02E04A60-4E14-E611-9D85-0025905A60D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02F0DE1B-7015-E611-81F5-00259075D70C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04175ACA-5014-E611-97B9-0025904C68D8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/043DD82D-7B14-E611-9E64-0CC47A4C8EEA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/044585D0-5014-E611-BA37-0025904C51F0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/049348CE-5014-E611-B371-0025905D1D02.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04E3B581-5314-E611-916B-0CC47A4C8E64.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04E7AEC8-8714-E611-BF27-0025905D1D02.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04FE622A-A614-E611-8CE2-0CC47A4D7692.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06098861-4C14-E611-A286-0025905BA736.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/062D8F6F-7714-E611-AE29-0025905C2CE4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06668956-4E14-E611-A56B-0CC47A4D762E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0677985B-4C14-E611-99B2-0025905C3DD0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06B39613-A514-E611-B9AE-0025905B8612.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06D299D4-8F14-E611-93D8-0025905C53DE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06E09F8D-5414-E611-A29B-0025905A6070.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/080290F5-A514-E611-A9A3-0CC47A4D7690.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/080DB547-7E14-E611-85B3-0CC47A4C8E16.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0814345E-9B14-E611-A9C0-0025905B8590.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/085D91CB-8C14-E611-A8A0-0CC47A78A408.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0878DF51-DE14-E611-9E59-002590D9D8AE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0891A328-7B14-E611-9FC1-00259074AEAE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08A168C4-8714-E611-97B6-0025905C4300.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08B47A72-7814-E611-B67E-0025905A6084.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08CBF654-4E14-E611-BE96-0090FAA57EA4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08D2697C-5714-E611-AD80-0025905A6138.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08D3092B-4E14-E611-A59C-0CC47A4D7650.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08EC3645-6515-E611-97F5-002590D9D894.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A20247D-5F15-E611-9BC6-0CC47A0AD48A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A333FC8-8C14-E611-B563-0CC47A4D7630.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A38A0D5-8714-E611-B1C2-0025904C4F9E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A6F4F44-7E14-E611-AB64-0025905B857E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A85C572-8714-E611-A019-0025905A60E4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0AA4E94B-5714-E611-996D-0025905A60F8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0ACA23F7-5514-E611-93DA-0025905A606A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0ADA187F-7814-E611-B66D-002590D0AF86.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0ADDC08E-5414-E611-94A5-0025905A609E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C0E0035-5014-E611-9EC1-0CC47A78A408.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C2BFB1F-A714-E611-B07D-0CC47A4D75F8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C427E16-7B14-E611-8D40-0CC47A4C8E26.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C5612A1-6015-E611-921E-00304867FE47.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C6EC989-5414-E611-AEAE-003048FFD7AA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0CD3D07B-7814-E611-B0CE-0025905D1D78.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0CD4DBD5-7B14-E611-B1EA-0025904C66F6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0CFF97D0-4E14-E611-925D-0090FAA588B4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E01F1D2-7B14-E611-9C92-0025904C656A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E0648CA-8C14-E611-930B-0CC47A4C8F18.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E35A01D-5314-E611-A181-0025905A48D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E4CD370-5114-E611-B885-0025905B85EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E579A3E-9814-E611-9098-0CC47A4C8F18.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E8AF4D5-8C14-E611-BF44-0CC47A4C8E82.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E900AC9-5014-E611-BEAC-0025905C3DF8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E9FC31D-A714-E611-B989-0CC47A78A2F6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0EB7EE87-5414-E611-8616-0CC47A4D76B6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0EB96469-9B14-E611-871F-0025905A6138.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0EE97D16-A514-E611-BE42-0CC47A4C8EB0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/100F428A-5414-E611-8708-0CC47A4D7638.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/102DB47F-9C14-E611-BB3D-003048FFD71C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/10324AA0-4514-E611-BDC4-001E675A6D10.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1033B8BE-8F14-E611-8A8C-0025904C540C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/103C2CEC-7F15-E611-AB80-002590D9D8BC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/105B8E31-A614-E611-975D-0CC47A78A456.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/105E5E47-6D14-E611-B172-0CC47A0AD6AA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1060E274-8714-E611-8881-0CC47A4D76B6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/108F6171-7814-E611-800B-0025905B860E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1091FF9C-5714-E611-8779-0CC47A4C8F18.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/10BAA559-4E14-E611-A706-0025907750A0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/10EDF937-9814-E611-8E03-0025905B85EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/121B0F65-4E14-E611-9EEC-0CC47A1DF1AA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1239651D-7C14-E611-BC16-0025905C5500.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12410AD3-5014-E611-8BDF-0025905D1D52.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1245F0F3-4F14-E611-A31A-0025905B85A0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/124D3137-5014-E611-9BD0-0CC47A4D7662.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1250345B-4E14-E611-B79F-0025905B85DC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12551AF5-5514-E611-9619-0CC47A4C8E26.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12B81A58-4E14-E611-B439-0025905A6064.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12B860FC-4F14-E611-B057-0025905B8598.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12EA0BF6-5514-E611-AA08-0025905A48C0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/12EA6C69-7714-E611-8EDD-0025905C3E36.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/14408D1D-5014-E611-8BE0-0CC47A4C8E22.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1470E68A-5414-E611-9654-0025905A60B2.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/149D4CE2-8C14-E611-A14B-0025905C2CA4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/14B7BCD0-5014-E611-8D1C-0025904C68DE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/14CCB936-A614-E611-BB99-0CC47A4C8E64.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/160FE543-7E14-E611-B6A2-0CC47A4D7614.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1639D059-4E14-E611-8657-0025905B85EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/16463678-9414-E611-8B20-0025905C95FA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/16481C60-7E14-E611-9EF8-0025905C3E66.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1656DD2F-7B14-E611-BB4B-0025905C53DC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/165AE977-7814-E611-A499-0090FAA57750.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/169DFBF4-5514-E611-8E5D-0CC47A4D76BE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18054E7F-7814-E611-AF9C-00259073E3A2.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18380038-7B14-E611-92B6-0090FAA578F0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18458387-7814-E611-A5BF-0025905C54C4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1870844F-5714-E611-812C-0CC47A4C8ECA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18766777-7814-E611-91F2-0090FAA588B4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1883C43E-7E14-E611-A4BC-0CC47A4D76AA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18CBA82C-5014-E611-8C24-00259073E536.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18E2795C-4C14-E611-A6BD-0025904CF93C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18E47E46-7E14-E611-8B8C-0CC47A4D767A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A0A9C0F-A214-E611-A471-0025905C542C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A16E57A-7814-E611-9F2C-0CC47A745284.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A1AEF6C-8714-E611-96A9-0CC47A78A458.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A275247-9214-E611-B2FF-0025905B85CA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A38A95C-7E14-E611-83E6-0025904C66E8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A3A4C86-7814-E611-9E74-0025905C2CEA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A829D46-7E14-E611-BA60-0CC47A78A468.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A8E0046-7E14-E611-8EDC-0025905A60B0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1A90FCF3-4F14-E611-BB64-0025905B8592.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1AD96430-7B14-E611-B417-0CC47A78A4B8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1AE12A1E-6415-E611-847C-0CC47A57CD00.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C17210D-7F14-E611-91F5-0025905C2C86.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C353029-4514-E611-8594-90B11C06DD39.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C35307D-7814-E611-B9BD-0025905A48EC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C445D20-5314-E611-9BBC-0025905A60BC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C5D1E7B-7814-E611-940A-0025905A610A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1C7F0BF0-7B14-E611-9A55-0025905B85BA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1CCE1478-7814-E611-B05D-0090FAA57770.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E07C514-A514-E611-BCA1-0CC47A745250.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E4A5A78-7814-E611-AE0A-0025905A6056.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E4E64D0-4E14-E611-A5A6-0090FAA1ACF4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E7298C6-DC14-E611-A127-0CC47AB0B828.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E9BF71E-A714-E611-A613-0CC47A4C8F12.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1EC74898-7815-E611-A83A-00304867FEEB.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1EFAF937-9B14-E611-B910-0CC47A4D7614.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2021BBBB-5014-E611-93C6-0CC47A4D76D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2048757B-7814-E611-A1B1-0090FAA59114.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/206D5C7D-5114-E611-8C16-0025904CF75A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/20D6751B-4514-E611-A1A9-001E67E69E32.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2220560E-5314-E611-BD25-0CC47A4D75F8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/227ED37B-7814-E611-A6B8-00259073E504.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/228284F3-5514-E611-B1CE-0025905A6104.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/228DF526-A614-E611-B473-0CC47A78A426.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/229C674E-7B14-E611-9851-0CC47A4DED0C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/22AEE254-7E14-E611-B9EF-0025905C2CEA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/22E4981B-7B14-E611-8563-0CC47A4D76AA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2407B37D-5714-E611-9D9B-0025905B8600.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24498348-9814-E611-AEAB-0025905A60D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24546159-4E14-E611-82B8-0025905A6122.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24765458-4E14-E611-91CD-0025905A613C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2482B430-EB14-E611-A8F4-003048CB8584.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2493C989-8F14-E611-B853-0025904C67B6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24A19252-4F14-E611-8FF1-0025904CF93E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24DEB958-4E14-E611-9377-0025905A607E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24E85B4E-9814-E611-97F7-0CC47A4D7630.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24EEC859-7E14-E611-B352-0025905C4300.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2627AED7-4E14-E611-A346-00259073E51A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2635F895-5114-E611-8CDB-0CC47A4C8E16.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2661987A-7814-E611-A096-0025905B859A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26AC637F-8F14-E611-9000-0025905C54C4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26BCA26F-7814-E611-8924-0CC47A78A4B8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26C50B3C-5314-E611-B152-0CC47A7452D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26D77B6E-DA14-E611-AEA4-002590FD5122.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26D9716F-8714-E611-B5B9-0025905A608A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26E2745B-4E14-E611-83F1-0025905A6080.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26ECD7C3-5014-E611-847B-0025905C975E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26F71DF1-4F14-E611-919D-0CC47A4C8E96.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26F8832A-5014-E611-ABB6-00259073E3D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/26F9C76C-7814-E611-9A0C-0090FAA57360.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/281FD6FA-4F14-E611-91CB-0025905D1D60.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/28697F29-A614-E611-83A7-0CC47A4D7626.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/28C42942-7E14-E611-8585-0CC47A4C8F2C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/28DBB337-8D14-E611-860C-0025904C540E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2A047678-7814-E611-BD66-0CC47A4C8F0A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2A182890-5414-E611-AEB3-0CC47A4C8E22.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2A22B674-7814-E611-BB35-0090FAA57BE0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2A2B54A7-5814-E611-922B-0CC47A7452D8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AD0C6F1-5514-E611-8F72-0CC47A4D75F0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AE94768-7714-E611-9273-0025905D1D50.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AF19F25-5014-E611-A600-0CC47A4C8E2A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AFC4AAC-A414-E611-B89D-0025905A60D6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AFF286C-7714-E611-BA63-0025905C2CA4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C166625-DB14-E611-90A9-0CC47A57D136.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C18F83C-5314-E611-92C3-0CC47A78A418.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C1EBD2B-7B14-E611-8136-0CC47A4C8E98.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C23A879-5114-E611-BA10-0025905B8562.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C68F72B-A614-E611-BEBA-0025905A6104.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C86CD83-7814-E611-B002-0025905C3D96.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2C99BE2C-7B14-E611-9469-0025905C2CEA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2CAC5EF4-5514-E611-9EF7-0025905A60B6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2CAEAE3D-7E14-E611-88A6-0CC47A4C8F1C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2CD5F856-4E14-E611-A60B-0CC47A4C8E22.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2CEE5A29-A614-E611-8518-0CC47A78A3EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E0A3D18-A814-E611-8A71-0CC47A4C8F08.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E30508B-5114-E611-877D-0CC47A4D765E.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E3CE1D5-5014-E611-A77C-0025905C53DE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E6554F1-9D14-E611-B428-0025905C2C84.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E7CEE5D-9414-E611-AB1D-0CC47A7452D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E97E44C-7B14-E611-9812-0025905C431A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2ECDF152-9B14-E611-89F2-0CC47A4C8E26.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2EE76744-7E14-E611-A3D1-0CC47A4C8F30.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2EEF36C3-8714-E611-AE89-0025905C2CBC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/300CDD5F-4E14-E611-BD3C-0CC47A4D7662.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/30273D7E-7814-E611-AA20-00259073E4AC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3064074C-7B14-E611-ABA2-0025905C3E66.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/32262D3A-5314-E611-890F-0CC47A78A456.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/322BA3C1-8714-E611-9EB7-0025905D1CB4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/322D29C6-8714-E611-98FE-0025904C6788.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3238A263-5714-E611-AD18-0025905B8580.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/323D873C-8A14-E611-A831-0025905A6132.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/32483092-7B14-E611-AF0E-0090FAA57330.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/327DD736-5014-E611-9816-0025905B8560.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/343CCC85-7814-E611-8EBD-0025905C2C86.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/346B0767-8714-E611-BE96-0CC47A4D7654.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/347921BC-5014-E611-9F44-0025904C6414.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/348CEC21-A814-E611-9150-0025905A60FE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/34E43CF7-A214-E611-A773-0025905B858A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/34F0B23E-9814-E611-AB64-0CC47A4D7600.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3613A33D-9814-E611-9C75-0CC47A4C8E26.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/364444B2-5114-E611-AFA0-0CC47A4C8E98.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3670E842-9B14-E611-8906-0CC47A4D764A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3690D050-4E14-E611-B429-0CC47A4D76AC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/36BF233E-9814-E611-842D-0CC47A4D7618.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/36C03B70-5714-E611-BD27-0025905A6080.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3817D3D1-5014-E611-9A2D-0025904C4F50.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/386594D0-5A15-E611-89E8-0025901ABD18.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/387F039F-A414-E611-A3DF-0025905B857C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/389B8776-7814-E611-AEA0-0090FAA57C60.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/389E118B-5414-E611-9AF9-0025905A6076.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/38A36B2B-5014-E611-9691-0025907750A0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/38C69538-9B14-E611-A190-0CC47A4C8EC6.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/38F79E3C-7B14-E611-9C17-002590D0AFB8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3A548B3C-7B14-E611-BD62-0025905D1CB4.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3A578F11-4F14-E611-9076-0CC47A4C8F18.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3A8CB136-5014-E611-B8B0-0025905B858C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3AF09F3B-5314-E611-A128-0CC47A4C8EEA.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3AF31A59-4E14-E611-8C23-0025905A60B0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C2B0DD0-8C14-E611-90F2-0CC47A4C8ECE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C447B57-4C14-E611-8057-0025905C3E66.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C7A5B40-9814-E611-BD0F-0CC47A4C8E14.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C85168C-5414-E611-86EC-0025905B858A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C8A424B-9B14-E611-A259-0025905A60EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3CEECE12-A214-E611-8113-0025904C656A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3E1A6186-AA14-E611-A00C-0025905A60EE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3E23E059-4F14-E611-A7DD-0025905C53D0.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3E25C57B-7814-E611-905A-00259074AEAE.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3E7A5573-8714-E611-BB4E-0CC47A4C8F2C.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3E9F9E78-7814-E611-9AB9-0CC47A4D7634.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3EBFAE74-5114-E611-AB49-0025905C2CE8.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3ED82A81-7814-E611-8576-0025905C43EC.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/40003B73-7E14-E611-BA5E-0025905C3D6A.root',
       '/store/mc/RunIISpring16FSPremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/40266E42-7E14-E611-94F5-0025905A607A.root' ] )

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

