from younotyou import Matcher, younotyou

candidates = [
    "asefasdfpatternasdfie",
    "aslkfjeasdfpatternasdlfuhoh",
    "asdfUHOHasdflePattERn",
]


def test__matcher():
    matcher = Matcher(["*string*", "my*"], ["*STrinG*"])
    assert matcher.matches("string")
    assert not matcher.matches("STrinGent")
    assert matcher.matches("stringent")
    assert matcher.matches("my text")
    assert not matcher.matches("this is my text")
    assert not matcher.matches("nope")
    matcher.case_sensitive = False
    assert not matcher.matches("stringent")
    ##########################################
    matcher.case_sensitive = True
    assert "string" in matcher
    assert not "STrinGent" in matcher


def test__younotyou():
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
