def CoreFunc():

    # load database of car
    AllCars = CarDatabase()

    # Greet the customer
    (ProgMenu1, LenProgMenu1, MenuLines,
        MenuSides, MenuTitle) = DisplayStartMenu()
    print('')
    print(MenuTitle)
    print(MenuSides)
    print(ProgMenu1)
    print(MenuSides)
    print(MenuLines)

    CarRentMenu(AllCars)


def CarRentMenu(AllCars):

    UserI = input(
        '\nPick up the option by typing it\'s number in the brackets: ')

    PermitedInput = ['1', '2', '3', '4']

    while UserI not in PermitedInput:
        print('\nWrong value, please enter only num 1 to 4.')
        UserI = input(
            '\nPick up the option by typing it\'s number in the brackets: ')

    UserI = int(UserI)

    if UserI == 1:
        AvailableCarsFunc(AllCars)
    elif UserI == 2:
        SearchCarMenu(AllCars)
    elif UserI == 3:
        RentCarFunc(AllCars)
    elif UserI == 4:
        ByeMessage = 'Thank you, have a nice day'
        GoodByeMessage(ByeMessage)


def CarDatabase():

    AllCars = {}
    noCars = 0

    with open('not_rented.txt', 'r') as rf1:
        for line in rf1:
            noCars += 1

    with open('rented.txt', 'r') as rf2:
        for line in rf2:
            noCars += 1

    for carID in range(1, noCars + 1):

        with open(str(carID) + '.txt', 'r') as rf:
            carData = {}
            techSpec = {'power': '', 'consumption': '',
                        'fuel': '', 'transmission': ''}

            for line in rf:
                splitLine = line.strip(' \n').split('=')
                if splitLine[0] in techSpec.keys():
                    techSpec[splitLine[0]] = splitLine[1]
                else:
                    carData[splitLine[0]] = splitLine[1]

            carData['technical'] = techSpec
            AllCars[carID] = carData

    return(AllCars)


# Available func display:
def AvailableCarsFunc(AllCars):

    # List of available cars:
    InCarList = []
    with open('not_rented.txt', 'r') as rf:
        for carID in rf:
            InCarList.append(carID.strip('\n'))

    print('')

    for num, car in enumerate(InCarList):
        print(num + 1, AllCars[int(car)]['brand'] +
              ' ' + AllCars[int(car)]['model'])

    OptionA = '(1)view car detail'
    OptionB = '(2)back to main menu'

    DisplayEndMenu(OptionA, OptionB)

    userI = input('\nChoose your option (1, 2): ')

    PermitedInput = ['1', '2']

    while userI not in PermitedInput:
        print('\nWrong value, please enter only num 1 to 2.')
        userI = input(
            '\nPick up the option by typing it\'s number in the brackets: ')

    userI = int(userI)

    while userI == 1:
        CarDetailView(AllCars, InCarList)
        DisplayEndMenu(OptionA, OptionB)
        userI = input('\nChoose your option (1, 2): ')
        PermitedInput = ['1', '2']

        while userI not in PermitedInput:
            print('\nWrong value, please enter only num 1 to 2.')
            userI = input(
                '\nPick up the option by typing it\'s number in the brackets: ')

        userI = int(userI)
    else:
        # available options
        DisplayMenu()
        CarRentMenu(AllCars)


def CarDetailView(AllCars, InCarList):
    UserICar = input('\tChoose a number of the car: ')

    PermitedInput = range(1, len(InCarList) + 1)
    print(PermitedInput)

    while not UserICar.isdecimal() or (int(UserICar) not in PermitedInput):
        print('\nWrong value, please enter only num of the car.')
        UserICar = input('\tChoose a number of the car: ')

    UserICar = int(UserICar)
    UserICar = int(InCarList[UserICar - 1])
    DisplayCar(AllCars[UserICar])


def SearchCarMenu(AllCars):

    OptionA = '(1)Search cars by parameters'
    OptionB = '(2)Compare cars head to head'

    DisplayEndMenu(OptionA, OptionB)

    UserI = input('\nChoose your option (1, 2): ')

    PermitedInput = ['1', '2']

    while UserI not in PermitedInput:
        print('\nWrong value, please enter only num 1 or 2.')
        UserI = input(
            '\nChoose your option (1, 2): ')

    UserI = int(UserI)

    if UserI == 1:
        SearchCar(AllCars)
    elif UserI == 2:
        HeadToHead(AllCars)


def SearchCar(AllCars):
    # Search car func display

    DisplayCategories(AllCars)

    Technical = ['power', 'consumption', 'fuel', 'transmission']
    LimitCategory = ['model year', 'power', 'consumption', 'price']
    LimitCategoryList = []

    UserISearch = input('\nEnter categories separate by comma to search in: ')

    SearchList = UserISearch.split(',')
    SearchListStriped = []

    for category in SearchList:
        category = category.strip(' ')
        if category in LimitCategory:
            LimitCategoryList.append(category)
        else:
            SearchListStriped.append(category)

    KeyWordList = []
    LimitList = []
    Limits = ['<', '>', '=', '<=', '>=']
    for category in SearchListStriped:
        KeyWord = input('Enter keyword for {}: '.format(category))
        KeyWordList.append(KeyWord)

    for category in LimitCategoryList:
        KeyWord = input('\nChoose limit sign of available limits {} plus enter \
search value of category {} (e.g.: <8): '.format(Limits, category))
        LimitList.append(KeyWord)

    SearchScoreTarget = len(KeyWordList)

    FinalResultPart1 = None
    FinalResultPart2 = None
    FinalCarList = []
    if len(LimitList) == 0:
        FinalResultPart1 = SearchCarStage1(AllCars, SearchListStriped,
                                           LimitList, KeyWordList,
                                           SearchScoreTarget, Technical)
        for car in FinalResultPart1:
            FinalCarList.append(FinalResultPart1[car])
        DisplayCarTable(FinalCarList)

        SearchCarEndMenu(AllCars)

    else:
        FinalResultPart1 = SearchCarStage1(AllCars, SearchListStriped,
                                           LimitList, KeyWordList,
                                           SearchScoreTarget, Technical)
        FinalResultPart2 = SearchCarStage2(
            FinalResultPart1, LimitCategoryList, Technical, LimitList, Limits)

        for car in FinalResultPart2:
            FinalCarList.append(FinalResultPart2[car])

        DisplayCarTable(FinalCarList)

        SearchCarEndMenu(AllCars)


def SearchCarStage1(AllCars, SearchListStriped, LimitList, KeyWordList,
                    SearchScoreTarget, Technical):

    ResultStage1 = {}

    for car in AllCars:
        SearchScore = 0
        i = 0
        for item in SearchListStriped:
            if item in Technical:
                if AllCars[car]['technical'][item] == KeyWordList[i]:
                    SearchScore += 1
                i += 1

            elif AllCars[car][item] == KeyWordList[i]:
                SearchScore += 1
                i += 1

        if SearchScore == SearchScoreTarget:
            ResultStage1[car] = (AllCars[car])

    return ResultStage1


def SearchCarStage2(ResultStage1, LimitCategoryList, Technical,
                    LimitList, Limits):

    FinalResult = {}

    for car in ResultStage1:
        ResultStage2 = None
        CarValue = None
        i = 0
        for item in LimitCategoryList:
            if item in Technical:
                CarValue = int(ResultStage1[car]['technical'][item])
                ResultStage2 = LimitFilter(LimitList[i], CarValue, Limits)
            else:
                CarValue = int(ResultStage1[car][item])
                ResultStage2 = LimitFilter(LimitList[i], CarValue, Limits)
            i += 1

        if ResultStage2:
            FinalResult[car] = ResultStage1[car]

    return FinalResult


# compare 2 cars (head to head)
def HeadToHead(AllCars):

    print('')

    SelectedCars = {}
    for car in AllCars:
        print(str(car) + ':', AllCars[car]
              ['brand'], AllCars[car]['model'])

    UserInput = input('''
\nPick up 2 car to Head to Head comparison.
Type number of car separate by comma (e.g.: 1, 6): ''')

    UserInput = UserInput.split(',')

    print('')

    UserInputInt = []
    for num_car in UserInput:
        num_car = int(num_car.strip(' '))
        UserInputInt.append(num_car)

    SelectedCars[UserInputInt[0]] = AllCars[UserInputInt[0]]

    for key in SelectedCars[UserInputInt[0]]:
        if key != 'technical':
            SelectedCars[UserInputInt[0]][key] = [
                SelectedCars[UserInputInt[0]][key]]

    for key in SelectedCars[UserInputInt[0]]['technical']:
        SelectedCars[UserInputInt[0]]['technical'][key] = [
            SelectedCars[UserInputInt[0]]['technical'][key]]

    for key in AllCars[UserInputInt[1]]:
        if key != 'technical':
            SelectedCars[UserInputInt[0]][key].append(
                AllCars[UserInputInt[1]][key])

    for key in AllCars[UserInputInt[1]]['technical']:
        SelectedCars[UserInputInt[0]]['technical'][key].append(
            AllCars[UserInputInt[1]]['technical'][key])

    HtH_display(SelectedCars)

    # Reset AllCars var changes made by Head to Head func
    AllCars = CarDatabase()

    SearchCarEndMenu(AllCars)


def SearchCategories(AllCars):
    print('')
    for category in AllCars[1].keys():
        if category == 'technical':
            for subcategory in AllCars[1]['technical']:
                print(subcategory)
        else:
            print(category)


def LimitFilter(SetVal, CarVal, SignList):
    Result = None

    if SetVal[1] != '=':
        SetVal1 = int(SetVal[1:])

        if SetVal[0] == SignList[0]:
            Result = SetVal1 > CarVal

        elif SetVal[0] == SignList[1]:
            Result = SetVal1 < CarVal
        elif SetVal[0] == SignList[2]:
            Result = SetVal1 == CarVal
    else:
        SetVal2 = int(SetVal[2:])
        if SetVal[:2] == SignList[3]:
            Result = SetVal2 >= CarVal
        elif SetVal[:2] == SignList[4]:
            Result = SetVal2 <= CarVal

    return Result


def SearchCarEndMenu(AllCars):

    OptionA = '(1)back to search menu'
    OptionB = '(2)back to main menu'

    DisplayEndMenu(OptionA, OptionB)

    UserI = input('\nChoose your option (1, 2): ')

    PermitedInput = ['1', '2']

    while UserI not in PermitedInput:
        print('\nWrong value, please enter only num 1 or 2.')
        UserI = input(
            '\nChoose your option (1, 2): ')

    UserI = int(UserI)

    if UserI == 1:
        SearchCarMenu(AllCars)
    elif UserI == 2:
        DisplayMenu()
        CarRentMenu(AllCars)


# rent a car func

def RentCarFunc(AllCars):

    # List of available cars:
    InCarList = []
    with open('not_rented.txt', 'r') as rf:
        for carID in rf:
            InCarList.append(carID.strip('\n'))

    print('')

    for num, car in enumerate(InCarList):
        print(num + 1, AllCars[int(car)]['brand'] +
              ' ' + AllCars[int(car)]['model'])

    userI = int(input('\nType a number of car which you would like to rent: '))

    UserICar = InCarList[userI - 1]

    Confirmation = (
        '\nThank you. Your {} {} is ready to go. \
Enjoy your journey :)'.format(AllCars[int(UserICar)]['brand'],
                              AllCars[int(UserICar)]['model']))

    print(Confirmation)

    # add car to rented-list
    with open('rented.txt', 'a') as wf:
        wf.write(str(UserICar))
        wf.write('\n')

    InCarList.remove(UserICar)

    with open('not_rented.txt', 'w') as wf:
        for line in InCarList:
            wf.write(line)
            wf.write('\n')

    RentCarEndMenu(AllCars)


def RentCarEndMenu(AllCars):

    OptionA = '(1)back to main menu'
    OptionB = '(2)exit program'

    DisplayEndMenu(OptionA, OptionB)

    UserI = int(input('\nChoose your option (1, 2): '))

    PermitedInput = [1, 2]

    while UserI not in PermitedInput:
        print('\nWrong value, please enter only num 1 or 2.')
        UserI = int(input(
            '\nChoose your option (1, 2): '))

    if UserI == 1:
        DisplayMenu()
        CarRentMenu(AllCars)
    elif UserI == 2:
        print('\nThank you, have a nice day\n')

# Display functions:


def DisplayStartMenu():

    ProgGreeting = ' Welcome to Radek\'s car rent '

    Option1 = '(1)available cars'
    Option2 = '(2)search cars'
    Option3 = '(3)rent a car'
    Option4 = '(4)exit the program'

    ProgMenu1 = (
        '| {} | {} | {} | {} |'.format(Option1, Option2, Option3, Option4)
    )

    LenProgMenu1 = len(ProgMenu1)
    MenuLines = '|' + (LenProgMenu1 - 2) * '*' + '|'
    MenuSides = '|' + (LenProgMenu1 - 2) * ' ' + '|'
    MenuTitle = '|{:*^{}}|'.format(ProgGreeting, LenProgMenu1 - 2)

    return ProgMenu1, LenProgMenu1, MenuLines, MenuSides, MenuTitle


def DisplayMenu():

    (ProgMenu1, LenProgMenu1, MenuLines,
        MenuSides, MenuTitle) = DisplayStartMenu()

    print('')
    print(MenuLines)
    print(MenuSides)
    print(ProgMenu1)
    print(MenuSides)
    print(MenuLines)


def DisplayEndMenu(OptionA, OptionB):

    ProgMenu2 = '| {} | {} |'.format(OptionA, OptionB)

    LenProgMenu2 = len(ProgMenu2)

    MenuLines = '|' + (LenProgMenu2 - 2) * '~' + '|'
    MenuSides = '|' + (LenProgMenu2 - 2) * ' ' + '|'

    print('')
    print(MenuLines)
    print(MenuSides)
    print(ProgMenu2)
    print(MenuSides)
    print(MenuLines)


def GoodByeMessage(ByeMessage):

    ProgMenu3 = '| {} |'.format(ByeMessage)

    LenProgMenu3 = len(ProgMenu3)

    MenuLines = '|' + (LenProgMenu3 - 2) * '+' + '|'
    MenuSides = '|' + (LenProgMenu3 - 2) * ' ' + '|'

    print('')
    print(MenuLines)
    print(MenuSides)
    print(ProgMenu3)
    print(MenuSides)
    print(MenuLines)


def DisplayCar(car):

    headerTemplate = '|{0:~^{1}}|'
    rowTemplate = '|{0:-<{1}}----> {2:<{3}}|'

    carAdjust = {}

    for key in car.keys():
        if key == 'technical':
            carAdjust['technical '] = {}
            for key in car['technical'].keys():
                key2 = '{} '.format(key)
                carAdjust['technical '][key2] = car['technical'][key]

        else:
            key2 = '{} '.format(key)
            carAdjust[key2] = car[key]

    colWidth = []
    colWidth2 = []
    for key in carAdjust:
        if key == 'technical ':
            for key in carAdjust['technical '].keys():
                colWidth.append(len(key))
                colWidth2.append(len(carAdjust['technical '][key]))
        else:
            colWidth.append(len(key))
            colWidth2.append(len(carAdjust[key]))

    headerChart = headerTemplate.format(
        ' CAR-INFO ', max(colWidth) + max(colWidth2) + 6)

    print('')
    print(headerChart)

    for key in carAdjust:
        if key == 'technical ':
            for key in carAdjust['technical '].keys():
                lineX = rowTemplate.format(
                    key, max(colWidth), carAdjust['technical '][key],
                    max(colWidth2))
                print(lineX)

        else:
            lineX = rowTemplate.format(
                key, max(colWidth), carAdjust[key], max(colWidth2))
            print(lineX)

    endLine = '|' + '=' * (max(colWidth) + max(colWidth2) + 6) + '|'
    print(endLine)


def DisplayCategories(carInput):

    headerTemplate = '|{0:~^{1}}|'
    rowTemplate = '|--- {0:-<{1}}--|'

    car = carInput[1]
    carAdjust = {}

    for key in car.keys():
        if key == 'technical':
            carAdjust['technical '] = {}
            for key in car['technical'].keys():
                key2 = '{} '.format(key)
                carAdjust['technical '][key2] = car['technical'][key]

        else:
            key2 = '{} '.format(key)
            carAdjust[key2] = car[key]

    colWidth = []
    for key in carAdjust:
        if key == 'technical ':
            for key in carAdjust['technical '].keys():
                colWidth.append(len(key))

        else:
            colWidth.append(len(key))

    headerChart = headerTemplate.format(
        ' CATEGORIES ', max(colWidth) + 6)

    print('')
    print(headerChart)

    for key in carAdjust:
        if key == 'technical ':
            for key in carAdjust['technical '].keys():
                lineX = rowTemplate.format(
                    key, max(colWidth))
                print(lineX)

        else:
            lineX = rowTemplate.format(
                key, max(colWidth))
            print(lineX)

    endLine = '|' + '=' * (max(colWidth) + 6) + '|'
    print(endLine)


def DisplayCarTable(data):

    titleTemplate = '|{0:~^{1}}|'
    headerTemplate = '| {:^{W1}} | {:^{W2}} | {:^{W3}} | {:^{W4}} | {:^{W5}} |\
     {:^{W6}} | {:^{W7}} | {:^{W8}} | {:^{W9}} |'
    bodyTemplate = '| {:^{W1}} | {:^{W2}} | {:^{W3}} | {:^{W4}} | {:^{W5}} |\
     {:^{W6}} | {:^{W7}} | {:^{W8}} | {:^{W9}} |'

    Header = []
    Lines = []
    ColWidths = {}

    for key in data[0].keys():
        if key == 'technical':
            for key in data[0]['technical'].keys():
                Header.append(key)

        else:
            Header.append(key)

    NumOfCol = 1
    for col in Header:
        ColWidths['W' + str(NumOfCol)] = len(col)
        NumOfCol += 1

    for car in data:
        lineX = []
        for key in car:
            if key == 'technical':
                for key in car['technical'].keys():
                    lineX.append(car['technical'][key])

            else:
                lineX.append(car[key])
        Lines.append(lineX)

    for line in Lines:
        n = 1
        for col in line:
            if len(str(col)) > ColWidths['W' + str(n)]:
                ColWidths['W' + str(n)] = len(str(col))
            n += 1

    line1 = headerTemplate.format(*Header, **ColWidths)

    line0 = titleTemplate.format(
        ' SEARCH RESULTS ', len(line1) - 2)

    blankline = '|' + ' ' * (len(line1) - 2) + '|'

    boarder = '|' + '-' * (len(line1) - 2) + '|'
    boarder2 = '|' + '=' * (len(line1) - 2) + '|'

    print('')
    print(line0)
    print(blankline)
    print(boarder)
    print(line1)
    print(boarder2)
    for line in Lines:
        line = bodyTemplate.format(*line, **ColWidths)
        print(line)
        print(boarder)


def HtH_display(data):

    table_sample = '{:^{}} \n|{:^{}} <-----> {:^{}}|'
    border_sample = '{:-^{}}'

    leftwidth = 0
    rightwidth = 0

    tabledata = {}
    for car in data:
        tabledata = data[car]

    tabledataDict = {}

    for key in tabledata:
        if key == 'technical':
            for key in tabledata['technical']:
                tabledataDict[key] = tabledata['technical'][key]
        else:
            tabledataDict[key] = tabledata[key]

    tabledataList = []

    for key in tabledata:
        if key == 'technical':
            for key in tabledata['technical']:
                tabledataList.append(tabledata['technical'][key])
        else:
            tabledataList.append(tabledata[key])

    for item in tabledataList:
        if len(item[0]) > leftwidth:
            leftwidth = len(item[0])
        if len(item[1]) > rightwidth:
            rightwidth = len(item[1])

    if leftwidth > rightwidth:
        rightwidth = leftwidth
    else:
        leftwidth = rightwidth

    totalwidth = leftwidth + rightwidth + len('| <-----> |')

    print('')
    for item in tabledataDict:
        formatvalue = (
            item,
            totalwidth,
            tabledataDict[item][0],
            leftwidth,
            tabledataDict[item][1],
            rightwidth)
        print(table_sample.format(*formatvalue))
        print(border_sample.format('', totalwidth))


CoreFunc()
