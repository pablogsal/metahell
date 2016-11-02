# metahell
Wellcome to the metahell

After installing metahell (`python setup.py` or `pip install .`) you can unleash the metahell using one metadevil from `metahell.metadevils` or your own:

```python

import metahell

with metahell.metainyect( lambda *args: 42 ):

    class Test():
        pass

    print(type(Test))
    print(Test)
    print( Test == 42 )

class Test2:
    pass

print(type(Test2))
print(Test2)
print( Test2 == 42 )
```

You can do the same without the contextmanager with:


```python

import metahell

metahell.unleash( lambda *args: 42 )

class Test():
    pass

print(type(Test))
print(Test)
print( Test == 42 )

```

To undo the `metahell.unleash` you need to call `metahell.you_cannot_pass()`.
