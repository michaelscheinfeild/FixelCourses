import torch
from torch.nn.utils.rnn import pack_sequence
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
class SequenceDataset(torch.utils.data.Dataset):
    def __init__(self, lX, vY):
        self.lX = lX
        self.vY = vY

    def __len__(self):
        return len(self.lX)

    def __getitem__(self, idx):
        vXi = self.lX[idx]
        yi  = self.vY[idx]
        return vXi, yi
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
def SequenceCollate(lBatch):

    lX, lY = zip          (*lBatch)
    vY     = torch.stack  (lY)
    mPackX = pack_sequence(lX, enforce_sorted=False)

    return mPackX, vY
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
