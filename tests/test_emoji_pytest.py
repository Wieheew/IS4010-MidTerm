import pytest
import requests
from unittest.mock import patch, Mock
from src.main import get_random_by_category, search_emoji

@pytest.fixture
def sample_emoji():
    """Fixture for a single emoji."""
    return {
        "name": "test emoji",
        "category": "test category",
        "group": "test group",
        "htmlCode": ["&#123;"],
        "unicode": ["U+123"]
    }

@pytest.fixture
def sample_emoji_list(sample_emoji):
    """Fixture for a list of emojis."""
    return [
        sample_emoji,
        {
            "name": "another emoji",
            "category": "test category",
            "group": "test group",
            "htmlCode": ["&#124;"],
            "unicode": ["U+124"]
        }
    ]

@pytest.mark.parametrize("category,expected_url", [
    ("smileys", "https://emojihub.yurace.pro/api/random/category/smileys"),
    ("food", "https://emojihub.yurace.pro/api/random/category/food"),
    ("flags", "https://emojihub.yurace.pro/api/random/category/flags")
])
def test_get_random_by_category_parametrized(category, expected_url, sample_emoji):
    """Parametrized test for getting random emoji by category."""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = sample_emoji
        mock_get.return_value = mock_response

        result = get_random_by_category(category)
        assert result == sample_emoji
        mock_get.assert_called_once_with(expected_url)

def test_search_emoji_pytest(sample_emoji_list):
    """Pytest-style test for emoji search."""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = sample_emoji_list
        mock_get.return_value = mock_response
        mock_response.raise_for_status = Mock()

        # Test with a matching search term
        result = search_emoji("test")
        assert len(result) == 1
        assert result[0]["name"] == "test emoji"

        # Test with a non-matching search term
        result = search_emoji("nonexistent")
        assert len(result) == 0

        # Test with empty string
        with pytest.raises(ValueError):
            search_emoji("")

        # Test with None
        with pytest.raises(TypeError):
            search_emoji(None)

        # Test with invalid type
        with pytest.raises(TypeError):
            search_emoji(123)

        # Test API error
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        with pytest.raises(requests.exceptions.RequestException):
            search_emoji("test")

@pytest.mark.parametrize("search_term,expected_count", [
    ("test", 1),
    ("another", 1),
    ("emoji", 2),
    ("nonexistent", 0)
])
def test_search_emoji_variations(search_term, expected_count, sample_emoji_list):
    """Parametrized test for different search scenarios."""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = sample_emoji_list
        mock_get.return_value = mock_response

        result = search_emoji(search_term)
        assert len(result) == expected_count