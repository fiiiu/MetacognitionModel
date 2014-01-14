

import parameters
import glob
import csv
import numpy as np
from collections import defaultdict

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

        #smarter parse according to trial type, discarding incomplete subjects
        self.wager_data={}
        self.data={'slider': defaultdict(list), 'wager': defaultdict(list), 'plain': defaultdict(list), 'control': defaultdict(list)}
        for subject, trials in self.rawdata.iteritems():
            #skip incomplete subjects
            if len(trials)<parameters.TOTAL_TRIAL_AMOUNT:
                continue
                
            self.wager_data[subject]=[]
            for trial in trials:
                if trial[1]=='wage':
                    self.wager_data[subject].append((trial[3],trial[5],trial[7],trial[8]))
                    self.data['wager'][subject].append((trial[3],trial[5],trial[7],trial[8]))
                elif trial[1]=='slider':
                    self.data['slider'][subject].append((trial[3],trial[5],trial[7],trial[8]))
                elif trial[1]=='plain':
                    self.data['plain'][subject].append((trial[3],trial[5],trial[7],trial[8]))
                else:
                    self.data['control'][subject].append((trial[3],trial[5],trial[7],trial[8]))


        self.data_loaded=True


    ############


    def get_wager_performance(self):

        wpt=np.zeros((len(self.wager_data),parameters.WAGER_AMOUNT), dtype=int)        
        for i, subject in enumerate(self.wager_data.keys()):
            for j, trial in enumerate(self.wager_data[subject]):
                wpt[i,j]=trial[0]=='True'
        return wpt

    
    def get_wager_confidence(self):

        wct=np.zeros((len(self.wager_data),parameters.WAGER_AMOUNT), dtype=int)        
        for i, subject in enumerate(self.wager_data.keys()):
            for j, trial in enumerate(self.wager_data[subject]):
                wct[i,j]=trial[1]=='True'
        return wct

    def save_wager(self):
        wpt=self.get_wager_performance()
        np.savetxt("wager_performance.csv", wpt, fmt='%d')
        wct=self.get_wager_confidence()
        np.savetxt("wager_confidence.csv", wpt, fmt='%d')


    ######################

    def get_performance(self, trial_type):
        perfo=np.zeros((len(self.data[trial_type]), len(self.data[trial_type][self.data[trial_type].keys()[0]])), dtype=int)
        for i, subject in enumerate(self.data[trial_type].keys()):
            for j, trial in enumerate(self.data[trial_type][subject]):
                perfo[i,j]=trial[0]=='True'
        return perfo


    def get_confidence(self, trial_type):
        
        if trial_type=='wager':
            confi=np.zeros((len(self.data[trial_type]), len(self.data[trial_type][self.data[trial_type].keys()[0]])), dtype=int)
            for i, subject in enumerate(self.data[trial_type].keys()):
                for j, trial in enumerate(self.data[trial_type][subject]):
                    confi[i,j]=trial[1]=='True'
            return confi
        
        elif trial_type=='slider':
            confi=np.zeros((len(self.data[trial_type]), len(self.data[trial_type][self.data[trial_type].keys()[0]])), dtype=float)
            for i, subject in enumerate(self.data[trial_type].keys()):
                for j, trial in enumerate(self.data[trial_type][subject]):
                    confi[i,j]=trial[1]
            return confi
        
        else:
            print 'no confidence for {0} trial type, or trial type unknown'.format(trial_type)
            return None


    def get_scale(self, trial_type):
        scale=np.zeros((len(self.data[trial_type]), len(self.data[trial_type][self.data[trial_type].keys()[0]])), dtype=float)
        for i, subject in enumerate(self.data[trial_type].keys()):
            for j, trial in enumerate(self.data[trial_type][subject]):
                scale[i,j]=trial[2]
        return scale




    def savetxts(self, trial_type):
        perfo=self.get_performance(trial_type)
        np.savetxt(trial_type+'_performance.csv', perfo, fmt='%d')
        if trial_type=='wager':
            confi=self.get_confidence(trial_type)
            np.savetxt(trial_type+'_confidence.csv', confi, fmt='%d')
        elif trial_type=='slider':     
            confi=self.get_confidence(trial_type)
            np.savetxt(trial_type+'_confidence.csv', confi, fmt='%f')
        scale=self.get_scale(trial_type)
        np.savetxt(trial_type+'_scale.csv', scale, fmt='%f')


    def church_print_performace(self, trial_type, n_subs, n_trials):
        perfo=self.get_performance(trial_type)
        bigstring='('
        for i in range(n_subs):
            #bigstring+='\'('
            for j in range(n_trials):
                bigstring+=str(perfo[i,j])+' '
            #bigstring+=') '
        bigstring+=') '
        print bigstring

    def church_print_stimuli(self, circle_num, trial_type, n_subs, n_trials):
        scales=self.get_scale(trial_type)
        bigstring='('
        for i in range(n_subs):
            #bigstring+='\'('
            for j in range(n_trials):
                bigstring+=str(float(parameters.get_sizes(scales[i,j])[circle_num])/100)+' '
            #bigstring+=') '
        bigstring+=') '
        print bigstring
