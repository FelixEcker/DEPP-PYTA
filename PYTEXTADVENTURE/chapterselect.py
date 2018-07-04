from bin import episodes_bin


def selection_input(txt):
    return input(txt)


def Select():
    choice = selection_input("Which chapter would you like to play? :")

    if choice in episodes_bin.episodes:
        episodes_bin.episodes(choice).play()
    else:
        print ("This episode doesn't exist! :(")
