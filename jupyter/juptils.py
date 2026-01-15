import pandas as pd
import os


################################################################

def env(key=None):
  if(key==None):
    return dict(sorted(os.environ.items()))
  else:
    return os.environ[key]  # raises KeyError if not set


################################################################

def ping():
  print("pong: juptils works! 😎")

  
################################################################

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
        return df2.style.set_properties(**{'text-align': 'left'}, subset=text_cols)
    else:
        return df2


################################################################

def show_all(self):
    with pd.option_context('display.max_rows', len(self)):
        display(self)


################################################################

def save_csv(self, fpath):
    self.to_csv(fpath, index=False)


################################################################


pd.DataFrame.lefty = lefty
pd.DataFrame.show_all = show_all
pd.DataFrame.save_csv = save_csv



