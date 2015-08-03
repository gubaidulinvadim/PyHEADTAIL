# monkey patching default classes with GPU variants
# is done on importing this module!

from skcuda.misc import mean, std, diff
from pycuda import gpuarray

from ..particles import particles as def_particles
from ..particles import slicing as def_slicing

# Particles rebindings for GPU
from .particles import ParticlesGPU

def_particles.Particles = ParticlesGPU
def_particles.mean = lambda *args, **kwargs: mean(*args, **kwargs).get()
def_particles.std = lambda *args, **kwargs: std(*args, **kwargs).get()

# Slicing rebindings for GPU
# def_slicing.min_ = lambda *args, **kwargs: gpuarray.min(*args, **kwargs).get()
# def_slicing.max_ = lambda *args, **kwargs: gpuarray.max(*args, **kwargs).get()
# def_slicing.diff = diff

from .slicing import SlicerGPU

# # to be replaced: find a better solution than monkey patching base classes!
# # (to solve the corresponding need to replace all inheriting classes' parent!)
# def_slicing.Slicer = SlicerGPU
# def_slicing.UniformBinSlicer.__bases__ = (SlicerGPU,)
