"""
nl2t.baselines — eight methods compared in the revised paper.

    NL2T        : proposed
    ISAC-MAC    : Duan et al., IEEE IoT-J 2026
    ETTOR-RL    : He et al., IEEE TMC 2025
    BGOR        : Wang et al., IEEE TCOM 2025
    EERPA       : Xu et al., IEEE Sensors J. 2025
    QTRU        : Khoshvaght et al., EAAI 2025
    DQN-ACMAC   : Rahman et al., JMSE 2025
    AUV-MR3D    : Xu et al., Ocean Eng. 2025
"""
from nl2t.baselines.nl2t_protocol import NL2TProtocol
from nl2t.baselines.isac_mac       import ISACMACProtocol
from nl2t.baselines.ettor_rl       import ETTORRLProtocol
from nl2t.baselines.bgor           import BGORProtocol
from nl2t.baselines.eerpa          import EERPAProtocol
from nl2t.baselines.qtru           import QTRUProtocol
from nl2t.baselines.dqn_acmac      import DQNACMACProtocol
from nl2t.baselines.auv_mr3d       import AUVMR3DProtocol

BASELINES = {
    "ISAC-MAC":  ISACMACProtocol,
    "ETTOR-RL":  ETTORRLProtocol,
    "BGOR":      BGORProtocol,
    "EERPA":     EERPAProtocol,
    "QTRU":      QTRUProtocol,
    "DQN-ACMAC": DQNACMACProtocol,
    "AUV-MR3D":  AUVMR3DProtocol,
}
__all__ = ["NL2TProtocol"] + list(BASELINES.values()) + ["BASELINES"]
