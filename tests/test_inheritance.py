import unittest
import metahell
import builtins


class TestInheritance(unittest.TestCase):

    def test_context_manager(self):
        self.assertNotEqual(
            builtins.__build_class__.__module__, 'metahell.metahell')
        with metahell.metainyect(metahell.metadevils.LoggingClass):
            import class_garden

            self.assertEqual(
                builtins.__build_class__.__module__, 'metahell.metahell')

        self.assertTrue(hasattr(class_garden.B(), 'logger'))
        self.assertTrue(hasattr(class_garden.B1(), 'logger'))
        self.assertTrue(hasattr(class_garden.Base(1), 'logger'))
        self.assertTrue(hasattr(class_garden.Derived(1, 2, 3), 'logger'))
        self.assertTrue(hasattr(class_garden.Subclass(1, 2, 3), 'logger'))
        self.assertTrue(hasattr(class_garden.Subsubclass(1, 2, 3), 'logger'))
        self.assertNotEqual(
            builtins.__build_class__.__module__, 'metahell.metahell')

    def test_unleash(self):
        metahell.unleash(metahell.metadevils.LoggingClass)
        self.assertEqual(builtins.__build_class__.__module__,
                         'metahell.metahell')
