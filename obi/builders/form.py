"""
form: internal storage formats for graphs
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2020-2022, Corey Rayburn Yung
License: Apache-2.0

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Contents:
    Adjacency (mapping.Dictionary, composite.Graph): a graph stored as an adjacency 
        list.
    Edges (sequences.Listing, composite.Graph): a graph stored as an edge list.
    Matrix (sequences.Listing, composite.Graph): a graph stored as an adjacency 
        matrix.
          
To Do:
    Integrate Kinds system when it is finished.
    
"""
from __future__ import annotations
import abc
import collections
from collections.abc import (
    Collection, Hashable, MutableMapping, MutableSequence, Sequence, Set)
import dataclasses
from typing import Any, ClassVar, Optional, Type, TYPE_CHECKING, Union

from . import composite
from . import mapping
from . import sequence
from ..inspectors import check
from ..organizers import convert


@dataclasses.dataclass
class Adjacency(mapping.Dictionary, composite.Graph):
    """Base class for adjacency-list graphs.
    
    Args:
        contents (MutableMapping[composite.Node, Set[composite.Node]]): keys 
            are nodes and values are sets of nodes (or hashable representations 
            of nodes). Defaults to a defaultdict that has a set for its value 
            type.
                                      
    """  
    contents: MutableMapping[composite.Node, Set[composite.Node]] = (
        dataclasses.field(
            default_factory = lambda: collections.defaultdict(set)))
   
    """ Properties """

    @property
    def adjacency(self) -> Adjacency:
        """Returns the stored graph as an Adjacency."""
        return self.contents

    @property
    def edges(self) -> Edges:
        """Returns the stored graph as an Edges."""
        return convert.adjacency_to_edges(item = self.contents)

    @property
    def linear(self) -> Linear:
        """Returns the stored graph as a Linear."""
        return convert.adjacency_to_linear(item = self.contents)
              
    @property
    def matrix(self) -> Matrix:
        """Returns the stored graph as a Matrix."""
        return convert.adjacency_to_matrix(item = self.contents)
           
    @property
    def tree(self) -> Tree:
        """Returns the stored graph as a Tree."""
        return convert.adjacency_to_tree(item = self.contents)
            
    """ Class Methods """
    
    @classmethod
    def from_adjacency(cls, item: Adjacency) -> Adjacency:
        """Creates an Adjacency instance from an Adjacency."""
        return cls(contents = item)
    
    @classmethod
    def from_edges(cls, item: Edges) -> Adjacency:
        """Creates an Adjacency instance from an Edges."""
        return cls(contents = convert.edges_to_adjacency(item = item))
    
    @classmethod
    def from_linear(cls, item: Linear) -> Adjacency:
        """Creates an Edges instance from a Linear."""
        return cls(contents = convert.linear_to_adjacency(item = item))
            
    @classmethod
    def from_matrix(cls, item: Matrix) -> Adjacency:
        """Creates an Adjacency instance from a Matrix."""
        return cls(contents = convert.matrix_to_adjacency(item = item))
             
    @classmethod
    def from_tree(cls, item: Tree) -> Adjacency:
        """Creates an Adjacency instance from a Tree."""
        return cls(contents = convert.tree_to_adjacency(item = item))
                   
    """ Dunder Methods """
    
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        """Returns whether 'instance' meets criteria to be a subclass.

        Args:
            instance (object): item to test as an instance.

        Returns:
            bool: whether 'instance' meets criteria to be a subclass.
            
        """
        return check.is_adjacency(item = instance)


@dataclasses.dataclass
class Edges(sequence.Listing, composite.Graph):
    """Base class for edge-list graphs.

    Args:
        contents (MutableSequence[composite.Edge]): list of edges. Defaults to 
            an empty list.
                                      
    """   
    contents: MutableSequence[composite.Edge] = dataclasses.field(
        default_factory = list)
   
    """ Properties """

    @property
    def adjacency(self) -> Adjacency:
        """Returns the stored graph as an Adjacency."""
        return convert.edges_to_adjacency(item = self.contents)

    @property
    def edges(self) -> Edges:
        """Returns the stored graph as an Edges."""
        return self.contents

    @property
    def linear(self) -> Linear:
        """Returns the stored graph as a Linear."""
        return convert.edges_to_linear(item = self.contents)
           
    @property
    def matrix(self) -> Matrix:
        """Returns the stored graph as a Matrix."""
        return convert.edges_to_matrix(item = self.contents)
           
    @property
    def tree(self) -> Tree:
        """Returns the stored graph as a Tree."""
        return convert.edges_to_tree(item = self.contents)
            
    """ Class Methods """
    
    @classmethod
    def from_adjacency(cls, item: Adjacency) -> Edges:
        """Creates an Edges instance from an Adjacency."""
        return cls(contents = convert.adjacency_to_edges(item = item))
    
    @classmethod
    def from_edges(cls, item: Edges) -> Edges:
        """Creates an Edges instance from an Edges."""
        return cls(contents = item)
    
    @classmethod
    def from_linear(cls, item: Linear) -> Edges:
        """Creates an Edges instance from a Linear."""
        return cls(contents = convert.linear_to_edges(item = item))
            
    @classmethod
    def from_matrix(cls, item: Matrix) -> Edges:
        """Creates an Edges instance from a Matrix."""
        return cls(contents = convert.matrix_to_edges(item = item))
             
    @classmethod
    def from_tree(cls, item: Tree) -> Edges:
        """Creates an Edges instance from a Tree."""
        return cls(contents = convert.tree_to_edges(item = item))
                
    """ Dunder Methods """
           
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        """Returns whether 'instance' meets criteria to be a subclass.

        Args:
            instance (object): item to test as an instance.

        Returns:
            bool: whether 'instance' meets criteria to be a subclass.
            
        """
        return check.is_edges(item = instance)
    
    
@dataclasses.dataclass
class Linear(sequence.Hybrid, composite.Graph):
    """Base class for linear graphs.
    
    Args:
        contents (MutableSequence[composite.Node]): list of nodes. Defaults to 
            an empty list.
                                      
    """   
    contents: MutableSequence[composite.Node] = dataclasses.field(
        default_factory = list)
                                
    """ Properties """

    @property
    def adjacency(self) -> Adjacency:
        """Returns the stored graph as an Adjacency."""
        return convert.matrix_to_adjacency(item = self.contents)

    @property
    def edges(self) -> Edges:
        """Returns the stored graph as an Edges."""
        return convert.matrix_to_edges(item = self.contents)

    @property
    def linear(self) -> Linear:
        """Returns the stored graph as a Linear."""
        return self.contents
           
    @property
    def matrix(self) -> Matrix:
        """Returns the stored graph as a Matrix."""
        return convert.linear_to_matrix(item = self.contents)
           
    @property
    def tree(self) -> Tree:
        """Returns the stored graph as a Tree."""
        return convert.linear_to_tree(item = self.contents)
            
    """ Class Methods """
    
    @classmethod
    def from_adjacency(cls, item: Adjacency) -> Linear:
        """Creates a Linear instance from an Adjacency."""
        return cls(contents = convert.adjacency_to_linear(item = item))
    
    @classmethod
    def from_edges(cls, item: Edges) -> Linear:
        """Creates a Linear instance from an Edges."""
        return cls(contents = convert.edges_to_linear(item = item))
    
    @classmethod
    def from_linear(cls, item: Linear) -> Linear:
        """Creates a Linear instance from a Linear."""
        return cls(contents = item)
            
    @classmethod
    def from_matrix(cls, item: Matrix) -> Linear:
        """Creates a Linear instance from a Matrix."""
        return cls(contents = convert.matrix_to_linear(item = item))
             
    @classmethod
    def from_tree(cls, item: Tree) -> Linear:
        """Creates a Linear instance from a Tree."""
        return cls(contents = convert.tree_to_linear(item = item))
                    
    """ Dunder Methods """
        
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        """Returns whether 'instance' meets criteria to be a subclass.

        Args:
            instance (object): item to test as an instance.

        Returns:
            bool: whether 'instance' meets criteria to be a subclass.
            
        """
        return check.is_linear(item = instance)
       
    
@dataclasses.dataclass
class Matrix(sequence.Listing, composite.Graph):
    """Base class for adjacency-matrix graphs.
    
    Args:
        contents (Sequence[Sequence[int]]): a list of list of integers 
            indicating edges between nodes in the matrix. Defaults to an empty
            list.
        labels (Sequence[Hashable]): names of nodes in the matrix. 
            Defaults to an empty list.
                                      
    """  
    contents: MutableSequence[MutableSequence[int]] = dataclasses.field(
        default_factory = list)
    labels: MutableSequence[Hashable] = dataclasses.field(
        default_factory = list)
   
    """ Properties """

    @property
    def adjacency(self) -> Adjacency:
        """Returns the stored graph as an Adjacency."""
        return convert.matrix_to_adjacency(item = self.contents)

    @property
    def edges(self) -> Edges:
        """Returns the stored graph as an Edges."""
        return convert.matrix_to_edges(item = self.contents)

    @property
    def linear(self) -> Linear:
        """Returns the stored graph as a Linear."""
        return convert.matrix_to_linear(item = self.contents)
           
    @property
    def matrix(self) -> Matrix:
        """Returns the stored graph as a Matrix."""
        return self.contents
           
    @property
    def tree(self) -> Tree:
        """Returns the stored graph as a Tree."""
        return convert.matrix_to_tree(item = self.contents)
         
    """ Class Methods """
    
    @classmethod
    def from_adjacency(cls, item: Adjacency) -> Matrix:
        """Creates a Matrix instance from an Adjacency."""
        return cls(contents = convert.adjacency_to_matrix(item = item))
    
    @classmethod
    def from_edges(cls, item: Edges) -> Matrix:
        """Creates a Matrix instance from an Edges."""
        return cls(contents = convert.edges_to_matrix(item = item))
    
    @classmethod
    def from_linear(cls, item: Linear) -> Matrix:
        """Creates a Graph instance from a Linear."""
        return cls(contents = convert.linear_to_matrix(item = item))
            
    @classmethod
    def from_matrix(cls, item: Matrix) -> Matrix:
        """Creates a Matrix instance from a Matrix."""
        return cls(contents = item[0], labels = item[1])
             
    @classmethod
    def from_tree(cls, item: Tree) -> Matrix:
        """Creates a Matrix instance from a Tree."""
        return cls(contents = convert.tree_to_matrix(item = item))
               
    """ Dunder Methods """
        
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        """Returns whether 'instance' meets criteria to be a subclass.

        Args:
            instance (object): item to test as an instance.

        Returns:
            bool: whether 'instance' meets criteria to be a subclass.
            
        """
        return check.is_matrix(item = instance)


@dataclasses.dataclass # type: ignore
class Tree(sequence.Hybrid, composite.Graph, composite.Node):
    """Base class for an tree data structures.
    
    The Tree class uses a Hybrid instead of a linked list for storing children
    nodes to allow easier access of nodes further away from the root. For
    example, a user might use 'a_tree["big_branch"]["small_branch"]["a_leaf"]' 
    to access a desired node instead of 'a_tree[2][0][3]' (although the latter
    access technique is also supported).
    
    There are several differences between a Tree and a Graph in piles:
        1) Graphs are more flexible. Trees must have 1 root, are directed, and
            each node can have only 1 parent node.
        2) Edges are only implicit in a Tree whereas they are explicit in a 
            Graph. This allows for certain methods and functions surrounding
            iteration and traversal to be faster.
        3) As the size of the data structure increases, a Tree should use less
            memory because the data about relationships between nodes is not
            centrally maintained (as with an adjacency matrix). This decreases
            access time to non-consecutive nodes, but is more efficient for 
            larger data structures.
        
    Args:
        contents (MutableSequence[Node]): list of stored Tree or other 
            Node instances. Defaults to an empty list.
        name (Optional[str]): name of Tree node which should match a parent 
            tree's key name corresponding to this Tree node. All nodes in a Tree
            must have unique names. The name is used to make all Tree nodes 
            hashable and capable of quick comparison. Defaults to None, but it
            should not be left as None when added to a Tree.
        parent (Optional[Tree]): parent Tree, if any. Defaults to None.
  
    """
    contents: MutableSequence[composite.Node] = dataclasses.field(
        default_factory = list)
    name: Optional[str] = None
    parent: Optional[Tree] = None 
    
    """ Properties """

    @property
    def adjacency(self) -> Adjacency:
        """Returns the stored graph as an Adjacency."""
        return convert.tree_to_adjacency(item = self.contents)

    @property
    def edges(self) -> Edges:
        """Returns the stored graph as an Edges."""
        return convert.tree_to_edges(item = self.contents)

    @property
    def linear(self) -> Linear:
        """Returns the stored graph as a Linear."""
        return convert.tree_to_linear(item = self.contents)
           
    @property
    def matrix(self) -> Matrix:
        """Returns the stored graph as a Matrix."""
        return convert.tree_to_matrix(item = self.contents)
           
    @property
    def tree(self) -> Tree:
        """Returns the stored graph as a Tree."""
        return self.contents
           
    """ Class Methods """
    
    @classmethod
    def from_adjacency(cls, item: Adjacency) -> Tree:
        """Creates a Tree instance from an Adjacency."""
        return cls(contents = convert.adjacency_to_tree(item = item))
    
    @classmethod
    def from_edges(cls, item: Edges) -> Tree:
        """Creates a Tree instance from an Edges."""
        return cls(contents = convert.edges_to_tree(item = item))
    
    @classmethod
    def from_linear(cls, item: Linear) -> Tree:
        """Creates a Tree instance from a Linear."""
        return cls(contents = convert.linear_to_tree(item = item))
            
    @classmethod
    def from_matrix(cls, item: Matrix) -> Tree:
        """Creates a Tree instance from a Matrix."""
        return cls(contents = convert.matrix_to_tree(item = item))
            
    @classmethod
    def from_tree(cls, item: Tree) -> Tree:
        """Creates a Tree instance from a Tree."""
        return cls(contents = item)
        
    @property
    def children(self) -> MutableSequence[composite.Node]:
        """Returns child nodes of this Node."""
        return self.contents
    
    @children.setter
    def children(self, value: MutableSequence[composite.Node]) -> None:
        """Sets child nodes of this Node."""
        self.contents = value
        return
           
    """ Dunder Methods """
        
    @classmethod
    def __instancecheck__(cls, instance: object) -> bool:
        """Returns whether 'instance' meets criteria to be a subclass.

        Args:
            instance (object): item to test as an instance.

        Returns:
            bool: whether 'instance' meets criteria to be a subclass.
            
        """
        return check.is_tree(item = instance)
    
    # def __add__(self, other: composite.Graph) -> None:
    #     """Adds 'other' to the stored tree using the 'append' method.

    #     Args:
    #         other (composite.Graph): another Tree, an adjacency list, an 
    #             edge list, an adjacency matrix, or one or more nodes.
            
    #     """
    #     self.append(item = other)     
    #     return 

    # def __radd__(self, other: composite.Graph) -> None:
    #     """Adds 'other' to the stored tree using the 'prepend' method.

    #     Args:
    #         other (composite.Graph): another Tree, an adjacency list, an 
    #             edge list, an adjacency matrix, or one or more nodes.
            
    #     """
    #     self.prepend(item = other)     
    #     return 

    # def __missing__(self) -> dict[str, Tree]:
    #     """[summary]

    #     Returns:
    #         dict[str, Tree]: [description]
            
    #     """
    #     return self.__class__()
    