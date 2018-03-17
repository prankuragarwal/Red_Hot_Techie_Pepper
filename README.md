

                                                   WELCOME TO  
                              An Intelligent Bot built with Zulip and Python
                              
INTRODUCTION

This Bot deals with with various features required by a personal relocation assistant that brings superior service and unpralleled delight to the user.
While you relocate,I(BOT) give you advice on where to go,which direction to take,what to do etc.

FEATURES

1.Currency Convertor
2.Near by ATM's locator
3.Language Translator
4.Nearby Restaurants locator
5.Gides you direction to different places
6.Gives nearest transportation service
7.Tells latitude and longitude of particular place
8.Helps you in finding your desired job
9.Tourist Spots
10.NLP Based instatnt response
11.AutoCorrects the queries and replies accordingly

DEPLOY

To deploy Jarvis bot using your local machine as server, follow following steps -

 1.Firstly create a zulip organisation on which you want to deploy bot. If you already have one then you may skip this step.
 2.Register a new bot user on the Zulip server's web interface.
 3.Log in to the Zulip server.
 4.Navigate to Settings -> Your bots -> Add a new bot. Select Generic bot for bot type, set both bot-name and bot username to Jarvis and click on Create bot.
 5.A new bot user should appear in the Active bots panel.
 6.Download the bot's zuliprc configuration file to your computer.
 7. Go to Settings -> Your bots
    In the Active bots panel, click on the little green download icon to download its configuration file zuliprc (the structure of this file is explained here).
 8.Make sure sure that your system has following packages installed -
    enchant (Please make sure your enchant version is <= 1.6.1-2)
    sshpass (For debian based system install using sudo apt-get install sshpass)
    aspell-en (For debian based system install using sudo apt-get install aspell-en)
 9.Install all required python packages, rum command pip3 install -r requirements.txt
 10.Now we are all set, to run bot enter following command zulip-run-bot <absolute path to jarvisBot.py file > --config-file <absolute path to downloaded zuliprc file>
 Example Usage - zulip-run-bot ~/Projects/TestBot/bot/TestsBot --config-file ~/Projects/TestsBot/bot/zuliprc
 

FEEDBACK

Feel free to message on the below mentioned email ids.COnstructive critism is welcome.

CONTRIBUTORS

Gunjan Singh         singh.gunjan72@gmail.com
Naguboyina Sravya    sravya.munnny@gmail.com
Prankur Agarwal      prankur.agarwal@gmail.com
Vrinda Agarwal       avrinda97@gmail.com

CONTRIBUTE

Feel free to report issues and bugs.It will be helpful for future launches of application.
All Suggestions are welcome.
Fork repository and Contribute.

ACKNOWLEDGEMENTS
Thanks to Zulip for providing Zulip Api and Platform.
