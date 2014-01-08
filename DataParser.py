

import parameters
import glob
import csv
import numpy as np


class DataParser():

    def __init__(self):
        self.data_directory=parameters.DATA_DIRECTORY
        self.data_loaded=False


    def load(self):

        if self.data_loaded:
            return

        self.rawdata={}

        for datafile in glob.glob(self.data_directory+'*.out'):
            subject=datafile[-12:-9]
            with open(datafile) as inputfile:
                fulldata=list(csv.reader(inputfile, delimiter='\t'))
                self.rawdata[subject] = fulldata[1:]


        self.wager_data={}
        for subject, trials in self.rawdata.iteritems():
            self.wager_data[subject]=[]
            for trial in trials:
                if trial[1]=='wage':
                    self.wager_data[subject].append((trial[3],trial[5],trial[7],trial[8]))

        for subject in list(self.wager_data.keys()):
            if len(self.wager_data[subject])<parameters.WAGER_AMOUNT:
                del self.wager_data[subject]

        self.data_loaded=True



    def get_wager_performance_table(self):

        wpt=np.zeros((len(self.wager_data),parameters.WAGER_AMOUNT), dtype=int)        
        for i, subject in enumerate(self.wager_data.keys()):
            for j, trial in enumerate(self.wager_data[subject]):
                wpt[i,j]=trial[0]=='True'

        return wpt

    
    def save_wager_performance_table(self):
        wpt=self.get_wager_performance_table()
        np.savetxt("wager_performance_table.csv", wpt, fmt='%d')
