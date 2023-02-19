### Author: Dung Ho
### Email: fin.dunngho@gmail.com
### Phone number: +358 449865555


## Overview
_This is a simple script is used to convert each character in the pattern into human readable text and output the corresponding text. The length of the output is defined by the integer argument._


## Requirements
- Python 3.7 or above.


## How to use
1. Run the main script by following command: 
	`python convert_pattern.py --pattern "SST" --nums "5 2 3 4"`

2. Run test by following command:
    `python convert_pattern_test.py`

3. Example outputs:
    + Main script:
    	```
        Soft, Soft, Tough, Soft and Soft
        Soft and Soft
        Soft, Soft and Tough
        Soft, Soft, Tough and Soft
        ```
    + Test script: 
		```
        .F.F
        ======================================================================
        FAIL: test_incorrect_convert_pattern_incorrect_cases (__main__.TestConvertPattern)
        This function is used to test the convert_pattern function
        ======================================================================
        FAIL: test_mapping_pattern_incorrect_cases (__main__.TestConvertPattern)
        This function is used to test the mapping_pattern function.
		```
