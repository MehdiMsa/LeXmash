import argparse
import itertools


def generate_wordlist(victim_info):
    wordlist = []

    # Extract victim information
    first_name = victim_info.get('first_name', '')
    last_name = victim_info.get('last_name', '')
    birthdate = victim_info.get('birthdate', '')
    birthplace = victim_info.get('birthplace', '')
    has_pets = victim_info.get('has_pets', False)
    pets = victim_info.get('pets', [])
    favorite_superhero = victim_info.get('favorite_superhero', '')
    favorite_musician = victim_info.get('favorite_musician', '')
    favorite_movie = victim_info.get('favorite_movie', '')
    has_children = victim_info.get('has_children', False)
    children_names = victim_info.get('children_names', [])
    has_partner = victim_info.get('has_partner', False)
    partner_name = victim_info.get('partner_name', '')

    # Generate combinations of victim information
    combinations = [first_name, last_name, birthdate.replace('/', ''), birthplace, favorite_superhero,
                    favorite_musician, favorite_movie] + pets + children_names
    for r in range(1, len(combinations) + 1):
        for combination in itertools.permutations(combinations, r):
            wordlist.append(''.join(combination))

    # Generate variations with special characters
    special_chars = ['!', '@', '#', '$', '%', '&']
    for word in wordlist.copy():
        for char in special_chars:
            wordlist.append(word + char)
            wordlist.append(word + char + birthdate[-2:])

    # Generate possible default passwords
    default_passwords = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome', 'login', 'secret']
    for password in default_passwords:
        wordlist.append(password)
        wordlist.append(password + birthdate[-2:])

    return wordlist


def get_victim_info():
    victim_info = {}

    print('----- Victim Information -----')
    victim_info['first_name'] = input('First Name: ')
    victim_info['last_name'] = input('Last Name: ')
    victim_info['birthdate'] = input('Birthdate (dd/mm/yyyy): ')
    victim_info['birthplace'] = input('Birthplace: ')

    has_pets = input('Do you have any pets? (y/n): ')
    if has_pets.lower() == 'y':
        victim_info['has_pets'] = True
        num_pets = int(input('Number of Pets: '))
        victim_info['pets'] = []
        for i in range(num_pets):
            pet_name = input(f'Enter Pet #{i + 1} Name: ')
            victim_info['pets'].append(pet_name)
    else:
        victim_info['has_pets'] = False

    victim_info['favorite_superhero'] = input('Favorite Superhero: ')
    victim_info['favorite_musician'] = input('Favorite Musician: ')
    victim_info['favorite_movie'] = input('Favorite Movie: ')

    has_children = input('Do you have any children? (y/n): ')
    if has_children.lower() == 'y':
        victim_info['has_children'] = True
        num_children = int(input('Number of Children: '))
        victim_info['children_names'] = []
        for i in range(num_children):
            child_name = input(f'Enter Child #{i + 1} Name: ')
            victim_info['children_names'].append(child_name)
    else:
        victim_info['has_children'] = False

    has_partner = input('Do you have a partner? (y/n): ')
    if has_partner.lower() == 'y':
        victim_info['has_partner'] = True
        partner_name = input('Partner Name: ')
        victim_info['partner_name'] = partner_name
    else:
        victim_info['has_partner'] = False

    return victim_info


def generate_wordlist_file(wordlist, first_name, last_name):
    filename = f'{first_name}_{last_name}_wordlist.txt'
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

    print(f'Wordlist file "{filename}" generated successfully.')


def main():
    parser = argparse.ArgumentParser(description='LeXmash Wordlist Generator')
    parser.add_argument('-help', action='help', help='Show this help message and exit')
    args = parser.parse_args()

    victim_info = get_victim_info()
    wordlist = generate_wordlist(victim_info)
    generate_wordlist_file(wordlist, victim_info['first_name'], victim_info['last_name'])


if __name__ == '__main__':
    main()
