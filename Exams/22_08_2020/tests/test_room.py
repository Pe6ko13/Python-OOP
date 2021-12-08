from unittest import TestCase, main
from project.rooms.room import Room
from project.people.child import Child


class TestRoom(TestCase):
    def setUp(self) -> None:
        self.room = Room('Petrov', 100, 2)

    def test_init(self):
        self.assertEqual('Petrov', self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -2
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses(self):
        self.assertEqual(0, self.room.expenses)
        c1 = Child(5, 4, 1)
        expected = 300
        self.room.calculate_expenses([c1])
        self.assertEqual(expected, self.room.expenses)


if __name__ == '__main__':
    main()
