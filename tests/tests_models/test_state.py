import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_create_state(self):
        # Test creating a state
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name(self):
        # Test state name
        state = State(name="California")
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
