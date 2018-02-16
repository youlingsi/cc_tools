import cc_data

"""
create and return a Map Title Field from json Field values
"""
def makeFieldMapTitle(field):
    title = field["title"]
    fieldMapTitle = cc_data.CCMapTitleField(title)
    return fieldMapTitle

"""
create and return a Encoded Password Field from json Field values
"""
def makeFieldEncedPassword(field):
    password = field["password"]
    fieldPassword = cc_data.CCEncodedPasswordField(password)
    return fieldPassword

"""
create and return a Hint Text Field from json Field values
"""
def makeFieldHintTxt(field):
    hint = field["hint"]
    fieldHint = cc_data.CCMapHintField(hint)
    return fieldHint

"""
create and return a Monster Field from json Field values
"""
def makeFieldMonster(field):
    monsters = []
    for cord in field["monster coordinates"]:
        ccCord = cc_data.CCCoordinate(cord["x"],cord["y"])
        monsters.append(ccCord)
    fieldMonster = cc_data.CCMonsterMovementField(monsters)
    return fieldMonster

"""
create and return a Trap Control Field from json Field values
"""
def makeFieldTrapControl(field):
    traps = []
    for trap in field["traps"]:
        trapControl = cc_data.CCTrapControl(trap["brown buttonX"],
                                    trap["brown buttonY"],
                                    trap["trapX"],
                                    trap["trapY"])
        traps.append(trapControl)
    fieldTrapControl = cc_data.CCTrapControlsField(traps)
    return fieldTrapControl

"""
create and return a Clone Machine Field from json Field values
"""
def makeFieldCloneMachine(field):
    machines = []
    for machine in field["machines"]:
        cloneMachines = cc_data.CCCloningMachineControl(machine["red buttonX"],
                                                        machine["red buttonY"],
                                                        machine["machineX"],
                                                        machine["machineY"])
        machines.append(cloneMachines)
    fieldCloneMachines = cc_data.CCCloningMachineControlsField(machines)
    return fieldCloneMachines


"""
create the optional fields data from json optional fields data
1. loop through all the objects in optional fields data
2. create related field variable and add it to the list
3, return the list of optional values
"""
def inputOptionalFields(fields):
    optionalFields = []
    ccField = cc_data.CCField(0,b'')
    for field in fields:
        fieldType = field["type"]
        if fieldType == 3:
            ccField = makeFieldMapTitle(field)
        elif fieldType == 4:
            ccField = makeFieldTrapControl(field)
            print(ccField)
        elif fieldType == 5:
            ccField = makeFieldCloneMachine(field)
            print(ccField)
        elif fieldType == 6:
            ccField = makeFieldEncedPassword(field)
        elif fieldType == 7:
            ccField = makeFieldHintTxt(field)
        elif fieldType == 10:
            ccField = makeFieldMonster(field)
        else:
            continue
        optionalFields.append(ccField)
    return optionalFields

"""
create the level data for a single level from json level data
1.take the level data within the json file
2.input related value to the class
3.handle the optionfields
4.return a ccLevel object
"""
def makeDataLevel(level):
    dataLevel = cc_data.CCLevel()
    dataLevel.level_number = level["level number"]
    dataLevel.num_chips = level["number of chips"]
    dataLevel.time = level["time"]
    dataLevel.upper_layer = level["upper level"]
    dataLevel.lower_layer = level["lower level"]
    dataLevel.optional_fields = inputOptionalFields(level["optional fields"])
    return dataLevel

"""
create the data file object
1. import all levels 
2. return a ccDatafile object
"""
def makeDataFile(jsonData):
    dataFile = cc_data.CCDataFile()
    for level in jsonData["levels"]:
        dataLevel = makeDataLevel(level)
        dataFile.add_level(dataLevel)
    return dataFile







    
