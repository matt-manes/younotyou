# younotyou

Filter a list of strings and/or paths based on include and exclude patterns.

## Installation

Install with:

<pre>
pip install younotyou
</pre>

Convenient one stop shop to include and exclude strings using glob style pattern matching.<br>


## Usage

Patterns can be literals or glob style wildcard strings.<br>
Exclusion patterns override include patterns,
i.e. if an item matches an include pattern but also matches an exclude pattern, it will be excluded.

<pre>
>>> from younotyou import younotyou
>>> strings = ["thispattern", "aPaTtErN", "mypatterns"]
>>> younotyou(strings, ["*pattern"])
['thispattern']
>>> younotyou(strings, ["*pattern*"])
['thispattern', 'mypatterns']
>>> younotyou(strings, ["*pattern*"], case_sensitive=False)
['thispattern', 'aPaTtErN', 'mypatterns']
>>> younotyou(strings, ["*pattern*"], ["my*", "*is*"], case_sensitive=False)
['aPaTtErN']
>>> younotyou(strings, exclude_patterns=["*PaT*"])
['thispattern', 'mypatterns']
>>> younotyou(strings, exclude_patterns=["*PaT*"], case_sensitive=False)
[]
>>> younotyou(strings, include_patterns=["*PaT*"], exclude_patterns=["*PaT*"], case_sensitive=False)
[]
</pre>
