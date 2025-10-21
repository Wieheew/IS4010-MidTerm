import requests
import argparse

BASE_URL = "https://emojihub.yurace.pro/api"

def get_random_emoji():
    """
    Fetch a random emoji from the Emojihub API.

    Returns
    -------
    dict
        A dictionary containing emoji information with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Raises
    ------
    requests.exceptions.RequestException
        If there's an error communicating with the API
    ValueError
        If the API response is not in the expected format

    Examples
    --------
    >>> emoji = get_random_emoji()
    >>> print(emoji['name'])
    'grinning face'
    """
    response = requests.get(f"{BASE_URL}/random")
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
    
    # Validate response format
    required_keys = ['name', 'category', 'group', 'htmlCode', 'unicode']
    if not all(key in data for key in required_keys):
        raise ValueError("Invalid API response format")
    
    return data

def get_random_by_category(category):
    """
    Fetch a random emoji from a specific category.

    Parameters
    ----------
    category : str
        The category to fetch from (e.g., "smileys and people", "animals and nature")

    Returns
    -------
    dict
        A dictionary containing emoji information with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Examples
    --------
    >>> emoji = get_random_by_category("smileys and people")
    >>> print(emoji['category'])
    'smileys and people'
    """
    return requests.get(f"{BASE_URL}/random/category/{category}").json()

def get_all_emojis():
    """
    Fetch all available emojis from the API.

    Returns
    -------
    list
        A list of dictionaries, each containing emoji information with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Examples
    --------
    >>> emojis = get_all_emojis()
    >>> print(len(emojis))
    1000
    """
    return requests.get(f"{BASE_URL}/all").json()

def get_all_by_category(category):
    """
    Fetch all emojis from a specific category.

    Parameters
    ----------
    category : str
        The category to fetch from (e.g., "smileys and people", "animals and nature")

    Returns
    -------
    list
        A list of dictionaries, each containing emoji information with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Examples
    --------
    >>> emojis = get_all_by_category("food and drink")
    >>> print(emojis[0]['category'])
    'food and drink'
    """
    return requests.get(f"{BASE_URL}/all/category/{category}").json()

def search_emoji(query):
    """
    Search for emojis by name.

    Parameters
    ----------
    query : str
        The search term to look for in emoji names (case-insensitive)

    Returns
    -------
    list
        A list of dictionaries containing matching emojis, each with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Raises
    ------
    requests.exceptions.RequestException
        If there's an error communicating with the API
    ValueError
        If the search query is empty or the API response is invalid
    TypeError
        If the search query is not a string

    Examples
    --------
    >>> results = search_emoji("cat")
    >>> print(len(results))
    5
    >>> print(results[0]['name'])
    'cat face'
    """
    if not isinstance(query, str):
        raise TypeError("Search query must be a string")
    if not query.strip():
        raise ValueError("Search query cannot be empty")

    response = requests.get(f"{BASE_URL}/all")
    response.raise_for_status()
    all_emojis = response.json()

    if not isinstance(all_emojis, list):
        raise ValueError("Invalid API response format")

    query = query.lower()
    return [emoji for emoji in all_emojis if 'name' in emoji and query in emoji['name'].lower()]

def print_emoji(emoji):
    """
    Print the details of a single emoji in a formatted way.

    Parameters
    ----------
    emoji : dict
        A dictionary containing emoji information with the following keys:
        - name (str): The name of the emoji
        - category (str): The category of the emoji
        - group (str): The group the emoji belongs to
        - htmlCode (list): HTML codes for the emoji
        - unicode (list): Unicode representations of the emoji

    Raises
    ------
    TypeError
        If emoji parameter is not a dictionary
    KeyError
        If required emoji information is missing
    IndexError
        If htmlCode or unicode lists are empty

    Examples
    --------
    >>> emoji = get_random_emoji()
    >>> print_emoji(emoji)
    Name: grinning face
    Category: smileys and people
    Group: face positive
    HTML Code: &#128512;
    Unicode: U+1F600
    """
    if not isinstance(emoji, dict):
        raise TypeError("Emoji must be a dictionary")

    required_keys = ['name', 'category', 'group', 'htmlCode', 'unicode']
    missing_keys = [key for key in required_keys if key not in emoji]
    if missing_keys:
        raise KeyError(f"Missing required emoji keys: {', '.join(missing_keys)}")

    if not emoji['htmlCode'] or not emoji['unicode']:
        raise IndexError("HTML code or Unicode data is missing")

    try:
        print(f"Name: {emoji['name']}")
        print(f"Category: {emoji['category']}")
        print(f"Group: {emoji['group']}")
        print(f"HTML Code: {emoji['htmlCode'][0]}")
        print(f"Unicode: {emoji['unicode'][0]}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Invalid emoji data format: {str(e)}")

VALID_CATEGORIES = [
    "smileys and people",
    "animals and nature",
    "food and drink",
    "activity",
    "travel and places",
    "objects",
    "symbols",
    "flags"
]

def validate_category(category):
    """
    Validate that a category name is valid.

    Parameters
    ----------
    category : str
        The category name to validate

    Raises
    ------
    ValueError
        If the category is not in the list of valid categories
    """
    if category not in VALID_CATEGORIES:
        valid_cats = '\n- '.join([''] + VALID_CATEGORIES)
        raise ValueError(f"Invalid category: {category}. Valid categories are:{valid_cats}")

def main():
    """
    Main function to run the CLI application.

    This function parses command-line arguments and executes the appropriate emoji
    retrieval functions based on the provided arguments.

    Command-line Arguments
    ---------------------
    --random : bool
        Get a random emoji
    --random_by_category : str
        Get a random emoji from the specified category
    --all : bool
        Get all emojis
    --all_by_category : str
        Get all emojis from the specified category
    --search : str
        Search for emojis by name

    Error Handling
    -------------
    - Handles network errors (RequestException)
    - Handles invalid category names
    - Handles malformed API responses
    - Handles invalid search queries

    Examples
    --------
    Get a random emoji:
    $ python main.py --random

    Search for emojis:
    $ python main.py --search "cat"

    Get all emojis from a category:
    $ python main.py --all_by_category "food and drink"
    """
    parser = argparse.ArgumentParser(description="Get emojis from Emojihub.")
    parser.add_argument("--random", action="store_true", help="Get a random emoji.")
    parser.add_argument("--random_by_category", type=str, help="Get a random emoji from a category.")
    parser.add_argument("--all", action="store_true", help="Get all emojis.")
    parser.add_argument("--all_by_category", type=str, help="Get all emojis from a category.")
    parser.add_argument("--search", type=str, help="Search for emojis by name.")
    
    args = parser.parse_args()

    try:
        if args.search:
            try:
                results = search_emoji(args.search)
                if results:
                    print(f"Found {len(results)} emoji(s) matching '{args.search}':")
                    for emoji in results:
                        print_emoji(emoji)
                        print("-" * 50)
                else:
                    print(f"No emojis found matching '{args.search}'")
            except ValueError as e:
                print(f"Invalid search query: {e}")
                return 1
                
        elif args.random:
            emoji = get_random_emoji()
            print_emoji(emoji)
            
        elif args.random_by_category:
            try:
                validate_category(args.random_by_category)
                emoji = get_random_by_category(args.random_by_category)
                print_emoji(emoji)
            except ValueError as e:
                print(str(e))
                return 1
                
        elif args.all:
            emojis = get_all_emojis()
            print(f"Found {len(emojis)} emojis:")
            for emoji in emojis:
                print_emoji(emoji)
                print("-" * 50)
                
        elif args.all_by_category:
            try:
                validate_category(args.all_by_category)
                emojis = get_all_by_category(args.all_by_category)
                print(f"Found {len(emojis)} emojis in category '{args.all_by_category}':")
                for emoji in emojis:
                    print_emoji(emoji)
                    print("-" * 50)
            except ValueError as e:
                print(str(e))
                return 1
                
        else:
            print("Welcome to the Emoji Hub CLI! Here's a random emoji for you:")
            emoji = get_random_emoji()
            print_emoji(emoji)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return 1
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return 1
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error parsing API response: {e}")
        return 1
    except (KeyError, IndexError) as e:
        print(f"Error parsing emoji data: {e}")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
    main()