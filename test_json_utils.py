import test_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    
    #Loop through the json_data
    for gm in json_data["gameList"]:
        #Create a new Game object from the json_data by reading
        gmObj = test_data.Game()
        #  title
        gmObj.title = gm["title"]
        #  year
        gmObj.year = gm["Year"]
        #  platform (which requires reading name and launch_year)
        gmPlatform = test_data.Platform()
        gmPlatform.launch_year = gm["platform"]["launch year"]
        gmPlatform.name = gm["platform"]["name"]
        gmObj.platform =gmPlatform
        #Add that Game object to the game_library
        game_library.add_game(gmObj)
    #Return the completed game_library
    return game_library
