"""
traits: characteristics of graphs
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
    Directed (ABC): a directed graph with unweighted edges.
        
To Do:
    Complete Network which will use an adjacency matrix for internal storage.
    
"""
from __future__ import annotations
import abc
import dataclasses
from typing import Any, Optional, Type, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import composite
    from . import hybrid
    from . import tree
    
    
@dataclasses.dataclass
class Directed(abc.ABC):
    """Base class for directed graph data structures."""  
    
    """ Required Subclass Properties """
        
    @abc.abstractproperty
    def endpoint(self) -> Optional[Union[composite.Node, composite.Nodes]]:
        """Returns the endpoint(s) of the stored composite object."""
        pass
 
    @abc.abstractproperty
    def root(self) -> Optional[Union[composite.Node, composite.Nodes]]:
        """Returns the root(s) of the stored composite object."""
        pass
        
    @abc.abstractproperty
    def pipeline(self) -> hybrid.Pipeline:
        """Returns the stored composite object as a Pipeline."""
        pass
        
    @abc.abstractproperty
    def pipelines(self) -> hybrid.Pipelines:
        """Returns the stored composite object as a Pipelines."""
        pass
            
    @abc.abstractproperty
    def tree(self) -> tree.Tree:
        """Returns the stored composite object as a Tree."""
        pass
                 
    """ Required Subclass Class Methods """
    
    @abc.abstractclassmethod
    def from_pipeline(cls, item: hybrid.Pipeline) -> Directed:
        """Creates an instance from a Pipeline."""
        pass
    
    @abc.abstractclassmethod
    def from_pipelines(cls, item: hybrid.Pipelines) -> Directed:
        """Creates an instance from a Pipelines."""
        pass

    @abc.abstractclassmethod
    def from_tree(cls, item: tree.Tree) -> Directed:
        """Creates an instance from a Tree."""
        pass
                 
    """ Required Subclass Methods """
    
    @abc.abstractmethod
    def append(
        self, 
        item: Union[composite.Node, composite.Graph], 
        *args: Any, 
        **kwargs: Any) -> None:
        """Appends 'item' to the endpoint(s) of the stored composite object.

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
        """Prepends 'item' to the root(s) of the stored composite object.

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
        path: Optional[hybrid.Pipeline] = None,
        return_pipelines: bool = True, 
        *args: Any, 
        **kwargs: Any) -> Union[hybrid.Pipeline, hybrid.Pipelines]:
        """Returns path in the stored composite object from 'start' to 'stop'.
        
        Args:
            start (Optional[composite.Node]): Node to start paths from. 
                Defaults to None. If it is None, 'start' should be assigned to 
                'root'.
            stop (Optional[composite.Node]): Node to stop paths at. 
                Defaults to None. If it is None, 'start' should be assigned to 
                'endpoint'.
            path (Optional[hybrid.Pipeline]): a path from 'start' to 'stop'. 
                Defaults to None. This parameter is used for recursively
                determining a path.
            return_pipelines (bool): whether to return a Pipelines instance 
                (True) or a Pipeline instance (False). Defaults to True.

        Returns:
            Union[hybrid.Pipeline, hybrid.Pipelines]: path(s) through the 
                graph. If multiple paths are possible and 'return_pipelines' is 
                False, this method should return a Pipeline that includes all 
                such paths appended to each other. If multiple paths are 
                possible and 'return_pipelines' is True, a Pipelines instance 
                with all of the paths should be returned. Defaults to True.
                            
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

    # def __str__(self) -> str:
    #     """Returns prettier str representation of an instance.

    #     Returns:
    #         str: a formatted str of an instance.
            
    #     """
    #     return represent.beautify(item = self, package = 'bunches')  
    
    