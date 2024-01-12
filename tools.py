import json
from googlesearch import search

def get_search_results(query, num_results=10):
    results = []
    try:
        # Perform the Google search and collect results until we reach the desired number
        for result in search(query, num_results=num_results, stop=None):
            results.append(result)
            # Break the loop when we reach the desired number of results
            if len(results) >= num_results:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    return results

def main():
    print("Choose a Google dork or enter your own:")
    print("1. intitle:'Index of' filetype:log")
    print("2. site:example.com intitle:index.of")
    print("3. inurl:/wp-content/uploads/ filetype:pdf")
    print("4. Enter your own custom dork")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        search_query = "intitle:'Index of' filetype:log"
    elif choice == '2':
        search_query = "site:example.com intitle:index.of"
    elif choice == '3':
        search_query = "inurl:/wp-content/uploads/ filetype:pdf"
    elif choice == '4':
        search_query = input("Enter your custom dork: ")
    else:
        print("Invalid choice. Exiting.")
        return

    # Get the number of results to retrieve
    num_results = int(input("Enter the number of results to retrieve: "))

    # Get the search results
    search_results = get_search_results(search_query, num_results)

    # Display the search results
    print("\nSearch Results:")
    for result in search_results:
        print(result)

    # Save the search results to a file
    with open('search_results.txt', 'w') as file:
        for result in search_results:
            file.write(result + '\n')
    print("Search results saved to 'search_results.txt'.")

if __name__ == "__main__":
    main()
