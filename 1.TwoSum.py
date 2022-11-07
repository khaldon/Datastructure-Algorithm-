import unittest


def two_sum(nums, target):
    complement = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if nums[i] in complement:
            return [complement[nums[i]], i]
        else:
            complement[comp] = i


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])


if __name__ == "__main__":
    unittest.main()
