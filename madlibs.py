# youtuber = 'Bibek Kumar Ghosh'
# print('subscribe to ' + youtuber)
# print('subscribe to {}'.format(youtuber))
# print(f'subscribe to {youtuber}')

# adj = input('Adjective: ')
# verb1 = input('Verb: ')
# verb2 = input('Verb: ')
# famous_person = input('Famous person: ')
#
# madlib1 = f'Computer programming is so {adj}! It makes me so excited all the time because \
# I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! '
import random


def mcu():
    quote_content = ''
    try:
        quote = input('Quote no: ')
        if quote == '1':
            adj = input('Adjective: ')

            quote1 = f'''"That's my secret, Captain. I'm always {adj}." -Hulk'''
            quote_content = quote1

        elif quote == '2':
            verb = input('Verb: ')
            digit = input('Digit: ')
            quote2 = f'''I wish I also had some to say "I {verb} you, {digit} to."'''
            quote_content = quote2

        elif quote == '3':
            some_cute_animal = input('Name a cute animal: ')
            stupid_made_up_weapon = input('Imaginary weapon: ')
            quote3 = f'''"We're fighting an army of {some_cute_animal} and I have a {stupid_made_up_weapon}. \
None of this makes sense." -Hawk-eye'''
            quote_content = quote3

        elif quote == '4':
            favourite_material_possession = input('Your favourite material possession: ')
            quote4 = f'''"If you're nothing without the {favourite_material_possession}, \
then you shouldn't have it." -Tony'''
            quote_content = quote4

    finally:
        random_quotes = ['"Whatever it takes." -Cap', '"I have nothing to prove to you." -Carol', '''"She's not alone."\
-Black Widow''', '"I can do this all day." -Cap']
        quote_content += '\n\n'
        quote_content += random.choice(random_quotes)
        return quote_content


def general():
    person = input('Type (man/woman/boy/girl): ')
    state_name = input('Choose a state in any country: ')
    verb1 = input('Stupid activity(eg.jump, run): ')
    common_noun2 = input('Random object(eg.wall, pole, tree): ')
    proper_noun1 = input('Random name of a person: ')
    proper_noun2 = input('Another random name: ')
    common_noun3 = input('Relative: ')
    body_part = input('Some body part: ')
    common_noun4 = input('Random object')
    story = f'''A {person} in {state_name} was arrested this morning after he {verb1}ed a {common_noun2} in front of \
{proper_noun1}. {proper_noun2}, had a history of {verb1}ing, but no one, not even his {common_noun3} ever imagined \
they'd {verb1} with a {common_noun4} stuck in his {body_part}.'''

    return story


def november_day():
    adj = input('Adjective: ')
    adj2 = input('Another adjective: ')
    type_of_bird = input('Type of bird: ')
    room_in_a_house = input('Room in a house: ')
    verb_pst = input('Any verb in past tense: ')
    verb = input('Verb: ')
    relative_name = input('Relative: ')
    food_item = input('Food item: ')
    some_liquid = input('Some liquid (preferably not drinkable): ')
    verb_ing = input('Verb in "ing" form: ')
    part_of_body_plural = input('Part of body(but plural like eyes,ears, legs, etc): ')
    plural_noun = input('Plural noun: ')
    verb_ing_2 = input('Verb in "ing" form: ')
    noun = input('Noun: ')

    story = f'''It was a {adj}, cold November day. I woke up to the {adj2} smell of {type_of_bird} roasting in \
the {room_in_a_house} downstairs. I {verb_pst} down the stairs to see if I could help {verb} the dinner. My mom said,\
"See if {relative_name} needs a fresh {food_item}." So I carried a tray of glasses full of {some_liquid} into the \
{verb_ing} room. When I got there, I couldn't believe my {part_of_body_plural}! There were {plural_noun} {verb_ing_2} \
on the {noun}!'''

    return story


print(november_day())

