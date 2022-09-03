jk_pathpatternmatcher
=====================

Introduction
------------

A python module to perform simple pattern matching on (relative) paths.

Information about this module can be found here:

* [github.com](https://github.com/jkpubsrc/python-module-jk-pathpatternmatcher)
* [pypi.org](https://pypi.org/project/jk_pathpatternmatcher/)

How to use this module
----------------------

### Import

To import this module use the following statement:

```python
import jk_pathpatternmatcher
```

### Matching Patterns

The function ```createPatternMatcher``` will compile a string or a list of strings and provide a pattern matcher object.
This object contains the method ```checkMatch(...)``` for checking against strings. Example:

```python
matcher = jk_pathpatternmatcher.createPatternMatcher('someDir/**/myFile.*.txt')
bResult = matcher.checkMatch("someDir/someOtherDir/evenAnotherDir/myFile.extra.txt')
```

### Iterating over Files and Directories

For processing files and directories the following function exists for your convenience:

```python
#
# Recursively get all files and directories. If a filter is specified the filter is taken into account.
#
# @param		str bRecursive				The base path that defines the starting point for the search.
# @param		bool bRecursive				If <c>True</c> (= the default) a recursive search will be performed.
# @param		misc relDirPathFilter		A filter specifying which directories to ignore.
# @param		misc relFilePathFilter		A filter specifying which files to ignore.
# @return		tuple						Returns a tuple containing:
#											* a list of directory paths relative to the search base directory
#											* a list of file paths relative to the search base directory
#
def getFilesAndDirs(searchBaseDirPath, relDirPathFilter, relFilePathFilter, bRecursive = True)
```

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0

