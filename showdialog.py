class ShowDialog():
    def returndialog(dial):
        file = open("dialogs/" + dial, "r")
        text = file.readlines()
        dialog = []

        for line in text:
            dialog.append(line[:-1])
        
        return dialog