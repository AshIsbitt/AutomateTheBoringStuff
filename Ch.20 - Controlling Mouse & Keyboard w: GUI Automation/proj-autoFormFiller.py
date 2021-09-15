# Automatically fill in the sections of a form

# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

import pyautogui as pyag
import time

# Get data to enter to form
formData = [{'name': 'Stephen',
             'fear': 'Spiders',
             'source': 'wand',
             'robocop': 4,
             'comments': 'Tell bob I say hi'}]

# Start typing data into form
for person in formData:
    # Give user a chance to kill the script
    print('FIVE SECOND PAUSE TO ESCAPE PROGRAM')
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    pyag.write(['\t', '\t', '\t'])

    # Name field
    print(f"Name: {person['name']}")
    pyag.write(person['name'] + '\t')

    # Greatest Fear
    print(f"Greatest Fear: {person['fear']}")
    pyag.write(person['fear'] + '\t')

    # Handling Lists
    if person['source'] == 'Wand':
        pyag.write(['down', 'enter', '\t'], duration=1)
    elif person['source'] == 'Amulet':
        pyag.write(['down', 'down', 'enter', '\t'], duration=1)
    elif person['source'] == 'crystal ball':
        pyag.write(['down', 'down', 'down', 'enter', '\t'], duration=1)
    elif person['source'] == 'Money':
        pyag.write(['down', 'down', 'down', 'down', 'enter', '\t'], duration=1)

    # Handling Radio Buttons
    if person['robocop'] == '1':
        pyag.write([' ', '\t'], 0.5)
    elif person['robocop'] == '2':
        pyag.write(['right', '\t'], 0.5)
    elif person['robocop'] == '3':
        pyag.write(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == '4':
        pyag.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == '5':
        pyag.write(['right', 'right', 'right', 'right', '\t'], 0.5)

    # Additional Comments
    pyag.write(person['comments'] + '\t')

    # Press submit
    time.sleep(0.5)
    pyag.press('enter')

    # Wait for form page to load
    print('Form Submitted')
