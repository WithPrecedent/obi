"""
trait: characteristics of graphs
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
    Directed (Protocol): a directed graph with unweighted edges.
        
To Do:

    
"""
from __future__ import annotations
import abc
import dataclasses
from typing import Any, Optional, Protocol, Type, TYPE_CHECKING, Union

from ..organizers import convert


if TYPE_CHECKING:
    from . import composite
    
    
@dataclasses.dataclass
class Directed(Protocol):
    """Base class for directed graph data structures."""  
    
    """ Required Subclass Properties """
        
    @abc.abstractproperty
    def endpoint(self) -> Union[composite.Node, composite.Nodes]:
        """Returns the endpoint(s) of the stored graph."""
        pass
 
    @abc.abstractproperty
    def root(self) -> Union[composite.Node, composite.Nodes]:
        """Returns the root(s) of the stored graph."""
        pass
        
    """ Required Subclass Methods """
    
    @abc.abstractmethod
    def append(
        self, 
        item: Union[composite.Node, composite.Graph], 
        *args: Any, 
        **kwargs: Any) -> None:
        """Appends 'item' to the endpoint(s) of the stored graph.

        Args:
            item (Union[composite.Node, composite.Graph]): a Node or Graph to 
                add to the stored graph.
                
        """
        pass
    
    @abc.abstractmethod
    def prepend(
        self, 
        item: Union[composite.Node, composite.Graph], 
        *args: Any, 
        **kwargs: Any) -> None:
        """Prepends 'item' to the root(s) of the stored graph.

        Args:
            item (Union[composite.Node, composite.Graph]): a Node or Graph to 
                add to the stored graph.
                
        """
        pass
    
    @abc.abstractmethod
    def walk(
        self, 
        start: Optional[composite.Node] = None,
        stop: Optional[composite.Node] = None, 
        path: Optional[composite.Linear] = None,
        *args: Any, 
        **kwargs: Any) -> composite.Linear:
        """Returns path in the stored graph from 'start' to 'stop'.
        
        Args:
            start (Optional[composite.Node]): Node to start paths from. 
                Defaults to None. If it is None, 'start' should be assigned to 
                'root'.
            stop (Optional[composite.Node]): Node to stop paths at. 
                Defaults to None. If it is None, 'start' should be assigned to 
                'endpoint'.
            path (Optional[composite.Linear]): a path from 'start' to 'stop'. 
                Defaults to None. This parameter is used for recursively
                determining a path.

        Returns:
            composite.Linear: path(s) through the graph. 
                            
        """
        pass
    
    """ Dunder Methods """

    def __add__(self, other: composite.Graph) -> None:
        """Adds 'other' to the stored graph using 'append'.

        Args:
            other (Union[composite.Graph]): another graph to add to the current 
                one.
            
        """
        self.append(item = other)     
        return 

    def __radd__(self, other: composite.Graph) -> None:
        """Adds 'other' to the stored graph using 'prepend'.

        Args:
            other (Union[composite.Graph]): another graph to add to the current 
                one.
            
        """
        self.prepend(item = other)     
        return 
  