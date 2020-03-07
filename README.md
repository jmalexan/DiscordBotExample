# Setup

1) Bot registration

Go to [Discord's Developer page](https://discordapp.com/developers) and create a new application, and give it the name that you want your bot to have.  Once that's created, go to the "Bot" tab and make sure that a bot is created as well.  Take note of the "Token" field on the page, and the long string of letters and numbers that you can reveal.  You'll need this later.

2) Add bot to your server

On the "OAuth2" tab on your bot page, at the bottom of the page, there should be an array of checkmarks.  Check the "bot" option.  When you do that, another separate array of checkmarks will appear below the first one.  Check the "Administrator" option.  Go back up to the first checkboxes, and click the "Copy" button next to the URL.  Paste that into your address bar, login to your Discord account, and choose a Discord server that you want to add your bot too.  WARNING: by giving your bot the Administrator permission, it has the ability to delete your server.  I highly recommend adding your bot to a test server before a more established server, in case there's a bug with catastrophic consequences.

3) Install Discord.py

In your terminal (Terminal on MacOS and Linux, Command Prompt or cmd on Windows) enter the command `python3 -m pip install -U discord.py`.  If this command doesn't function, you can also try `py -3 -m pip install -U discord.py`.  This should show a message about installing the discord.py library.

4) Create a tokenfile

The Bot token that I mentioned earlier is like a password for your bot.  If someone has it, they can just login as your bot and make it do things.  This is especially bad, given that we've given the bot the Administrator permission.  You should take steps to make sure no one can get it, including that you don't accidentally put the token on GitHub (if you're using it).  This project loads the token from a file called "tokenfile.txt", but for obvious reasons I've removed it from this repository.  In order for this example program to function, you need to create a file called "tokenfile.txt" and paste your Bot's Token into it, and save it.

5) Run the file

With all of this setup, it *should* just work.  Try running the script with the command `python3 main.py` or `py main.py`.  To see which commands the bot has by default, just take a look at the source code! ;)