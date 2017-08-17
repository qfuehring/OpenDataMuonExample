# 2011-2012-di-muon-example
Validation code for 2011/12 SingleMu and DoubleMu datasets, based on dimuon mass spectrum.

You need to work in a Virtual Machine properly contextualized for CMS.
Everything is available on the CERN Open Data Portal http://opendata.cern.ch/VM/CMS/2011.

In order to run the demoanalyzer_cfg.py to create the Commissioning ROOT files, 
you need to create a working area and set up a proper CMS environment.

## Creating the Working Area

This step is only needed the first time.
```
cmsrel CMSSW_5_3_32
```
## Setting up the CMS environment
Type this command to change directory:
```
cd CMSSW_5_3_32/src
```
```
cmsenv
mkdir Demo
cd Demo
mkedanlyzer DemoAnalyzer
cd DemoAnalyzer
```


## Cloning the 2011-2012-di-muon-example repository from Github
For cloning type:
```
git clone https://github.com/qfuehring/OpenDataMuonExample
```


## Compiling and Running
```
scram b
cmsRun demoanalyzer_cfg.py
```

## Work in Progress
