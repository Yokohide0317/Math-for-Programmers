#%%
import glob
import os

# %%
flist = glob.glob("./Chapter*") + glob.glob("./Appendix*")
flist
# %%
for file in flist:
  os.rename(file, file.replace(" ", "_"))
# %%
