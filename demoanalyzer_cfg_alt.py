import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process = cms.Process("Demo")


# intialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
# **********************************************************************
# set the maximum number of events to be processed                     *
#    this number (argument of int32) is to be modified by the user     *
#    according to need and wish                                        *
#    default is preset to 10000 events                                 *
# **********************************************************************
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# set the number of events to be skipped (if any) at end of file below

# select one of the following two:
# define JSON file for 2011 data
#goodJSON = '/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt'
# define JSON file for 2012 data
goodJSON = '/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'


myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',')

# ****************************************************************************
# define the input data set here by inserting the appropriate .txt file list *
# ****************************************************************************
import FWCore.Utilities.FileUtils as FileUtils
#
# ******************************************************************
# load the data set (uncomment exactly one of the following lines) *
# useful datasets are SingleMu and DoubleMu                        *
# To run over all data subsets, uncomment them one by one          *
# consecutively (make sure you save the output before rerunning)   *
# and add up the histograms (separately for 2011 and 2012)         *
# using root tools.                                                *
# ******************************************************************
#
# *** SingleMu data sets 2011 ***
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_SingleMu_AOD_12Oct2013-v1_10000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_SingleMu_AOD_12Oct2013-v1_10001_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_SingleMu_AOD_12Oct2013-v1_20000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_SingleMu_AOD_12Oct2013-v1_20001_file_index.txt')

# *** DoubleMu data sets 2011 ***
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_10000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_10001_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2011A_DoubleMu_AOD_12Oct2013-v1_20000_file_index.txt')

# *** SingleMu data sets 2012 ***
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_110000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20001_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20002_file_index.txt')
files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20003_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20008_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20009_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20011_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20012_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20014_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20016_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20020_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20023_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20025_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20033_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20036_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_20040_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_30000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_30001_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_30003_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_SingleMu_AOD_22Jan2013-v1_30004_file_index.txt')

# *** DoubleMu data sets 2012 ***
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_10000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20001_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_20002_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_210000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_30000_file_index.txt')
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/CMS_Run2012B_DoubleMuParked_AOD_22Jan2013-v1_310000_file_index.txt')


# to test parts of bigger index files
# files201112data = FileUtils.loadListFromFile ('/home/cms-opendata/OpenDataMuonExample/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/test_index.txt')


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*files201112data    
    )
)

# apply JSON file
#   (needs to be placed *after* the process.source input file definition!)
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

# *************************************************
# number of events to be skipped (0 by default)   *
# *************************************************
process.source.skipEvents = cms.untracked.uint32(0)


process.demo = cms.EDAnalyzer('DemoAnalyzer'
)
# ***********************************************************
# output file name (exactly one should be uncommented)      *
# default is SingleMu.root                                  *
# change this according to your wish                        *
# ***********************************************************
process.TFileService = cms.Service("TFileService",
       fileName = cms.string('SingleMu.root')
#       fileName = cms.string('DoubleMu.root')
                                   )

process.p = cms.Path(process.demo)
