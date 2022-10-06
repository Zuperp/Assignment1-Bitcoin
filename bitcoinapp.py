import PySimpleGUI as sg
import os


#       It's handled with python "os" which lets you execute cli commands from the code and the PySimpleGUI lib

#      ----     GUI definition    ----         #

#       Moves us to the directory which the Bitcoin server is supposed to already be running
dir = "C:\Program Files\Bitcoin\daemon"
os.chdir(dir)

#       Changes the theme
sg.theme("DarkBlue3")

#       The layout is difined below here, with buttons and text. These are used to display the elements on the screen.

layout = [
        [sg.Button("Setup wallet with coins"), sg.Text("Write your wallet name here"), sg.Input(key="-walletname-") ],
        [sg.Button("Generate a wallet to send to with the name: "), sg.Input(key="-GetWalletName-") ],
        [sg.Text("Your generated address"), sg.Multiline(disabled=True, key="-target-")],
        
        [sg.Text("Copy your target address in here:"), sg.Input(key="-typeTargetHere-") ],
        [sg.Text("Amount you wish to send"), sg.Input(key="-SendAmount-"), sg.Button("Send")],
        
        [sg.Text("Balance remaining" ,key="-outputbox-"),  ],
        [sg.Button("Show remaning balance and list unspent"), sg.Text("", key="-listunspent-")  ],
]

#       What's in the title of the window
window = sg.Window("Bitcoin app for blockchain assignment 1", layout)


#        ----           Loop for handling events      ----          #

while True:
    event, values = window.read()

    #       Handler for the button that creates the main wallet you're sending from. It creates, loads, generates an address, 
    #       and gives it 101 blocks which gives it 50 BTC because it's in the first 150 blocks, and finally updates 
    #       the balance so you can see you recieved 50 BTC

    if event == "Setup wallet with coins":
        walletvari = values["-walletname-"]
        os.system("bitcoin-cli createwallet {} ".format(walletvari))
        print("created wallet")
        os.system("bitcoin-cli loadwallet {} ".format(walletvari))
        print("Loaded wallet")
        main_wallet = os.popen("bitcoin-cli getnewaddress").read()
        print("Main wallet string: " + str(main_wallet))
        os.system("bitcoin-cli generatetoaddress 101 {}".format(main_wallet))
        print("Generated to main wallet")
        balanceInput = os.popen("bitcoin-cli getbalance").read()
        window["-outputbox-"].update("Balance left is: " + balanceInput)

    #       Exit button
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    #       Updates the balance and list unspent via the "listunspent" command

    if event == "Show remaning balance and list unspent":
        input_text = os.popen("bitcoin-cli getbalance").read()
        window["-outputbox-"].update("Balance left is: " + input_text)
        listunspent = os.popen("bitcoin-cli listunspent 0").read()
        window["-listunspent-"].update(listunspent)

    #       The send button, which sends the amount you typed in to the address you typed

    if event == "Send":
        os.system("bitcoin-cli unloadwallet {}".format(nameForWalletGen))
        os.system("bitcoin-cli loadwallet {} ".format(walletvari))
        sendingAmount = values["-SendAmount-"]
        targetToSendTo = values["-typeTargetHere-"]
        os.system("bitcoin-cli sendtoaddress {} {}".format(targetToSendTo, sendingAmount)) 
    
    #       Generates the wallet you want to send BTC to.

    if event == "Generate a wallet to send to with the name: ":
        walletvari = values["-walletname-"]
        os.system("bitcoin-cli unloadwallet {}".format(walletvari))
        nameForWalletGen = values["-GetWalletName-"]
        os.system("bitcoin-cli createwallet {} ".format(nameForWalletGen))
        os.system("bitcoin-cli loadwallet {} ".format(nameForWalletGen))
        wallet_to_send_to = os.popen("bitcoin-cli getnewaddress").read()
        window["-target-"].update(wallet_to_send_to)
        print(wallet_to_send_to)


window.close()
