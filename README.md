# LeXmash

LeXmash is a wordlist generation tool designed to assist with creating personalized wordlists based on victim information. It takes various personal details provided by the user and generates a wordlist containing combinations and permutations of the information.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the source code for LeXmash.

2. Open a terminal or command prompt and navigate to the directory where the LeXmash code is located.

3. Run the following command to install the required dependencies:
   ```
   pip install argparse
   ```

4. Run the tool using the following command:
   ```
   python LeXmash.py
   ```

5. Follow the prompts to provide the victim's information, such as their first name, last name, birthdate, birthplace, pet names, parents' names, favorite superhero, favorite musician, favorite movie, children's names, and partner's name.

6. Once all the information is provided, LeXmash will generate a wordlist based on the victim's details and save it in a file named `wordlist.txt`.

## How it Works

LeXmash uses the `argparse` module to handle command-line arguments and provide a help message when needed.

The tool consists of the following main functions:

### `get_victim_info()`

This function prompts the user to enter various victim information, such as their first name, last name, birthdate, birthplace, whether they have pets, parents' names, favorite superhero, favorite musician, favorite movie, whether they have children, and partner's name. The function collects this information and returns it as a dictionary.

### `generate_wordlist(victim_info)`

This function takes the victim's information as input and generates a wordlist based on the provided details. It creates combinations and permutations of the victim's information, including their names, birthdate, birthplace, favorite superhero, favorite musician, favorite movie, and parents' names. If the victim has pets, children, or a partner, it also includes variations of their names and common patterns such as appending numbers and exclamation marks. The function returns the generated wordlist.

### `generate_wordlist_file(wordlist)`

This function takes the generated wordlist as input and writes it to a file named `wordlist.txt`. Each word in the wordlist is written on a separate line.

### `main()`

The `main()` function serves as the entry point for the LeXmash tool. It sets up the argument parser, calls `get_victim_info()` to collect the victim's information, generates the wordlist using `generate_wordlist()`, and then saves the wordlist to a file using `generate_wordlist_file()`.

## Contributing

Contributions to LeXmash are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## Disclaimer

LeXmash is intended for educational and ethical use only. The tool should not be used for any unauthorized or malicious activities. The developers of LeXmash are not responsible for any misuse or damage caused by the tool.

## License

LeXmash is released under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](https://github.com/MehdiMsa/LeXmash/main/LICENSE) file for more details.
