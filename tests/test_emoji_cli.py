import unittest
import pytest
from unittest.mock import patch, Mock
import json
from src.main import get_random_emoji, get_random_by_category, get_all_emojis, get_all_by_category, search_emoji

# Pytest fixtures
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

# Test class that works with both unittest and pytest
class TestEmojiHubCLI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.sample_emoji = {
            "name": "test emoji",
            "category": "test category",
            "group": "test group",
            "htmlCode": ["&#123;"],
            "unicode": ["U+123"]
        }
        
        self.sample_emoji_list = [
            self.sample_emoji,
            {
                "name": "another emoji",
                "category": "test category",
                "group": "test group",
                "htmlCode": ["&#124;"],
                "unicode": ["U+124"]
            }
        ]

    @patch('requests.get')
    def test_get_random_emoji(self, mock_get):
        """Test getting a random emoji."""
        mock_response = Mock()
        mock_response.json.return_value = self.sample_emoji
        mock_get.return_value = mock_response

        result = get_random_emoji()
        self.assertEqual(result, self.sample_emoji)
        mock_get.assert_called_once_with("https://emojihub.yurace.pro/api/random")

    @patch('requests.get')
    def test_get_all_emojis(self, mock_get):
        """Test getting all emojis."""
        mock_response = Mock()
        mock_response.json.return_value = self.sample_emoji_list
        mock_get.return_value = mock_response

        result = get_all_emojis()
        self.assertEqual(result, self.sample_emoji_list)
        mock_get.assert_called_once_with("https://emojihub.yurace.pro/api/all")

# Pytest-style tests
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

        # Test with a matching search term
        result = search_emoji("test")
        assert len(result) == 1
        assert result[0]["name"] == "test emoji"

        # Test with a non-matching search term
        result = search_emoji("nonexistent")
        assert len(result) == 0

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

if __name__ == '__main__':
    unittest.main()