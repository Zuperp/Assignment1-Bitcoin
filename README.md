# Assignment1-Bitcoin

It contains the Config file which changes the mode to regtest, this means that you're not interacting with other nodes than on your local machiene, not even test nodes.

There is a stop and start script to run the server. And the main python app.

To run the assignment sucesfully do this in order: 

* Copy the bitcoin.conf file into your bitcoin folder in the %appdata% folder
* Run the StartScript to start the bitcoin server
* Run the main python application which laynches the GUI
* Type the name you want for your main wallet
* Click the button "Setup wallet with coins"
* Write the name you want for the wallet you want to send to
* Click the button "Generate wallet to send to with name:"
* The address of the second wallet you created will be displayed below, copy that manually.
* Place the copied address in the "Copy your target address here" text field
* Write the number of bitcoins you wish to send
* Click the send button
* Click the "Show balance and list unspent" button, this will update the balance, and show the string you recieve from the "listunspent" cli command
* Run the StopScript to shut down the bitcoin server

----------

Things to avoid:
* Empty or invalid inputs in the fields that require specific text from you
* Doing everything in a random order, it may break due to some issues not yet solved.

----------


The gui contains, in order:

A setup button that sets up the first wallet, based on the string you've typed. And the field which you're supposed to type it in.

A button to generate the wallet you're supposed to send to and the field for the name for the wallet.

A field where the generated address is, use this to paste into the target address field.

The field you copy the address into.

A field that takes the amount you want to send from the main wallet, to the second generated wallet. And a send button.

The balance that's on the main wallet, and the info from running the listunspent command, which only shows up if you click the button below, which updates balance and displays the list unspent string.
