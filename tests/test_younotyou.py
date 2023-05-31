import pytest

from younotyou import younotyou


def test():
    candidates = [
        "asefasdfpatternasdfie",
        "aslkfjeasdfpatternasdlfuhoh",
        "asdfUHOHasdflePattERn",
    ]
    assert younotyou(candidates, ["*pattern*"], ["*uhoh"]) == candidates[:1]
    assert younotyou(candidates, ["*pattern*"], ["*uhoh"], False) == candidates[::2]
    assert (
        younotyou(candidates, ["*pattern*"], ["*uhoh", "asd*"], False) == candidates[:1]
    )
    assert younotyou(candidates, ["*pattern*"]) == candidates[0:2]
    assert younotyou(candidates, ["*pattern*"], case_sensitive=False) == candidates
    assert (
        younotyou(candidates, exclude_patterns=["*pattern*"], case_sensitive=False)
        == []
    )
    assert younotyou(candidates, exclude_patterns=["*pattern"]) == candidates
    assert (
        younotyou(candidates, exclude_patterns=["*pattern"], case_sensitive=False)
        == candidates[:2]
    )
    assert (
        younotyou(candidates, exclude_patterns=["*pattern*"], case_sensitive=False)
        == []
    )
    assert younotyou(candidates, ["*pattern*"], ["*pattern*"], False) == []
