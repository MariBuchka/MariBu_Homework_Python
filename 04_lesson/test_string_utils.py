import pytest
from string_utils import StringUtils

#Позитивные тесты

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("HELLO world", "Hello world"),
        ("HELL0 world", "Hell0 world"),
    ],
)

def test_capitilize_positive(input_text, expected_output):
    strings = StringUtils()
    assert strings.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" hello", "hello"),
        ("   Hello", "Hello"),
        ("     57Hello", "57Hello"),
        ("  -Hello!", "-Hello!"),
    ],
)

def test_trim_positive(input_text, expected_output):
    strings = StringUtils()
    assert strings.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, delimiter, expected_output",
    [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("8/p/m/79", "/", ["8", "p", "m", "79"]),
        ("8,9/p/m/7,9", "/", ["8,9", "p", "m", "7,9"]),
        ("8,9/p/m/7,9", ",", ["8", "9/p/m/7", "9"]),
    ],
)

def test_to_list_with_delimiter_positive(input_text, delimiter, expected_output):
    strings = StringUtils()
    assert strings.to_list(input_text, delimiter) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("a,b,c,d", ["a", "b", "c", "d"]),
        ("Привет, Alex! Как дела, пирожочек?", ["Привет", " Alex! Как дела", " пирожочек?"]),
        ("19,05+19.05=38,1", ["19", "05+19.05=38", "1"]),
    ],
)

def test_to_list_without_delimiter_positive(input_text, expected_output):
    strings = StringUtils()
    assert strings.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("a,b,c,d", "c", True),
        ("StopSecret", "S", True),
    ],
)

def test_contains_positive(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Abrakadabra", "b", "Arakadara"),
        ("Hello, love", "lo", "Hel, ve"),
    ],
)

def test_delete_symbol_positive(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Abrakadabra", "b", False),
        ("Hello, love", "H", True),
        ("#Hello, #love", "#", True),
    ],
)

def test_starts_with_positive(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Abrakadabra", "A", False),
        ("Hello, love!", "!", True),
        ("#Hello, #love", "#", False),
        ("", "", True),
        ("   ", "!", False),
    ],
)

def test_end_with_positive(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Abrakadabra", False),
        ("   Hello, love!", False),
        ("#Hello, #love", False),
        ("", True),
        ("   ", True),
    ],
)

def test_is_empty_positive(input_text, expected_output):
    strings = StringUtils()
    assert strings.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [
        (["Abra, kadabra", "#kadabra"], "-", "Abra, kadabra-#kadabra"),
        (["#Мир", "Дружба", "Жвачка"], "#", "#Мир#Дружба#Жвачка"),
        (["Агент", 0, 0, 7], "", "Агент007"),
        (["Hello", " world"], ",", "Hello, world"),
        (["Abra", "kada", "bra"], "_", "Abra_kada_bra"),
        (["Агент", "", 7], "0", "Агент007"),
    ],
)

def test_to_string_with_joiner_positive(input_text, joiner, expected_output):
    strings = StringUtils()
    assert strings.list_to_string(input_text, joiner) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (["Abra, kadabra", "#kadabra"], "Abra, kadabra, #kadabra"),
        (["#Мир", "Дружба", "Жвачка"], "#Мир, Дружба, Жвачка"),
        (["Агент", 0, 0, 7], "Агент, 0, 0, 7"),
    ],
)

def test_to_string_without_joiner_positive(input_text, expected_output):
    strings = StringUtils()
    assert strings.list_to_string(input_text) == expected_output

#Негативные тесты

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("  world", "  world"),
        ("d", "D"),
        ("42woRld02", "42world02"),
        ("#woRld02", "#world02"),
        ("", ""),
        ("   ", "   "),
    ],
)

def test_capitilize_edge_cases_negative(input_text, expected_output):
    strings = StringUtils()
    assert strings.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text",
    [
        None,
        666,
        ["string1", "string2"],
    ],
)

def test_capitilize_invalid_input_negative(input_text):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.capitilize(input_text)

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        ("   ", ""),
        ("myWorld", "myWorld"),
        ("myWorld   ", "myWorld   "),
        ("my World", "my World"),
        ("\tmyWorld", "\tmyWorld"),
        ("\nmyWorld", "\nmyWorld"),
    ],
)

def test_trim_edge_cases_negative(input_text, expected_output):
    strings = StringUtils()
    assert strings.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text",
    [
        None,
        666,
        ["   string1", "string2"],
    ],
)

def test_trim_invalid_input_negative(input_text):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.capitilize(input_text)

@pytest.mark.parametrize(
    "input_text, delimiter, expected_output",
    [
        ("a,b,c,d", ":", ["a,b,c,d"]),
        ("1:2::3", ":", ["1", "2", "", "3"]),
        ("", "", []),
        ("  ", ",", []),
    ],
)

def test_to_list_edge_cases_negative(input_text, delimiter, expected_output):
    strings = StringUtils()
    assert strings.to_list(input_text, delimiter) == expected_output

@pytest.mark.parametrize(
    "input_text, delimiter",
    [
        (None, ","),
        (123, ","),
    ],
)

def test_to_list_invalid_input_negative(input_text, delimiter):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.to_list(input_text, delimiter)

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "", True),
        ("", "/", False),
        ("   ", "!", False),
        ("words", "", True),
    ],
)

def test_contains_edge_cases_negative(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol",
    [
        (None, "R"),
        (123, "9"),
    ],
)

def test_contains_invalid_input_negative(input_text, symbol):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.contains(input_text, symbol)

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "M", ""),
        ("", "", ""),
        ("   ", "!", "   "),
    ],
)

def test_delete_symbol_edge_cases_negative(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol",
    [
        (None, "R"),
        (123, "9"),
    ],
)

def test_delete_symbol_invalid_input_negative(input_text, symbol):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.delete_symbol(input_text, symbol)

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Marta", "", True),
        ("", "M", False),
        ("   ", "!", False),
    ],
)

def test_starts_with_edge_cases_negative(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol",
    [
        (None, "R"),
        (123, "9"),
    ],
)

def test_starts_invalid_input_negative(input_text, symbol):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.starts_with(input_text, symbol)

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Marta", "", True),
        ("", "", True),
        ("   ", "!", False),
    ],
)

def test_end_with_edge_cases_negative(input_text, symbol, expected_output):
    strings = StringUtils()
    assert strings.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol",
    [
        (None, "R"),
        (123, "9"),
    ],
)

def test_end_with_invalid_input_negative(input_text, symbol):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.end_with(input_text, symbol)

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", True),
        ("   ", True),
    ],
)

def test_is_empty_edge_cases_negative(input_text, expected_output):
    strings = StringUtils()
    assert strings.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text",
    [
        None,
        123,
    ],
)

def test_is_empty_invalid_input_negative(input_text):
    strings = StringUtils()
    with pytest.raises(AttributeError):
        strings.is_empty(input_text)

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [
        ([], "", ""),
        ([""], "#", ""),
        ([0, None, 7], ", ", "0, None, 7"),
        (["  ", ""], ",", "  ,"),
    ],
)

def test_to_string_edge_cases_negative(input_text, joiner, expected_output):
    strings = StringUtils()
    assert strings.list_to_string(input_text, joiner) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [
        (None, ",", TypeError),
        ([123], "-", None),
    ],
)

def test_to_string_invalid_input_negative(input_text, joiner, expected_output):
    strings = StringUtils()
    if expected_output:
        with pytest.raises(expected_output):
            strings.list_to_string(input_text, joiner)
    else:
        result = strings.list_to_string(input_text, joiner)
        assert result == "123", f"Ожидалось '123', но получено {result}"