# ==============================================================================
"""GRID : a generic rectangular grid"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # store grid cells as a 2D hidden list
__date__    = "2017-10-15"
__usage__   = ""
# ------------------------------------------------------------------------------
from ezCLI import testcode, grid as str_grid
# ------------------------------------------------------------------------------
class grid(object):
  """a generic rectangular grid"""
  # ----------------------------------------------------------------------------
  def __init__(self, row=1, col=1, none=None):
    """initialize 'self' with provided arguments"""
    self.row, self.col, self.none, self.size = row, col, none, row*col
    self._grid = [[self.none for c in range(col)] for r in range(row)]
    
  # ----------------------------------------------------------------------------
  def __repr__(self):
    """return object representation for 'self'"""
    name, row, col, none = type(self).__name__, self.row, self.col, self.none
    return "%s(row=%r, col=%r, none=%r)" % (name, row, col, none)
  # ----------------------------------------------------------------------------
  def __eq__(self, peer):
    """test equality between 'self' and 'peer'"""
    return repr(self) == repr(peer) and self() == peer()
  # ----------------------------------------------------------------------------
  def __call__(self, *items):
    """get grid as a 2D tuple or set grid from a 1D tuple of items"""
    if len(items): # 'items' contains a tuple of items to be inserted into grid
      for n, item in enumerate(items[:self.size]): # loop over items
        self._grid[n//self.col][n%self.col] = item
    return tuple(tuple(row) for row in self._grid) # return cells as a tuple
  # ----------------------------------------------------------------------------
  def __str__(self):
    """return a string representation of 'self'"""
    return str_grid(self._grid)
   # ----------------------------------------------------------------------------
  def __len__(self):
    """return length of 'self' (i.e. number of non-empty cells)"""
    return len([cell for cell in self if cell != self.none])
  # ----------------------------------------------------------------------------
  def __iter__(self):
    """generate iterator over the grid cells"""
    return iter(sum(self._grid, [])) # convert 2D list into 1D list then iterate
  # ----------------------------------------------------------------------------
  def __getitem__(self, box):
    """x.__getitem__(box) <==> x[box] where 'box' is a tuple of int or slice"""
    rows, cols = box; grid = self()
    if isinstance(rows, int): return grid[rows][cols]
    return tuple(row[cols] for row in grid[rows])
  # ----------------------------------------------------------------------------
  def __setitem__(self, box, item):
    """x.__setitem__(box, items) <==> x[box] = item"""
    rows, cols = box; rows, cols = range(self.row)[rows], range(self.col)[cols]
    for row in (rows if isinstance(rows, range) else [rows]):
      for col in (cols if isinstance(cols, range) else [cols]):
        self._grid[row][col] = item
  # ----------------------------------------------------------------------------
  def __delitem__(self, box):
    """x.__delitem__(box) <==> del x[box]"""
    self[box] = self.none
  # ----------------------------------------------------------------------------
  def clone(self):
    """return clone of 'self'"""
    return eval(repr(self))
  # ----------------------------------------------------------------------------
  def copy(self):
    """return copy of 'self'"""
    peer = self.clone(); peer(*self); return peer
  # ----------------------------------------------------------------------------
  def clear(self):
    """reset all the items to 'self.none'"""
    self[:,:] = self.none; return self()
# # ==============================================================================
# if __name__ == "__main__":
#   code = r'''
# a, b = grid(), grid(3, 6, 0)
# a, a.row, a.col, a.none, a.size
# b, b.row, b.col, b.none, b.size
# a()
# str(a)
# b()
# str(b)
# a('A','B','C','D','E'), b(1,2,3,4,5,6,7,8,9)
# str(a)
# str(b)
# len(a), len(b)
# tuple(b)
# list(b)
# a[0,0], b[0,-1], b[1,:], b[:,1]
# a.clear(), b.clear()
# b[1,0] = b[1,-1] = 1; b[0,:] = 2; b[:,1] = 3; b[1:,2:4] = 4; b[-1,::5] = 5
# str(b)
# c, d = b.clone(), b.copy()
# c, d
# c()
# d()
# b is c, b == c, b is d, b == d
# '''; testcode(code)
# # ==============================================================================
