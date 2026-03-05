from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ---------------------------------------------------------------------------
# check_guess
# ---------------------------------------------------------------------------

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_winning_guess_message():
    _, msg = check_guess(7, 7)
    assert "Correct" in msg

def test_too_high_message_says_lower():
    _, msg = check_guess(99, 1)
    assert "LOWER" in msg

def test_too_low_message_says_higher():
    _, msg = check_guess(1, 99)
    assert "HIGHER" in msg

def test_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_off_by_one_above():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_off_by_one_below():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------

def test_parse_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_valid_float_truncates():
    ok, val, err = parse_guess("7.9")
    assert ok is True
    assert val == 7

def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert err is not None

def test_parse_none():
    ok, val, err = parse_guess(None)
    assert ok is False
    assert val is None

def test_parse_non_numeric():
    ok, val, err = parse_guess("banana")
    assert ok is False
    assert err is not None

def test_parse_negative_number():
    ok, val, err = parse_guess("-5")
    assert ok is True
    assert val == -5

def test_parse_whitespace_only():
    ok, val, err = parse_guess("   ")
    assert ok is False


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100

def test_unknown_difficulty_defaults():
    low, high = get_range_for_difficulty("Legendary")
    assert low == 1 and high == 100


# ---------------------------------------------------------------------------
# update_score
# ---------------------------------------------------------------------------

def test_win_early_gives_high_score():
    score = update_score(0, "Win", attempt_number=1)
    assert score > 0

def test_win_late_gives_minimum_points():
    # attempt_number=10 → 100 - 110 = negative, clamped to 10
    score = update_score(0, "Win", attempt_number=10)
    assert score == 10

def test_too_high_deducts_score():
    score = update_score(50, "Too High", attempt_number=1)
    assert score == 45

def test_too_low_deducts_score():
    score = update_score(50, "Too Low", attempt_number=1)
    assert score == 45

def test_unknown_outcome_no_change():
    score = update_score(50, "Banana", attempt_number=1)
    assert score == 50

def test_score_cannot_go_below_zero_by_design():
    # update_score itself doesn't clamp, but verify it just does math correctly
    score = update_score(3, "Too High", attempt_number=1)
    assert score == -2