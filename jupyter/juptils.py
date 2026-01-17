import pandas as pd
import os


################################################################



################################################################
# left justify text cols
# convert specified col to int64

def pretty(self, int_col=None, n=10):

    df1 = self.copy() # default deep=True


    # fix int cols that turn into fugly floats
    if int_col is not None:
        df1[int_col] = df1[int_col].astype('int64')
    
    if len(df1) <= n:
        df2 = df1
    else:
        head = df1.head(n)
        tail = df1.tail(n)
      
        ellipsis_row = pd.DataFrame([['...'] * len(df1.columns)], columns=df1.columns)
      
        df2 = pd.concat([head, ellipsis_row, tail], ignore_index=True)

    text_cols = df1.select_dtypes(include='object').columns
    
    if len(text_cols) > 0:
        return df2.style.set_properties(**{'text-align': 'left'}, subset=text_cols).hide(axis="index")
    else:
        return df2


################################################################
# left justify text cols

def lefty(self, n=10):
    
    if len(self) <= n:
        df2 = self
    else:
        head = self.head(n)
        tail = self.tail(n)
        ellipsis_row = pd.DataFrame([['...'] * len(self.columns)], columns=self.columns)
        df2 = pd.concat([head, ellipsis_row, tail], ignore_index=True)

    text_cols = self.select_dtypes(include='object').columns
    
    if len(text_cols) > 0:
        return df2.style.set_properties(**{'text-align': 'left'}, subset=text_cols).hide(axis="index")
    else:
        return df2


################################################################


pd.DataFrame.lefty = lefty
pd.DataFrame.pretty = pretty





# left justify text cols


