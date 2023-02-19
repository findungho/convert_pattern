#!/usr/bin/env python3
# Description: this script is used to test following functions:
# mapping_pattern and convert_pattern
# Author : Dung Ho

import unittest
from convert_pattern import mapping_pattern, convert_pattern

class TestConvertPattern(unittest.TestCase):
	"""
	Basic test class.
	"""
	
	def test_mapping_pattern_correct_cases(self):
		"""
		This function is used to test the mapping_pattern function
		that includes correct test cases.
		"""
		res1 = mapping_pattern("SST", 5)
		res2 = mapping_pattern("SST", 2)
		res3 = mapping_pattern("SST", 3)
		self.assertEqual(res1, "SSTSS")
		self.assertEqual(res2, "SS")
		self.assertEqual(res3, "SST")
		
	def test_mapping_pattern_incorrect_cases(self):
		"""
		This function is used to test the mapping_pattern function.
		that includes incorrect test cases.
		"""
		res = mapping_pattern("SST", 6)
		self.assertEqual(res, "SSTSSTS")
		
	def test_convert_pattern_correct_cases(self):
		"""
		This function is used to test the convert_pattern function
		that includes correct test cases.
		"""
		res1 = convert_pattern("SSTSS")
		res2 = convert_pattern("SS")
		res3 = convert_pattern("SST")
		self.assertEqual(res1, "Soft, Soft, Tough, Soft and Soft")
		self.assertEqual(res2, "Soft and Soft")
		self.assertEqual(res3, "Soft, Soft and Tough")
		
	def test_convert_pattern_incorrect_cases(self):
		"""
		This function is used to test the convert_pattern function
		that includes incorrect test cases.
		"""
		res = convert_pattern("SSTSST")
		self.assertEqual(res, "Soft, Soft, Tough, Soft, Soft and Soft")
		
		
if __name__ == '__main__':
	unittest.main()