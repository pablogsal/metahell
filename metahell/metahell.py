import builtins
import contextlib

__builtins_build_class = builtins.__build_class__
__metadevils__ = []


def _create_custom_build(metadevil):
    def _custom_build(func, name, *bases, **kwargs):
        if not any(isinstance(base, type) for base in bases):
            if 'metaclass' in kwargs:
                pass
            else:
                kwargs['metaclass'] = metadevil

        return __builtins_build_class(func, name, *bases, **kwargs)
    return _custom_build


@contextlib.contextmanager
def metainyect(metadevil):
    builtins.__build_class__ = _create_custom_build(metadevil)
    yield
    builtins.__build_class__ = __builtins_build_class


def unleash(metadevil):
    builtins.__build_class__ = _create_custom_build(metadevil)
