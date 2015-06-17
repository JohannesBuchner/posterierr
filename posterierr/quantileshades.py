import scipy.stats
import matplotlib.pyplot as plt
import numpy

class Shade(object):
	"""
	The Shade class allows plotting of model predictions as calculated from a chain.
	
	:param: x the independent variable
	
	call add to add predictions from the chain.
	
	Example:
	
	x = numpy.linspace(0, 1, 100)
	shade = Shade(x)
	for c in chain:
		shade.add(c[0] * x + c[1])
	shade.line()
	shade.shade()
	plt.show()
	
	"""
	def __init__(self, x, shadeargs={}, lineargs={}):
		self.x = x
		self.ys = []
		self.shadeargs = shadeargs
		self.lineargs = lineargs
	def add(self, y):
		""" add a possible prediction """
		self.ys.append(y)
	def set_shadeargs(self, **kwargs):
		self.shadeargs = kwargs
	def set_lineargs(self, **kwargs):
		self.lineargs = kwargs
	def shade(self, q=0.341, **kwargs):
		""" Use the stored predictions to plot a shaded region
		using 0.5-q and 0.5+q as limits. """
		assert len(self.ys) > 0, self.ys
		shadeargs = dict(self.shadeargs)
		shadeargs.update(kwargs)
		lo = scipy.stats.mstats.mquantiles(self.ys, 0.5 - q, axis=0)[0]
		hi = scipy.stats.mstats.mquantiles(self.ys, 0.5 + q, axis=0)[0]
		plt.fill_between(self.x, lo, hi, **shadeargs)
	def line(self, **kwargs):
		""" Use the stored predictions to plot the median """
		assert len(self.ys) > 0, self.ys
		lineargs = dict(self.lineargs)
		lineargs.update(kwargs)
		mid = scipy.stats.mstats.mquantiles(self.ys, 0.5, axis=0)[0]
		plt.plot(self.x, mid, **lineargs)

__doc__ = Shade.__doc__
__all__ = ['Shade']

