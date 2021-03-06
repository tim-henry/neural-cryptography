# sys
from abc import ABC, abstractmethod
from enum import Enum

#lib
from dataclasses import dataclass
# self
from models.model import NeuralCryptographyModel


class AdversarialGame(Enum):
    """
    The types of adversarial game that eve can play against encryption
    techniques.

    ******** Games

    CiphertextIndistinguishability1: Given a plaintext P and a possible
    encryption of that P, C'. Was C' = ENC(P)?

    CiphertextIndistinguishability2: Given two plaintexts P_1,
    and P_2 and two ciphertexts C_1 and C_2: which C belongs
    to which P? The exact formatting in the network is described
    below.
    """
    CiphertextIndistinguishability1 = 0
    CiphertextIndistinguishability2 = 1

    # TODO CCA like attacks?


@dataclass
class Eve(NeuralCryptographyModel, ABC):

    @abstractmethod
    def initialize_model(self):
        raise NotImplementedError()

    @staticmethod
    def get_supported_adversarial_modes():
        """
        A method to validate what kinds of adversarial games
        the current Eve implementation supports. The default
        is that all implementations are supported.

        :return: a set of the supported AdversarialGame(s)
        """
        return set([v for v in AdversarialGame])

    def __call__(self,
                 epochs=50,
                 iterations_per_epoch=300,
                 batch_size=512):
        """
        fit eve on data generated by specification to the
        Adversarial games. The data generation function
        should handle most of this. Thus, few params are needed
        for eves fitting.

        The call description of this class' superclass also
        hold.

        :param epochs: The number of epochs to fit eve
        :param batch_size: the batch size
        :return:
        """
        raise NotImplementedError()

