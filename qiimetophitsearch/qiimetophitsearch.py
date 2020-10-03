class qiimetophitsearch:
    def __init__(self, filename):
        import pandas as pd
        self.filename = filename

    def tophit(self, spcname):
        #import pandas as pd
        df = pd.read_csv(self.filename, delimiter='\t', header=1, index_col=0)
        return(spcname + '\t' + df[spcname].idxmax())

    def tophit_all(self):
        #import pandas as pd
        maxtaxa=[]
        df = pd.read_csv(self.filename, delimiter='\t', header=1, index_col=0)
        df=df.T
        for i in range(len(df)):
            maxtaxa.append(df.iloc[i].idxmax())
        df_new = pd.DataFrame(maxtaxa, index=df.index, columns=['#OTU ID'])
        df_new_tsv = df_new.to_csv('output.tsv', sep='\t', index=True)
        return(df_new_tsv)
   
