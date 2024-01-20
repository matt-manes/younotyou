import fnmatch
from typing import Iterable


class Matcher:
    """Determines if a string matches a set of include patterns and also doesn't match a set of exclude patterns.

    Patterns can be wildcard style and case sensitivity is configurable (case sensitive by default).

    Matching can be checked with the `matches` function or by using `in`:

    >>> matcher = Matcher(["*string*"], ["*STrinG*"])
    >>> matcher.matches("string")
    >>> True
    >>> "string" in matcher
    >>> True
    >>> matcher.matches("STrinGent")
    >>> False
    >>> "STrinGent" in matcher
    >>> False
    >>> matcher.matches("stringent")
    >>> True
    >>> "stringent" in matcher
    >>> True
    >>> matcher.case_sensitive = False
    >>> matcher.matches("stringent")
    >>> False
    """

    def __init__(
        self,
        include_patterns: Iterable[str] = ["*"],
        exclude_patterns: Iterable[str] = [],
        case_sensitive: bool = True,
    ):
        """ """
        self.include_patterns = include_patterns
        self.exclude_patterns = exclude_patterns
        self.case_sensitive = case_sensitive
        self._matcher = fnmatch.fnmatchcase if case_sensitive else fnmatch.fnmatch

    def __contains__(self, text: str) -> bool:
        return self.matches(text)

    @property
    def case_sensitive(self) -> bool:
        """Whether this matcher is case sensitive."""
        return self.case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, is_sensitive: bool):
        self._case_sensitive = is_sensitive
        self._matcher = fnmatch.fnmatchcase if self._case_sensitive else fnmatch.fnmatch

    def matches(self, text: str) -> bool:
        """Returns `True` if `text` matches any pattern in `self.include_patterns`
        and also doesn't match any pattern in `self.exclude_patterns`."""
        return any(
            self._matcher(text, pattern) for pattern in self.include_patterns
        ) and all(not self._matcher(text, pattern) for pattern in self.exclude_patterns)


def younotyou(
    candidates: Iterable[str],
    include_patterns: Iterable[str] = ["*"],
    exclude_patterns: Iterable[str] = [],
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
    matcher = Matcher(include_patterns, exclude_patterns, case_sensitive)
    return [candidate for candidate in candidates if candidate in matcher]
