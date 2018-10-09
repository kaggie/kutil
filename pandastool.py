import pandas

class prep():
    def __init__(self,data):        
        self.keys = data.keys()
        self.data = data
        self.uniques = {}
        self._temp_data = data
        for key in self.keys:
            uniquevals = np.unique(self.data[key])
            #uniquevals = uniquevals[not np.isnan(uniquevals)]
            self.uniques[key] = uniquevals
    def get_type(self,keyvals = {}, data = None):
        if data is None:
            newdata = self.data
        else:
            newdata = data
        for key in keyvals.keys():
            newdata = newdata[newdata[key] == keyvals[key]]
        self._temp_data = newdata
        return newdata
    def get_stats(self,data = None,niceprint=False):
        if data is None:
            data = self._temp_data
        means = data['mean']
        n = len(means)
        if niceprint:
            print(str(np.mean(means)) + ' +/- '  + str(np.std(means)) + ' , N = ' + str(n))
            return 
        return np.mean(means), np.std(means)
