#!/usr/bin/env python3
# Description: this script is used to convert each character in the pattern 
# into human readable text and output the corresponding text.
# The length of the output is defined by the integer argument.
# Author : Dung Ho


import argparse

def mapping_pattern(input_str: str, n: int) -> str:
	"""
	Compare the length of pattern and given integer,
	if the length of pattern > n return a substring of the pattern from n index,
	if the length of pattern == n return a same string of pattern,
	if the length of pattern < n return extended string of the pattern
	"""
	if len(input_str) > n:
		return input_str[:n]
	
	if len(input_str) == n:
		return input_str
	
	if len(input_str) <= n:
		q, mod = divmod(n, len(input_str))
		return input_str*q + input_str[:mod]
	
def convert_pattern(input_pattern: str):
	"""
	Checking each character in the input pattern,
	print corresponding output that based on characters.
	"""
	new_pattern = list()
	for c in input_pattern:
		if c.lower() == 'S'.lower():
			new_pattern.append('Soft')
		if c.lower() == 'T'.lower():
			new_pattern.append('Tough')
			
	fist_range_of_pattern = ", ".join(new_pattern[:-2])
	last_range_of_pattern = " and ".join(new_pattern[-2:])
	
	if fist_range_of_pattern != "":
		return f"{fist_range_of_pattern}, {last_range_of_pattern}"
	else:
		return f"{last_range_of_pattern}"

def main():
	"""
	Executes the mapping_pattern and convert_pattern functions with given input via CommandLine Interface.
	"""
	parser = argparse.ArgumentParser(
		description='This script is used for converting each character in the pattern' +
		' into human readable test and output the corresponding text. ' +
		' The length of the output is defined by the integer argument'
	)
	parser.add_argument(
		'--pattern',
		help='The random pattern that consisting character of S and T.' +
		' E.g: "STTTS"',
		required=True
	)
	
	parser.add_argument(
		'--nums',
		help='The number of integers that separate by a space.' +
		' E.g: "1 5 8"',
		required=True
	)
	
	args = parser.parse_args()
	pattern = args.pattern
	nums = args.nums
	
	for i in nums.split():
		mapped_pattern = mapping_pattern(pattern, int(i))
		converted_pattern = convert_pattern(mapped_pattern)
		print(converted_pattern)
		
		
if __name__ == "__main__":
	main()