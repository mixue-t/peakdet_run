#!/usr/bin/env python

from __future__ import absolute_import
from peakdet import physio
from scipy.interpolate import interp1d


class ECG(physio.PeakFinder):
    """
    Class for ECG data analysis
    """

    def __init__(self, data, fs):
        super(ECG,self).__init__(data, fs)
        self.bandpass([5.,15.])


class PPG(physio.PeakFinder):
    """
    Class for PPG data analysis
    """

    def __init__(self, data, fs):
        super(PPG,self).__init__(data, fs)
        self.lowpass([2.0])


class RESP(physio.PeakFinder):
    """
    Class for respiratory data analysis
    """

    def __init__(self, data, fs, TR=None):
        super(RESP,self).__init__(data, fs)
        self.bandpass([0.01,0.5])
        self._TR = TR

    @property
    def TR(self):
        return self._TR

    @TR.setter
    def TR(self, value):
        self._TR = float(value)

    @property
    def RVT(self, TR=None):
        if TR is not None: self.TR = TR
        if self.TR is None: raise ValueError('TR needs to be set!')

        peaks   = self.rawdata[self.peakinds]
        heights = self.rawdata[self.troughinds]
