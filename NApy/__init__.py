from .post_processing import *
from .post_processing import help as help_general
from .matrix_methods.help import dict2
from .matrix_methods.help import help as help_matrix
from .ODE_solvers.help import dict1
from .ODE_solvers.help import help as help_ode

def help(kw = ""):
    help_general(kw)
    help_matrix(kw)
    help_ode(kw)
    return 0
