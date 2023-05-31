import fnmatch
from pathlib import Path
from pathier import Pathier
from typing import Iterable


def younotyou(
    candidates: Iterable[str],
    include_patterns: list[str] = ["*"],
    exclude_patterns: list[str] = [],
    case_sensitive: bool = True,
) -> list[str]:
    """Returns a list of strings that match any pattern in `include_patterns`, but don't match any pattern in `exclude_patterns`.

    Patterns can be literals or glob style wildcard strings.

    Exclusion patterns override include patterns,
    i.e. if an item matches an include pattern but also matches an exclude pattern, it will be excluded.
    >>> strings = ["thispattern", "aPaTtErN", "mypatterns"]
    >>> younotyou(strings, ["*pattern"])
    >>> ['thispattern']
    >>> younotyou(strings, ["*pattern*"])
    >>> ['thispattern', 'mypatterns']
    >>> younotyou(strings, ["*pattern*"], case_sensitive=False)
    >>> ['thispattern', 'aPaTtErN', 'mypatterns']
    >>> younotyou(strings, ["*pattern*"], ["my*", "*is*"], case_sensitive=False)
    >>> ['aPaTtErN']
    >>> younotyou(strings, exclude_patterns=["*PaT*"])
    >>> ['thispattern', 'mypatterns']
    >>> younotyou(strings, exclude_patterns=["*PaT*"], case_sensitive=False)
    >>> []
    >>> younotyou(strings, include_patterns=["*PaT*"], exclude_patterns=["*PaT*"], case_sensitive=False)
    >>> []
    """
    matcher = fnmatch.fnmatchcase if case_sensitive else fnmatch.fnmatch
    return [
        candidate
        for candidate in candidates
        if any(matcher(candidate, pattern) for pattern in include_patterns)  # type: ignore
        and all(not matcher(candidate, pattern) for pattern in exclude_patterns)  # type: ignore
    ]
