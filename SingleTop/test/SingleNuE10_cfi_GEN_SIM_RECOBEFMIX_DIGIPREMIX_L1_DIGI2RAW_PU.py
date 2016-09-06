# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleNuE10_cfi --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --pileup_input dbs:/MinBias/almorton-CRAB3_MC_PileUp_160906b-0e8a9371e45edd808242a5d89d29dcd9/USER instance=prod/phys03 --fast --mc --eventcontent PREMIX -s GEN,SIM,RECOBEFMIX,DIGIPREMIX,L1,DIGI2RAW --era Run2_2016 --beamspot Realistic25ns13TeV2016Collision --datatier GEN-SIM-DIGI-RAW --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU -n 5000000 --fileout minbias_premixed.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('DIGI2RAW',eras.Run2_2016,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.Digi_PreMix_cff')
process.load('SimGeneral.MixingModule.digi_noNoise_cfi')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleNuE10_cfi nevts:5000000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('minbias_premixed.root'),
    outputCommands = process.PREMIXEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_1.root', 
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_10.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_100.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_101.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_102.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_103.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_104.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_105.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_106.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_107.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_108.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_109.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_11.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_110.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_111.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_112.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_113.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_114.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_115.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_116.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_117.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_118.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_119.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_12.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_120.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_121.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_122.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_123.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_124.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_125.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_126.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_127.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_128.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_129.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_13.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_130.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_131.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_132.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_133.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_134.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_135.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_136.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_137.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_138.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_139.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_14.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_140.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_141.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_142.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_143.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_144.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_145.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_146.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_147.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_148.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_149.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_15.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_150.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_151.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_152.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_153.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_154.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_155.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_156.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_157.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_158.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_159.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_16.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_160.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_161.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_162.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_163.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_164.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_165.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_166.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_167.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_168.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_169.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_17.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_170.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_171.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_172.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_173.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_174.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_175.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_176.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_177.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_178.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_179.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_18.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_180.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_181.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_182.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_183.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_184.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_185.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_186.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_187.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_188.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_189.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_19.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_190.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_191.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_192.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_193.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_194.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_195.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_196.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_197.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_198.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_199.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_2.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_20.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_200.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_201.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_202.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_203.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_204.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_205.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_206.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_207.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_208.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_209.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_21.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_210.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_211.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_212.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_213.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_214.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_215.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_216.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_217.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_218.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_219.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_22.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_220.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_221.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_222.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_223.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_224.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_225.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_226.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_227.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_228.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_229.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_23.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_230.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_231.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_232.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_233.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_234.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_235.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_236.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_237.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_238.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_239.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_24.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_240.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_241.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_242.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_243.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_244.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_245.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_246.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_247.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_248.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_249.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_25.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_250.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_26.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_27.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_28.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_29.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_3.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_30.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_31.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_32.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_33.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_34.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_35.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_36.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_37.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_38.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_39.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_4.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_40.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_41.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_42.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_43.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_44.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_45.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_46.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_47.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_48.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_49.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_5.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_50.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_51.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_52.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_53.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_54.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_55.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_56.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_57.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_58.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_59.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_6.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_60.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_61.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_62.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_63.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_64.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_65.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_66.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_67.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_68.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_69.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_7.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_70.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_71.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_72.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_73.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_74.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_75.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_76.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_77.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_78.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_79.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_8.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_80.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_81.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_82.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_83.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_84.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_85.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_86.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_87.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_88.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_89.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_9.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_90.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_91.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_92.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_93.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_94.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_95.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_96.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_97.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_98.root',
       '/store/user/almorton/MinBias/CRAB3_MC_PileUp_160906b/160906_084523/0000/minbias_99.root' ] )

process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersNoNoise)
process.esDigiToRaw.Label = cms.string('mix')
process.SiStripDigiToRaw.FedReadoutMode = cms.string('PREMIX_RAW')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_miniAODv2_v1', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxE = cms.double(10.01),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinE = cms.double(9.99),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        PartID = cms.vint32(12)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single Nu E 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXoutput_step = cms.EndPath(process.PREMIXoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


