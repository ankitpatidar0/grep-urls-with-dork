# Google Dork Search Script

## Overview

This Python script allows users to perform Google searches using predefined or custom Google dorks and save the search results to a file.

## Dependencies

- [googlesearch-python](https://pypi.org/project/googlesearch-python/)

## Installation

1. Install the required dependencies using the following command:

    ```bash
    pip install googlesearch-python
    ```

2. Download the script (`google_dork_search.py`) to your local machine.

## Usage

1. Run the script using the following command:

    ```bash
    python google_dork_search.py
    ```

2. Choose a Google dork or enter a custom dork when prompted.

3. Enter the number of search results to retrieve.

4. The script will display the search results and save them to a file named `search_results.txt`.

## Google Dork Options

1. `intitle:'Index of' filetype:log`
2. `site:example.com intitle:index.of`
3. `inurl:/wp-content/uploads/ filetype:pdf`

## Custom Dork

If you choose option 4, you can enter your own custom dork when prompted.

## File Output

The search results are saved to a file named `search_results.txt`.

## Note

- Ensure that you have an active internet connection to perform Google searches.

## License

This script is released under the [MIT License](LICENSE).
