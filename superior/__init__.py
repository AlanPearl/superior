"""
superior
Author: Alan Pearl

TODO:
    Ideally, superior would be a class that (1) inherits method
    from the parents of `thistype`, (2) can determine `thistype`
    and `obj` by default to be the current class and self
    respectively, and (3) supports a return value (although 
    honestly I'm not sure what it would return). This all sounds 
    like a lot of work though, so I probably won't actually work 
    on any of it, but anyone else is free to.
""" 

def superior(thistype, obj, method, *args, **kwargs):
    """
superior(thistype, obj, "method", *args, **kwargs)

A function to replace super(thistype, obj).method(*args, **kwargs)
i.e., getattr(super(thistype, obj), "method")(*args, **kwargs)

superior can ONLY call direct parents, but still keeps track of
the classes each method is bound to, ensuring that no class can
be used multiple times in the case of diamond inheritance.

Also notable, this function is compatible with classes within the
hierachy calling methods from their parent classes directly.
However, it is NOT compatible with classes within the hierarchy
using super() to call methods (but you know, nothing is compatible 
with super anyways).

**Note that superior requires a slight change of the standard MRO 
to a depth-first strategy, instead of the almost-depth-first
strategy of super**
    """
    if not obj in __supers__:
        # Add the object to our dictionary to keep track of 
        # the classes that it has already called.
        # This makes sure no class is called twice.
        __supers__[obj] = {obj.__class__}
        
        try:
            _superior(thistype.__bases__, obj, method, *args, **kwargs)
        except:
            if obj in __supers__:
                del __supers__[obj]
            raise
        else:
            del __supers__[obj]
    
    else:
        _superior(thistype.__bases__, obj, method, *args, **kwargs)

def _superior(parents, obj, method, *args, **kwargs):
    for nexttype in parents:
        if not nexttype in __supers__[obj]:
            __supers__[obj].add(nexttype)
            if hasattr(nexttype, method):
                getattr(nexttype, method)(obj, *args, **kwargs)


def superiorMRO(thistype):
    """
superiorMRO(thistype)

A useful function which returns the superior MRO of a class.

**Note that superior requires a slight change of the standard MRO 
to a depth-first strategy, instead of the almost-depth-first
strategy used by super**
    """
    mro, mroset = [], set()
    _MRO(thistype, mro, mroset)
    return mro

def _MRO(thistype, mro, mroset):
    mro.append(thistype)
    mroset.add(thistype)
    for nexttype in thistype.__bases__:
        if not nexttype in mroset:
            _MRO(nexttype, mro, mroset)
    

__supers__ = {}
