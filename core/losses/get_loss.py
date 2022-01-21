'''As in https://github.com/lliuz/ARFlow'''
from .flow_loss import unFlowLoss

def get_loss(args):
    return unFlowLoss(args)
