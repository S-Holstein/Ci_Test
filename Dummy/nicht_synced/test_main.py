from io import StringIO
from contextlib import redirect_stdout
from main import message_to_the_world  # Passe den Importpfad an


def test_message_to_the_world():
    # Testfall 1: Überprüfen, ob die Funktion True zurückgibt, wenn der Input ein String ist
    assert message_to_the_world("Hello, world!") is True

    # Testfall 2: Überprüfen, ob die Funktion False zurückgibt, wenn der Input kein String ist
    assert message_to_the_world(12345) is False

    # Testfall 3: Überprüfen, ob die Funktion den Text korrekt ausgibt
    text = "Hello, world!"
    with StringIO() as buf, redirect_stdout(buf):
        message_to_the_world(text)
        output = buf.getvalue().strip()
    assert output == text
