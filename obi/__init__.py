"""
obi: python organizers, builders, and inspectors
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
    
    
ToDo:
   

For Developers:

As with all of my packages, I use Google-style docstrings and follow the Google 
Python Style Guide (https://google.github.io/styleguide/pyguide.html) with two 
notable exceptions:
    1) I always add spaces around '='. This is because I find it more readable 
        and it is practically the norm with type annotations adding the spaces
        to function and method signatures. I realize that this will seem alien
        to many coders, but it is far easier on my eyes.
    2) I've expanded the Google exception for importing multiple items from one
        package from just 'typing' to also include 'collections.abc'. This is
        because, as of python 3.9, many of the type annotations in 'typing'
        are being depreciated and have already been combined with the similarly
        named types in 'collections.abc'. I except Google will make this change
        at some point in the near future.

My packages lean heavily toward over-documentation and verbosity. This is
designed to make them more accessible to beginnning coders and generally more 
usable. The one exception to that general rule is unit tests, which hopefully 
are clear enough to not require further explanation. If there is any area of the 
documentation that could be made clearer, please don't hesitate to email me or
any other package maintainer - I want to ensure the package is as accessible and 
useful as possible.
     
"""
from __future__ import annotations

__version__ = '0.1.0'

__package__ = 'obi'

__author__ = 'Corey Rayburn Yung'


from . import builders
from . import inspectors
from . import organizers
from .builders.base import *
from .builders.composite import *
from .builders.foundry import *
from .builders.form import *
from .builders.graph import *
from .builders.hybrid import *
from .builders.mapping import *
from .builders.registry import *
from .builders.sequence import *
from .builders.trait import *
from .inspectors.check import *
from .inspectors.clock import *
from .inspectors.examiner import *
from .inspectors.report import *
from .inspectors.represent import *
from .organizers.convert import *
from .organizers.formats import *
from .organizers.lazy import *
from .organizers.manager import *
from .organizers.modify import *
from .organizers.validate import *
