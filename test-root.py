import ROOT

print "This is a test or PyROOT"
h = ROOT.TH1D("h", "", 10, 0, 10)
h.FillRandom("gaus", 100)
print h.GetMean()