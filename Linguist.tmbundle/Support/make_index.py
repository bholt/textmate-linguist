#!/usr/bin/env python
import sys, os
LIBCLANG_PATH = os.environ['TM_BUNDLE_SUPPORT']+"/libclang-py"
# LIBCLANG_PATH = '/Users/bholt/Library/Application Support/Avian/Bundles/ClangMate.tmbundle/Support/libclang-py'
sys.path.append(LIBCLANG_PATH)
from clang.cindex import Index, Cursor, CursorKind

# PROJECT_DIR = '/Users/bholt/dev/test'

DEBUG = False

class MateIndex:
  
  def __init__(self):
    self.project_dir = os.environ['TM_PROJECT_DIRECTORY']
    self.index = Index.create()
    self.type_kinds = set([CursorKind.STRUCT_DECL, CursorKind.CLASS_DECL, CursorKind.CLASS_TEMPLATE,CursorKind.TYPEDEF_DECL])
    
  def find_types(self, node=None, types=set()):
    global DEBUG
    
    if not node:
      node = self.tu.cursor
    # if DEBUG and node.kind.is_declaration():
      # print node.spelling, node.kind
      
    if node.kind in self.type_kinds:
      if self.project_dir in str(node.location.file):
        # print node.spelling, node.kind, node.location.file
        types.add(node.spelling)
    
    for c in node.get_children():
      self.find_types(c,types)
    
    return types
  
  def parse(self, fname):
    self.tu = self.index.parse(fname)
    
    
if __name__ == "__main__":
  DEBUG = True
  types = find_types(tu.cursor)
  print types
