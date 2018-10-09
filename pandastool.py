import pandas

class prep():
    def __init__(self,datapath = ''):
        self.data = pandas.read_excel(datapath)
        self.keys = data.keys()
        self.data = data
        self.uniques = {}
        for key in self.keys:
            uniquevals = np.unique(self.data[key])
            #uniquevals = uniquevals[not np.isnan(uniquevals)]
            self.uniques[key] = uniquevals
    def get_type(self,keyvals = {}):
        newdata = self.data
        for key in keyvals.keys():
            newdata = newdata[newdata[key] == keyvals[key]]
        self._temp_data = newdata
        return newdata
    def get_stats(self,data = None,niceprint=False):
        if data is None:
            data = self._temp_data
        means = data['mean']
        if niceprint:
            print(str(np.mean(means)) + ' +/- '  + str(np.std(means)))
            return 
        return np.mean(means), np.std(means)
