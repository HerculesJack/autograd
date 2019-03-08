from __future__ import absolute_import
from . import chi2
from . import beta
from . import gamma
from . import norm
from . import poisson
from . import t
from . import kde

# Try block needed in case the user has an old version
# of scipy without multivariate_normal or dirichlet.

try:
    from . import multivariate_normal
except AttributeError:
    pass

try:
    from . import dirichlet
except AttributeError:
    pass
