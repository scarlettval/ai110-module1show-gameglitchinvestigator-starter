from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def click_button(at, label_start):
    button = next(b for b in at.button if b.label.startswith(label_start))
    return button.click().run()


def test_new_game_clears_history_and_restarts_after_loss():
    # Bug: New Game didn't reset status or history, so after a loss the app
    # kept showing "Game over" and old guesses carried into the new game.
    at = AppTest.from_file(APP_PATH).run()
    at.session_state.status = "lost"
    at.session_state.history = [10, 20, 30]
    at.session_state.attempts = 8
    at.run()
    assert at.error[0].value.startswith("Game over")

    click_button(at, "New Game")

    assert at.session_state.status == "playing"
    assert at.session_state.history == []
    assert at.session_state.attempts == 0
    assert not at.error

    # The new game should actually accept guesses.
    secret = at.session_state.secret
    guess = 1 if secret != 1 else 2
    at.text_input[0].input(str(guess))
    click_button(at, "Submit")
    assert at.session_state.history == [guess]
    assert at.session_state.attempts == 1


def test_new_game_secret_uses_difficulty_range():
    # Bug: New Game always picked the secret from 1-100, ignoring difficulty.
    at = AppTest.from_file(APP_PATH).run()
    at.selectbox[0].select("Easy").run()

    for _ in range(10):
        click_button(at, "New Game")
        assert 1 <= at.session_state.secret <= 20
