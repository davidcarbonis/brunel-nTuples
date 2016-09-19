# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Hadronizer_TTbar_ZToLL_cfi.py --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --filein root://sbgse1.in2p3.fr//store/user/kskovpen/FCNCProdv2/LHE/TT_topLeptonicDecay_kappa_zct_LO/0.lhe --filetype LHE --era Run2_2016 --fast -n 10 --eventcontent AODSIM --datatier AODSIM -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 --pileup_input dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput --beamspot Realistic25ns13TeV2016Collision --python_filename prodLHEtoAOD_TT_AntiTopLeptonicDecay_TZ_2L_Kappa_Zct.py --datamix PreMix --fileout aod.root --no_exec
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
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/0.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/1.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/2.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/3.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/4.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/5.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/6.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/7.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/8.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/9.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/10.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/11.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/12.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/13.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/14.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/15.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/16.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/17.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/18.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/19.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/20.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/21.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/22.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/23.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/24.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/25.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/26.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/27.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/28.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/29.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/30.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/31.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/32.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/33.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/34.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/35.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/36.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/37.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/38.lhe',
    'root://sbgse1.in2p3.fr//dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/FCNCProdv2/LHE/TT_antitopLeptonicDecay_kappa_zct_LO/39.lhe'
    ),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/Hadronizer_TTbar_ZToLL_cfi.py nevts:10'),
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

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 40.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 2', 
            'JetMatching:doShowerKt = off'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters', 
            'JetMatchingParameters'),
        processParameters = cms.vstring('23:onMode = off', 
            '23:5:onMode = on', 
            '23:7:onMode = on', 
            '23:9:onMode = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

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
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

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

