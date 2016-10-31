brunel-nTuples
==============

ntupliser for brunel group

the famous ntupliser passed down from one generation of brunel phd student to
the next. all our marks left indelibly on it, if no other reason than that the
next guy has no idea what we did.

enjoy, future students.

***

The CMSSW_8_0_20 branch contains code from CMSSW_8_0_5 branch which is modified
to work for Run 2 miniAODv3 80X data and MC. As data/MC reprocessing taking is
using CMSSW_8_0_X, the branch is named CMSSW_8_0_20 after the version which data
and MC is currently avaliable for.

N.B. As Run 2 MC seems to use Pythia 8 for generation, the old status codes have
been updated from those used in Pythia 6. This WILL affect the output. Double
check generator used if running over old data. Status code for gen level is
saved. Worth noting that other occasions where status code is checked, these dsfsdf
varaibles are not saved to the final root nTuple output.

---

## FCNC Stuff:

Generation of signal samples up till the LHE
format: <https://twiki.cern.ch/twiki/bin/view/CMS/TopFCNCgenerationSingletop>

Due to the size of the lhe files generated, they cannot be included in the crab
sandbox and have to be on a grid storage element to be accesible. The command to
copy them is: 

``` bash
xrdcopy <file> 'root://dc2-grid-64.brunel.ac.uk////cms/store/user/<username>/<dirPath>'
```

Rest of instructions follow below ...

N.B. For some reason I have not been able to get premixing to work correctly on
pion - used lxplus machines to submit the Crab jobs and retrieved the final
output (i.e. signal files) on pion.

The cmsDriver.py scripts must be run in the src directory of the CMSSW release.

Additional setup if doing generation stuff (i.e. LHE to AOD):

``` bash
git cms-addpkg Configuration/Applications

git submoudle add git@github.com:cms-sw/genproductions.git Configuration/GenProduction/

git submoudle add https://github.com/kskovpen/FCNCProd

cp NTupliser/FCNC/python/* Configuration/GenProduction/python/
```

Modify Configuration/Applications/python/ConfigBuilder.py to include
`defaultOptions.limit = 0`

cmsDriver instructions used to create various FCNC files:

pileup:
ST FCNC script for LHE to AOD:-

``` bash
cmsDriver.py Configuration/GenProduction/python/Hadronizer_ZToLL_cfi.py \
    --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 \
    --filein file:/tmp/almorton/TLL_Thadronic_kappa_zct.lhe --filetype LHE \
    --era Run2_2016 --fast -n 10 --eventcontent AODSIM --datatier AODSIM \
    -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 \
    --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW" \
    --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput \
    --beamspot Realistic25ns13TeV2016Collision \
    --python_filename prodLHEtoAOD_ST_TZ_2L_Kappa_Zct.py --datamix PreMix \
    --fileout aod.root --no_exec
```

Current output dataset DAS URLs:

Kappa Zct (part1):
`/ST_TZ_2L_Kappa_Zct_161006/almorton-CRAB3_MC_ST_TZ_2L_Kappa_Zct_161006-491cc9c0c16244aa3248937bd6af6e2c/USER`

Kappa Zct (part2):
`/ST_TZ_2L_Kappa_Zct_ext_161006/almorton-CRAB3_MC_ST_TZ_2L_Kappa_Zct_ext_161006-491cc9c0c16244aa3248937bd6af6e2c/USER`

Kappa Zut:
`/ST_TZ_2L_Kappa_Zct_ext_161020/almorton-CRAB3_MC_ST_TZ_2L_Kappa_Zct_ext_161020-491cc9c0c16244aa3248937bd6af6e2c/USER`

Zeta Zct:
`/ST_TZ_2L_Zeta_Zct_161007/almorton-CRAB3_MC_ST_TZ_2L_Zeta_Zct_161007-491cc9c0c16244aa3248937bd6af6e2c/USER`

Zeta Zut:
`/ST_TZ_2L_Zeta_Zut_20161024/choad-CRAB3_MC_ST_TZ_2L_Zeta_Zut_20161024-491cc9c0c16244aa3248937bd6af6e2c/USER`

TTbar FCNC script for LHE to AOD:

``` bash
cmsDriver.py Configuration/GenProduction/python/Hadronizer_TTbar_ZToLL_cfi.py \
    --mc --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 \
    --filein root://sbgse1.in2p3.fr//store/user/kskovpen/FCNCProdv2/LHE/TT_topLeptonicDecay_kappa_zut_LO/0.lhe \
    --filetype LHE --era Run2_2016 --fast -n 10 --eventcontent AODSIM \
    --datatier AODSIM \
    -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@frozen2016 \
    --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW" \
    --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput \
    --beamspot Realistic25ns13TeV2016Collision \
    --python_filename prodLHEtoAOD_TT_TopLeptonicDecay_TZ_2L_Kappa_Zut.py \
    --datamix PreMix --fileout aod.root --no_exec
```

### FCNC script for AOD to miniAOD:

``` bash
cmsDriver.py step2 --filein file:aod.root --fileout file:miniaod.root -n 10 \
    -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --era Run2_2016 \
    --no_exec --python_filename prodAODtoMINIAOD.py \
    --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v1 --fast
```

Current output dataset DAS URLs: In production

Alexander.
