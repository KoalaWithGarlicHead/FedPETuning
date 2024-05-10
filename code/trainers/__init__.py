"""FedETuning's trainers registry in trainer.__init__.py -- IMPORTANT!"""

from code.trainers.FedBaseTrainer import BaseTrainer
from code.run.fedavg.trainer import FedAvgTrainer
from code.run.centralized.trainer import CenClientTrainer
from code.run.dry_run.trainer import DryTrainer

__all__ = [
    "BaseTrainer",
    "FedAvgTrainer",
    "DryTrainer",
    "CenClientTrainer"
]
