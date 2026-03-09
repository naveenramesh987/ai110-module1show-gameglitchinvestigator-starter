from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hints_use_numeric_not_string_comparison():
    # Bug fix test: guess of 7 vs secret of 42.
    # With the old bug, "7" > "42" alphabetically, so it wrongly returned "Too High".
    # After the fix, 7 < 42 numerically, so it must return "Too Low".
    outcome, _ = check_guess(7, 42)
    assert outcome == "Too Low"
