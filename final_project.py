
print('What type of Dungeons and Dragons character are you? Answer this short personality test to find out.')
birthday = str(input('Please enter your astrology sign, Ex. aquarius, sagittarius, et.,: '))
print()
name_birth = ('Cupcake', 'Krusk', 'Gimble', 'Hennet', 'Tordek', 'Ragnara', 'Sandharrow', 'Eulad', 'Xerxes', 'Avery', 'Quinn', 'Riley', 'Kingsley',)

name = 'a'

if birthday == ('aquarius'):
    name = name_birth[0]
elif birthday == ('pisces'):
    name = name_birth[1]
elif birthday == ('capricorn'):
    name = name_birth[2]
elif birthday == ('sagittarius'):
    name = name_birth[3]
elif birthday == ('scorpio'):
    name = name_birth[4]
elif birthday == ('libra'):
    name = name_birth[5]
elif birthday == ('virgo'):
    name = name_birth[6]
elif birthday == ('leo'):
    name = name_birth[7]
elif birthday == ('cancer'):
    name = name_birth[8]
elif birthday == ('gemini'):
    name = name_birth[9]
elif birthday == ('taurus'):
    name = name_birth[10]
elif birthday == ('aries'):
    name = name_birth[11]
else:
    print(str(input('Sorry, check your spelling and only use lowercase. Enter your astrology sign, Ex. aquarius, sagitarius, et.,: ')))

color = str(input('What is your favorite color? '))
print()

evil_adj = ('0', 'fine and dandy', 'gentle', 'unpleasant', 'sniveling', 'destructive', 'revolting', 'wicked', 'hateful', 'depraved', 'heinous')
clean_location = ('0', 'Buggers Swamp', 'Ratstool lagoon', 'Curmudgeon Cave', 'Fort solitude', 'Mediocre Village', 'Hillside Hamlet', 'Michaels Mansion', 'Crystal Castle', 'the Golden Temple of Ka', 'Anti-microbial Vaccum Chamber Palace')
char_race = ('0', 'zombie', 'troll', 'curmudgeon', 'gnome', 'dwarf', 'human', 'elf', 'pixie', 'leprechaun', 'wood sprite')
theft_noun =  ('0', 'cupcake', 'bleeding heart', 'social butterfly', 'destroyer', 'usurper', 'nimrod', 'cretin', 'devil', 'simpleton', 'slavedriver')
courage_weapon = ('0', 'large blunt object', 'branch from a willow tree', 'obtuse finger', 'unusually large thumb', 'flaming sword','death glare', '10,000 exploding fingers of fury manuever', '+3 utility knife', 'callous handshake', 'uncomfortable stare'  )
role = ('fighter', 'ranger', 'cleric', 'paladin', 'wizard', 'magic-user', 'thief', 'ninja', 'archer', 'jester', 'shaman')
clr = 'a'
if color == ('white'):
    clr = role[0]
elif color == ('black'):
    clr = role[1]
elif color == ('pink'):
    clr = role[2]
elif color == ('blue'):
    clr = role[3]
elif color == ('yellow'):
    clr = role[4]
elif color == ('red'):
    clr = role[5]
elif color == ('green'):
    clr = role[6]
elif color == ('orange'):
    clr = role[7]
elif color == ('purple'):
    clr = role[8]
elif color == ('brown'):
    clr = role[9]
elif color == ('maroon'):
    clr = role[10]
else:
    color = (str(input('Sorry, try a different color. What is your favorite color? ')))

charisma = int(input('On a scale from 1-10, ten being the highest, how often do you spend time for recreation? '))
print()
if charisma > 10:
    print(int(input('Sorry, please enter numbers 1-10 only. How often do you spend time for recreation? ')))
elif charisma <= 0:
    print(int(input('Sorry, please enter numbers 1-10 only. How often do you spend time for recreation? ')))
else:
    print(' ')
theft = int(input('On a scale from 1-10, ten being the highest, How often do you steal small items at work, in a hotel, or from your classmates? '))
print()
if theft > 10:
    print(int(input('Sorry, please enter numbers 1-10 only. How often do you steal small items at work, in a hotel, or from your classmates? ')))
elif charisma <= 0:
    print(int(input('Sorry, please enter numbers 1-10 only. How often do you steal small items at work, in a hotel, or from your classmates? ')))
else:
    print(' ')
clean = int(input('On a scale from 1-10, ten being the highest, how clean do you require your surroundings to be? '))
print()
if clean > 10:
    print(int(input('Sorry, please enter numbers 1-10 only. How clean do you require your surroundings to be? ')))
elif clean <= 0:
    print(int(input('Sorry, please enter numbers 1-10 only. How clean do you require your surroundings to be?')))
else:
    print(' ')
evil = int(input('On a scale from 1-10, ten being the highest, how much empathy do you have for seeing innocent people suffer while you benefit from their misfortune? '))
print()
if evil > 10:
    print(int(input('Sorry, please enter numbers 1-10 only. How much empathy do you have for seeing innocent people suffer while you benefit from their misfortune?')))
elif evil <= 0:
    print(int(input('Sorry, please enter numbers 1-10 only. How much empathy do you have for seeing innocent people suffer while you benefit from their misfortune?')))
else:
    print(' ')
courage = int(input('On a scale from 1-10, ten being the highest, how much courage do you have in killing spiders? '))
print()

import textwrap
print('Congratulations! You are %s the %s %s of %s!' % (name, evil_adj[evil], theft_noun[theft], clean_location[clean]))
print('You are a %s %s and your weapon of choice is your %s.' % (char_race[charisma], clr, courage_weapon[courage]))
beginning = (str(input('Do you wish to continue? Y/N' + '\n')))
if beginning == ('n'):
    print('So sorry to hear that! Quitting is the cowards way out. Have fun pecking around the yard for feed and laying eggs. Good-bye!')
elif beginning ==('y'):
    strs = 'Excellent!!!! Now our adventure can begin! Imagine you find yourself in a strange building on Highline campus you have never seen before.' \
           ' You walk cautiously down the hallway and come to a T intersection. You are facing a very large bookshelf. Half lazily looking at it while pondering your next move you ' \
           'slowly realize that all of the redbacked books on the shelf stand out and spell the word, KANG. Just then a large booming voice comes over the speakers. Who dares enter' \
           ' the building of Professor Kang! Imediately a swarm of bats come flying out from an opening in the ceiling.'
print(textwrap.fill(strs, 75))

user_input = (str(input('%s the %s %s dives to the floor: '
                'Make a dexterity roll by randomly choosing any lowercase alphabet key to continue....' % (name, evil_adj[evil], theft_noun[theft]))))
print()

def dexterity():
    for (str) in user_input:
        if ('a' <= (str) <= 'g'):
            print('%s the %s %s just barely misses. -0 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
        elif ('h' <= (str) <= 's'):
            print('%s the %s %s cannot get out of the way in time. -5 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
        elif ('t' <= (str) <= 'z'):
            print('%s the %s %s fails utterly and completely. -10 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
dexterity()

strs = 'You get up, dust yourself off and notice a clue. A pair of size 12 footprints go left down the corrider. That must be Professor Kang! ' \
       'You walk down the corrider keeping an eye out for bats. The corrider leads to an open room full of cobwebs. You can see a light at the far end ' \
       'and move towards it. The cobwebs are getting thicker now, so thick you begin to wonder if they are even spiderwebs at all. As you get closer to the ' \
       'light you catch movement out of the corner of your eyes. About that time you trip and fall on something big and heavy. ' \
       'That is when you realize you are surrounded by large spiders that were feeding on the mummified corpse of a student intern. And now they are coming towards you!' + '\n'
print(textwrap.fill(strs, 75))
user_input = (str(input('You raise your %s high as %s the %s prepares for battle: '
                'Make a strength roll and randomly choose any lowercase alphabet key to continue....\n' % (courage_weapon[courage], name, theft_noun[theft]))))
print()
def strength():
    for (str) in user_input:
        if ('a' <= (str) <= 'g'):
            print('The %s is swung violently against the floor and bounces back in your face. -10 pts.\n' % (courage_weapon[courage]))
        elif ('h' <= (str) <= 's'):
            print('You cannot wield the %s effectively because your %s is wet -gross. +0 pts.\n' % (courage_weapon[courage], courage_weapon[courage]))
        elif ('t' <= (str) <= 'z'):
            print('Nothing can withstand the might of your %s. +10 pts.\n' % (courage_weapon[courage]))
strength()

strs = 'You head towards the light and discover it is the light to an open elevator door. You get inside ' \
       'and decide Professor Kang is most likely on the top floor.  Only the best for Professor Kang, you grimace.' \
       ' You try the button. Nothing happens. You try again, nothing. Two minutes later of kicking and cursing a ' \
       'ceiling panel falls down and hits you on the head. $@$*?$! and then you notice it leads to the elevator shaft. ' \
       'OK you think to yourself. I have been through bats and spiders so far so what is a little climb compared to that? You ' \
       'climb up to the cable and give it all you got. As you near the top you are surprised at how much energy you still have. ' \
       'Finally all of those trips to the gym paid off! With all that left over energy you easily swing yourself onto the floor in ' \
       'one heroic leap. And as you land you realize the shiny floor is shiny because it is all slippery and slick like black ice. No!!!!!' + '\n'
print(textwrap.fill(strs, 75))
user_input = (str(input('%s the %s %s is approaching the floor at break neck speed: '
                'Make a dexterity roll by randomly choosing any lowercase alphabet key to continue....' % (name, evil_adj[evil], theft_noun[theft]))))
print()

def dexterity():
    for (str) in user_input:
        if ('a' <= (str) <= 'g'):
            print('%s the %s %s just barely misses. -0 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
        elif ('h' <= (str) <= 's'):
            print('%s the %s %s cannot get out of the way in time. -5 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
        elif ('t' <= (str) <= 'z'):
            print('%s the %s %s fails utterly and completely. -10 pts.\n' % (name, evil_adj[evil], theft_noun[theft]))
dexterity()

strs = 'After you gather your bearings you realize the floors were freshly waxed. ' \
       'Nothing but the best for Professor Kang, you lament. Is that so?, a voice from behind you says. ' \
       'You whirl around and see yourself face to face with the Professor Kang! Or rather, face to ' \
       'belt buckle because Professor Kang is huge! However, despite his size he does look just ' \
       'like his canvas highline picture. He opens his mouth and breathes fire, his eyes glow red and as ' \
       'he tilts his head back a laser beam shoots out from under his nose!' + '\n'
print(textwrap.fill(strs, 75))

user_input = (str(input('You raise your %s high as %s the %s prepares for battle: '
                'Make a strength roll and randomly choose any lowercase alphabet key to continue....\n' % (courage_weapon[courage], name, theft_noun[theft]))))
print()
def strength():
    for (str) in user_input:
        if ('a' <= (str) <= 'g'):
            print('The %s is swung violently against the floor and bounces back in your face. -10 pts.\n'  % (courage_weapon[courage]))
        elif ('h' <= (str) <= 's'):
            print('You cannot wield the %s effectively because your %s is wet -gross. +0 pts.\n' % (courage_weapon[courage], courage_weapon[courage]))
        elif ('t' <= (str) <= 'z'):
            print('Nothing can withstand the might of your %s. +10 pts.\n' % (courage_weapon[courage]))
strength()

strs = 'The great Professor Kang suddenly lurches backwards, then forwards, then backwards again before ' \
       'crashing to the floor! You gingerly walk over to the behemoth giant and notice something printed ' \
       'on the side of his neck. Made in China it says. What?! This was not Professor Kang at all but a robot. ' \
       'At about that time a very handsome, distinguished, refined, gentleman steps out from behind a curtain. ' \
       'I see you defeated my robot. Well I guess it can not be helped. I will just build another one with my godlike ' \
       'knowledge of python and the secrets of the universe. You see, for me building that robot is no more difficult ' \
       'than it is for an imbecile to wipe his nose with the back of his hand. But I digress, clearly you had a good ' \
       'reason to spend so much trouble to seek my audience. And now you have it. So, as the laymen say, what can I do you for? ' \
       'You look upon the greatness that is Professor Kang and you suddenly blurt out, My grades! In python class! ' \
       'How did I do?! To the embaressment of both of you. Professor Kang replies, Ah yes, your grades. Let us see, in my ' \
       'infinite wisdom I constructed the obstacles within this building as a test. If you want to know how you did in ' \
       'class, simply look at the results of your time in this obstacle course. Shall I show you? It is the least I can do.'  + '\n'
print(textwrap.fill(strs, 75))

ending = (str(input('Do you wish to know your final grade on the obstacle course? Y/N' + '\n')))
print()
if ending == ('n'):
    print('As you give your answer you are shocked to see he is already on his way out. Grades are posted on canvas! Next time take my advice and trust me when I say canvas is the best way to reach me!')

elif ending ==('y'):
    strs = 'Here is how you did:'



cont = (str(input('Play again? Y/N' + '\n')))