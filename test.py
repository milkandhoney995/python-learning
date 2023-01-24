import unittest

# テストコード(Dollarが正しく動くかを確認する)
class MoneyTest(unittest.TestCase):
  def testMultiplication(self):
    five = Dollar(5)
    product = five.times(2)
    self.assertEqual(10, product.amount)

# 実装コード
class Dollar():

  def __init__(self, amount):
    self.amount = amount
  def times(self, multiplier):
    return Dollar(self.amount * multiplier)
# テストの実行方法
if __name__ == '__main__':
  unittest.main()