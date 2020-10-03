class qiimetophitsearch:
    def __init__(self, filename):
        import pandas as pd
        self.filename = filename

    def tophit(self, spcname):
        #import pandas as pd
        df = pd.read_csv(self.filename, delimiter='\t', header=1, index_col=0)
        return(spcname + ',' + df[spcname].idxmax())

    def tophit_all(self):
        #import pandas as pd
        maxtaxa=[]
        df = pd.read_csv(self.filename, delimiter='\t', header=1, index_col=0)
        df=df.T
        for i in range(len(df)):
            maxtaxa.append(df.iloc[i].idxmax())
        df_new = pd.DataFrame(maxtaxa, index=df.index, columns=['#OTU ID'])
        return(df_new)
   
