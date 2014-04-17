#!/usr/bin/env python
import sys, os; from os import environ as env

LIBCLANG_PATH = "./libclang-py"
if env.has_key('TM_BUNDLE_SUPPORT'):
  LIBCLANG_PATH = env['TM_BUNDLE_SUPPORT']+"/libclang-py"  
sys.path.append(LIBCLANG_PATH)
from clang.cindex import Index, Cursor, CursorKind, Config

Config.set_library_path('/opt/llvm/head/lib')

# PROJECT_DIR = '/Users/bholt/dev/test'

DEBUG = False

class MateIndex:
  
  def __init__(self):
    if env.has_key('TM_PROJECT_DIRECTORY'):
      self.project_dir = env['TM_PROJECT_DIRECTORY']
    else:
      self.project_dir = "."
    
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
  
  def find(self, node=None, kinds=set(), result=list(), local_only=True):
    global DEBUG
    
    if not node:
      node = self.tu.cursor
    # if DEBUG and node.kind.is_declaration():
      # print node.spelling, node.kind
      
    if node.kind in kinds:
      if (not local_only) or self.project_dir in str(node.location.file):
        # print node.spelling, node.kind, node.location.file
        result.append({
          'name': node.spelling,
          'file': str(node.location.file),
          'line': node.location.line
        })
    
    for c in node.get_children():
      self.find(c, kinds, result, local_only)
    
    return result
  
  def parse(self, fname):
    self.tu = self.index.parse(fname)
    
    
if __name__ == "__main__":
  DEBUG = True
  import pprint
  
  idx = MateIndex()
  idx.parse('test/test.cpp')
    
  idx.find(kinds=set([CursorKind.VAR_DECL]))
  
  # import ipdb; ipdb.set_trace()
