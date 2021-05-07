# Class for creating rooms
class Room:
    def __init__(self, name):
        self.name = name
        self.exits =[]
        self.exitLocations = []
        self.features = []
        self.featureDescriptions = []
        self.items = []

    # Adds exits and exit locations to a room
    def addExit(self, theexit, room):
        self.exits.append(theexit)
        self.exitLocations.append(room)

    # Adds items to a room
    def addFeature(self, item, desc):
        self.features.append(item)
        self.featureDescriptions.append(desc)

    # Adds an item to room
    def addItem(self, item):
        self.items.append(item)

    # Removes an item from room when used
    def remvItem(self, item):
        self.items.remove(item)

    # String function returns
    def __str__(self):
        #
        roomName = '{}\n'.format(self.name)

        roomDesc = 'In this room, there is:'
        for features in self.features:
            roomDesc += ' '
            roomDesc += features


        roomExits = 'The exits in this room are located {}\n'.format(self.exits)

        string = (roomName + roomDesc + '.\n' + roomExits)
        return string

# Begin constructing the game space- THE HAUNTED MANSION
# For a fresh game, set player in foyer
# For loaded file, set location to savefile location, set inventory to savefile inventory, and
# remove any items in inventory from relevant rooms
def createRooms():
    global location

    # First Floor- Creates named rooms, which can have attributes added in later through functions
    # for easier visualization of the gamespace
    foyer = Room('The Foyer. The wood floors are cracked and pitted, and the broken windows show nothing but a thick, featureless fog.')
    diningHall = Room('The Dining Hall. A huge, multi-course meal has been set up on a long table...about a decade ago, it appears.')
    library = Room('The Library. The books are in suprisingly good condition, given the multiple leaks in the roof here. You can almost read the spines!')

    # Second Floor
    landing = Room('The Landing at the Top of the Stairs. The light mist seen from the bottom of the stairs suddenly seems must thicker, and you can almost see faces in it.')
    armory = Room('The Armor Room. Dozens of suits of rusted-out armor line the long room to either side of the door, standing in front of a variety of completely ruined banners.')
    childRoom = Room('The Child\'s Bedroom. A crib with peeling white paint sits underneath a creaking, slowly spinning mobile. On the other side of the room is a cracked porcelain doll.')
    masterRoom = Room('The Master Bedroom. A four poster bed in the middle room is obscured by theadbare satin curtains. You think you can make out a man\s figure behind it.')
    lockedStudy = Room('The Mysterious Study. You finally enter into the mysterious study. There is an oppressive atmosphere.')

    # Basement
    laboratory = Room('The Underground Laboratory. Coming down the ladder, you enter a surprisingly clean room, filled with bubbling beakers and Tesla coils.')

    # Begin adding attributes to the rooms
    # Starting with the foyer:
    # Add exits:
    foyer.addExit('western_door', diningHall)
    foyer.addExit('eastern_door', library)
    foyer.addExit('stairway', landing)

    # Now we add inspectable features:
    foyer.addFeature('carpet', 'A long rug spills down the stairway, all the way across the foyer, and to the front door of the foyer.')
    foyer.addFeature('stairs', 'A stairway leads to an upper landing. You think someone must have left a window open, as there is a light mist spilling down it.')
    foyer.addFeature('pedestal', 'A pedestal with a worn, near-featureless bust atop it stands guard by the doorway.')
    foyer.addFeature('front_door', 'The front door was right behind you, you\'re sure. It appears to have disappeared entirely.')
    foyer.addFeature('seal', 'Barely legible against the ruined floorboards, an engraved family crest depicts a cackling skull on a cracked shield.')

    # No items to pick up here, so we move to the Dining Hall.
    diningHall.addExit('eastern_door', foyer)

    # Dining hall features
    diningHall.addFeature('food', 'All of the food is rotted. At least on rat flees from any plate you approach.')

    # Library exits
    library.addExit('western_door', foyer)
    library.addExit('trapdoor', laboratory)

    # Library features
    library.addFeature('rug', 'Underneath a rotting rug in the corner is a trapdoor. It emits a faint odor of formaldehyde.')
    library.addFeature('bookshelf', 'The sagging bookshelf holds books that almost seem to be melting. When you try to grab one, the piece you grabbed breaks off, and a couple worms fall out.')

    # Laboratory Exits
    laboratory.addExit('ladder', library)

    # Lab features
    laboratory.addFeature('beaker', 'A green bubbling liquid is heating over a Bunsen burner. To your surprise, it actually boils faster when you remove it from the heat.')
    laboratory.addFeature('table', 'A cold metal slab table takes center stage in the room. There are four steel shackles along the edges, and an enormous lever next to the Tesla coil at it\'s head. The shackles are broken.')

    # Landing exits
    landing.addExit('northern_door', armory)
    landing.addExit('western_door', childRoom)
    landing.addExit('eastern_door', masterRoom)

    # Landing features
    landing.addFeature('mist', 'Any time you focus on one point in the mist for too long, a hand shoots out from it toward your face. It just brushes past you, but you think that may not be a great idea.')

    # Child's Room exits
    childRoom.addExit('eastern_door', landing)

    # Child's room features
    childRoom.addFeature('doll', 'One of the doll\'s painted eyes has a crack right through it. It is sitting in a tiny rocking chair in the middle of a pile of toys broken beyond recognition. Anytime you look away, you swear the chair starts rocking.')
    childRoom.addFeature('mobile', 'Taking a closer look at the mobile, you can tell that it is made of painted bird skulls. Some still have bits of feather and viscera stuck underneath the splotchy paint.')

    # Master bedroom exits
    # Locked study exit will be added later, through item finding puzzle
    masterRoom.addExit('western_door', landing)

    # Master bedroom features
    masterRoom.addFeature('curtains', 'When you pull back the curtains, the figure behind them disappears. When you replace the curtain, the figure returns.')
    masterRoom.addFeature('strange_door', 'In a house full of rotting wood and crumbling stone, the last thing you thought you\'d see was an oaken door in pristing condition, and the second to last thing you thought you would see was a glistening brass lock.')

    # Armor room exits
    armory.addExit('southern_door', landing)

    # Armor room features
    armory.addFeature('shivering_armor', 'One suit of armor in the corner, smaller in stature to the others, seems to be quivering. There is a spectral_key around his neck.')

    # Armor room items
    armory.addItem('spectral_key')
    # Locked study exits
    lockedStudy.addExit('southern_door', masterRoom)

    # Locked study feeatures
    lockedStudy.addFeature('hearth', 'Though this house has been long abandoned, the fire in the hearth still burns.')

    # Set the current room
    location = foyer

# Start the game
createRooms()
# Add the player inventory
inventory = []
# Implement game responses to player
# Run until the game is won or player quits
victory = False
while victory == False:
    player = 'You are in {}\nIn your bag, you have {}\n'.format(location, inventory)

    if location == None:
        victory = True

    print(player)

    # Implement verbs to traverse and interact with the game
    do = input('What should I do? ')
    do = do.lower()

    # When a player quits, create a save file
    if do == 'quit':
        savefile = open('Save_File', 'W')
        savefile.writelines(inventory, '\n', location)
        savefile.close()
        break

    # Set a default response to incorrect verbs
    response = 'That is not a valid action.\nYour verbs are GO, LOOK, and TAKE.\nType your action in \"verb noun\" format.'

    # Split the player input into two words
    action = do.split()

    # Read in any valid 2 word inputs
    if len(action) == 2:
        verb = action[0]
        noun = action[1]

        # Implement the GO verb
        if verb == 'go':
            # Default response
            response = 'Invalid Exit'

            for i in range(len(location.exits)):
                if noun == location.exits[i]:
                    # Move player to room associated with exits in createRoom function
                    location = location.exitLocations[i]

                    response = 'Moved to new room.'
                    break

        # Implement the LOOK verb
        elif verb == 'look':
            # Default response
            response == 'There isn\'t anything in this room matching that description.'

            # Look for features in the room
            for i in range(len(location.features)):
                # If player has input a valid feature
                if noun == location.features[i]:
                    response = location.featureDescriptions[i]
                    break

        # Implement the TAKE verb
        elif verb == 'take':
            # Default response
            response = 'There is no such item in this room.'

            # Check for valid items in the room
            for items in location.items:
                # Found a valid item
                if noun == items:
                    # Add item to inventory
                    inventory.append(items)

                    # Remove item from room
                    location.remvItem(items)

                    # Let player know the item is retrieved.
                    response = 'You picked up {}'.format(items)
                    break
    # Display response
    print('\n{}'.format(response))



#### Game is implemented in basic form
#### To do: Game Winnable, Save/Load feature, One more item to collect, One text entry puzzle
#### Add point values to the items, 25 points apiece
#### Implement USE verb, to unlock the door- USE verb must be implemented separately every time
#### something can be used, and in this case it is a) "open" a door by adding a new door to the
#### master bedroom, and USE the hearth to burn the remains for 25 points each
#### When 100 points are gained, change victory == True, and play a victory message
#### When a player enters quit, save all relevant data to an outfile. When a player starts the
#### game, before starting the menu, ask if they want to start a new game or load a save file.
####
