#Setting up various environmental stuff that makes all of this jazz actually work.
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')
options.setDefault('maxEvents', 3)
options.parseArguments()

process = cms.Process("USER")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#	'file:/nfs/data/eepgadm/ROOTfiles/Summer12_tZq_signal_MC/001C0B68-536A-E311-B25F-002590D0B066.root',	
	'root://xrootd.unl.edu//store/mc/RunIIFall15DR76/tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/0449ADFC-0EA9-E511-9C06-003048F0E016.root',
        )
)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )


process.printTree = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(3),
  printVertex = cms.untracked.bool(False),
  src = cms.InputTag("genParticles")
)

process.p = cms.Path(process.printTree)
