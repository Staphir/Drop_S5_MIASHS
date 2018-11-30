# ==============================================================================
"""GravityGrid : a generic rectangular grid with gravity"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # basic implementation without checking nor encapsulation
__date__    = "2018-11-15"
__usage__   = ""
# ------------------------------------------------------------------------------
from ezCLI import testcode, grid as str_grid
# ------------------------------------------------------------------------------
class GravityGrid(object):
  """a generic rectangular grid with gravity"""
  # ----------------------------------------------------------------------------
  def __init__(self, row=1, col=1, none=None):
    """initialize 'self' with provided arguments"""
    self.row, self.col, self.none, self.size = row, col, none, row*col
    self._grid = [[self.none for r in range(row)] for c in range(col)]
  # ----------------------------------------------------------------------------
  def __repr__(self):
    """return object representation of 'self'"""
    name, row, col, none = type(self).__name__, self.row, self.col, self.none
    return "%s(row=%r, col=%r, none=%r)" % (name, row, col, none)
  # ----------------------------------------------------------------------------
  def __eq__(self, peer):
    """test equality between 'self' and 'peer'"""
    return repr(self) == repr(peer) and self() == peer()
  # ----------------------------------------------------------------------------
  def __str__(self):
    """return a string representation of 'self'"""
    return str_grid([[self._grid[col][self.row-row-1]
      for col in range(self.col)] for row in range(self.row)])
  # ----------------------------------------------------------------------------
  def __call__(self, *items):
    """get grid as a 2D list or set grid from a 1D tuple of items"""
    if len(items): # 'items' contains a tuple of items to be inserted into grid
      for n, item in enumerate(items[:self.size]): # loop over items
        self._grid[n//self.row][n%self.row] = item
    return self._grid
   # ---------------------------------------------------------------------------
  def __len__(self):
    """return length of 'self' (i.e. number of non-empty items)"""
    return len([item for item in self if item != self.none])
  # ----------------------------------------------------------------------------
  def __iter__(self):
    """generate iterator over the grid items"""
    return iter(sum(self._grid, [])) # convert list from 2D to 1D then iterate
  # ----------------------------------------------------------------------------
  def __getitem__(self, col):
    """x.__getitem__(col) <==> x[col]"""
    return self._grid[col]
  # ----------------------------------------------------------------------------
  def __setitem__(self, col, item):
    """x.__setitem__(col, item) <==> x[col] = item"""
    items = self._grid[col]
    if items[-1] == self.none: # at least one empty item in selected row
      row = items.index(self.none); items[row] = item
  # ----------------------------------------------------------------------------
  def __delitem__(self, col):
    """x.__delitem__(col) <==> del x[col]"""
    items = self._grid[col]
    if items[0] != self.none: # at least one non empty item in selected row
      row = items.index(self.none); items[row-1] = self.none
  # ----------------------------------------------------------------------------
  def clone(self):
    """return clone of 'self'"""
    return eval(repr(self))
  # ----------------------------------------------------------------------------
  def copy(self):
    """return copy of 'self'"""
    peer = self.clone()
    for col in range(self.col): peer[col][:] = self[col]
    return peer
  # ----------------------------------------------------------------------------
  def clear(self):
    """reset all the items to 'self.none'"""
    cols, rows, none = range(self.col), range(self.row), self.none
    self._grid = [[none for row in rows] for col in cols]; return self()
  # ----------------------------------------------------------------------------
  def gravity(self):
    """apply gravity rules to current grid"""
    empty = [self.none] * self.row # create whole column of empty items
    for col in range(self.col): # loop over cols and apply gravity to items
      fall = [item for item in self._grid[col] if item != self.none] + empty
      self._grid[col] = fall[:self.row] # replace current col with fallen items
  # ----------------------------------------------------------------------------
  def hflip(self):
    """flip the grid horizontally"""
    self._grid.reverse(); return self() # reverse order of columns
  # ----------------------------------------------------------------------------
  def vflip(self):
    """flip the grid vertically"""
    for col in self._grid: col.reverse() # reverse order of rows, col by col
    self.gravity(); return self() # apply gravity before returning grid
  # ----------------------------------------------------------------------------
  def hroll(self, n=1):
    """roll the grid horizontally by 'n' steps"""
    self._grid[:] = self._grid[-n:] + self._grid[:-n]; return self()
  # ----------------------------------------------------------------------------
  def vroll(self, n=1):
    """roll the grid vertically by 'n' steps"""
    for col in self._grid: col[:] = col[-n:] + col[:-n]
    self.gravity(); return self()
  # ----------------------------------------------------------------------------
  def lpush(self, n=0):
    """push the columns to the left (starting from row 'n')"""
    p, grid = 0, self._grid
    for q in range(self.col):
      if grid[q][n] == self.none: continue # skip cols with less than 'n' items
      grid[p][n:], grid[q][n:] = grid[q][n:], grid[p][n:]; p += 1
    self.gravity(); return self()
  # ----------------------------------------------------------------------------
  def rpush(self, n=0):
    """push the columns to the right (starting from row 'n')"""
    self.hflip(); self.lpush(n); self.hflip() # rpush <=> hflip o lpush o hflip
    return self()
  # ----------------------------------------------------------------------------
  def lslide(self):
    """slide the items to the left"""
    for n in range(self.row): self.lpush(n) # lpush items row by row
    return self()
  # ----------------------------------------------------------------------------
  def rslide(self):
    """slide the items to the right"""
    self.hflip(); self.lslide(); self.hflip() # rslide <=> hflip o lslde o hflip
    return self()
# ==============================================================================
if __name__ == "__main__": # test code for class "GravityGrid"
  code = r'''
a = GravityGrid(3, 6, 0)
a, a.row, a.col, a.none, len(a)
a()
str(a)
a(1,2,3,4,5,6,7,8,9)
len(a)
str(a)
a.clear()
a[0] = a[2] = a[5] = 1; a[0] = a[3] = 2; a[0] = a[5] = 3; a[0] = a[2] = 9
len(a)
str(a)
a.hflip()
a.vflip()
a.hroll(-1)
a.vroll(2)
a.lpush()
a.rpush()
a.lslide()
a.rslide()
'''; testcode(code)
# ==============================================================================
