import unittest
from lab_04 import InfixToPostfixEvaluator
 

class TestInfixToPostfixEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = InfixToPostfixEvaluator()

    def test_is_operator(self):
        self.assertTrue(self.evaluator.is_operator('+'))
        self.assertTrue(self.evaluator.is_operator('-'))
        self.assertTrue(self.evaluator.is_operator('*'))
        self.assertTrue(self.evaluator.is_operator('/'))
        self.assertTrue(self.evaluator.is_operator('^'))
        self.assertFalse(self.evaluator.is_operator('a'))
        self.assertFalse(self.evaluator.is_operator('('))
        self.assertFalse(self.evaluator.is_operator(')'))

    def test_priority(self):
        self.assertEqual(self.evaluator.priority('+'), 1)
        self.assertEqual(self.evaluator.priority('-'), 1)
        self.assertEqual(self.evaluator.priority('*'), 2)
        self.assertEqual(self.evaluator.priority('/'), 2)
        self.assertEqual(self.evaluator.priority('^'), 3)
        self.assertEqual(self.evaluator.priority('a'), 0) 

    def test_infix_to_postfix(self):
        expression = "3 + 5 * ( 2 - 8 ) / 4"
        result = self.evaluator.infix_to_postfix(expression.split())
        self.assertEqual(result, ['3', '5', '2', '8', '-', '*', '4', '/', '+'])

    def test_evaluate_postfix(self):
        postfix_expression = ['3', '5', '2', '8', '-', '*', '4', '/', '+']
        result = self.evaluator.evaluate_postfix(postfix_expression)
        self.assertEqual(result, -4.5)

if __name__ == '__main__':
    unittest.main()
