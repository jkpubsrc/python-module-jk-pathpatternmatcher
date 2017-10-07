#!/usr/bin/env python3
# -*- coding: utf-8 -*-





import os
import sys

import jk_pathpatternmatcher


TEST_DATA = [
	('someDir/someFile.txt', 'someDir/someFile.txt', True),
	('someDir/otherDir/someFile.txt', 'someDir/otherDir/someFile.txt', True),
	('someDir/*/someFile.txt', 'someDir/otherDir/someFile.txt', True),
	('**/someFile.txt', 'someDir/otherDir/someFile.txt', True),
	('someDir/someFile.txt', 'someDir/otherDir/someFile.txt', False),
	('**/*.txt', 'someDir/otherDir/someFile.txt', True),
	('someDir/**/myFile.*.txt', 'someDir/someOtherDir/evenAnotherDir/myFile.extra.txt', True),
]



for (pattern, path, bExpectedResult) in TEST_DATA:
	matcher = jk_pathpatternmatcher.createPatternMatcher(pattern)
	bVerificationResult = matcher.checkMatch(path) == bExpectedResult
	if bVerificationResult:
		print("SUCCESS :: \"" + path + "\" against \"" + pattern + "\" expecting " + str(bExpectedResult))
	else:
		print("FAILED  :: \"" + path + "\" against \"" + pattern + "\" expecting " + str(bExpectedResult))











