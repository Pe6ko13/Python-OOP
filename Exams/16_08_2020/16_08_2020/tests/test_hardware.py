from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self) -> None:
        self.hard = Hardware('P', 'H', 10, 10)

    def test_init(self):
        self.assertEqual('P', self.hard.name)
        self.assertEqual('H', self.hard.type)
        self.assertEqual(10, self.hard.capacity)
        self.assertEqual(10, self.hard.memory)
        self.assertEqual([], self.hard.software_components)

    def test_install_soft(self):
        soft = Software('P', 'S', 5, 5)
        self.hard.install(soft)
        self.assertEqual([soft], self.hard.software_components)

    def test_install_soft_raise_exception(self):
        soft = Software('P', 'S', 15, 15)
        with self.assertRaises(Exception) as ex:
            self.hard.install(soft)
        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual([], self.hard.software_components)

    def test_uninstall_soft(self):
        soft = Software('P', 'S', 5, 5)
        self.hard.install(soft)
        self.assertEqual([soft], self.hard.software_components)
        self.hard.uninstall(soft)
        self.assertEqual([], self.hard.software_components)


if __name__ == '__main__':
    main()