from unittest import TestCase

from stack import Stack, EmptyStackError, NotEnoughtElements


class TestStackOperations(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack.clear()

    def test_should_add_new_element_to_stack(self):
        value, expected = 42, 42

        self.stack.push(value)

        self.assertEqual(self.stack.peek(), expected)

    def test_should_remove_last_element_from_stack(self):
        element, expected = 42, 42
        self.stack.push(element)

        value = self.stack.pop()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 0)

    def test_peek_should_show_last_element_and_not_remove_it(self):
        element, expected = 42, 42
        self.stack.push(element)

        value = self.stack.peek()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 1)

    def test_should_clear_stack(self):
        self.stack.push(42)
        self.stack.push(43)

        self.stack.clear()

        self.assertEqual(self.stack.size, 0)

    def test_should_raise_when_called_pop_on_empty_stack(self):
        self.assertRaises(EmptyStackError, self.stack.pop)

    def test_multi_pop_raises_if_num_of_element_is_less_then_in_stack(self):
        self.assertRaises(NotEnoughtElements, self.stack.multi_pop, 2)

    def test_multi_pop_should_return_two_elements(self):
        expected = [9, 8, 7, 6]
        for elem in range(10):
            self.stack.push(elem)

        result = self.stack.multi_pop(4)

        self.assertEqual(result, expected)