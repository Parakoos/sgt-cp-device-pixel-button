Code to run a simple remote for the the Shared Game Timer, having a single button, one 'logical' NeoPixel
and possibly some kind of alert 'thing' like a vibrator.

What is The Shared Game Timer?  It is a board game timer that runs in the browser. See https://sharedgametimer.com for more info.

It has a Bluetooth API that allow for electronic devices to act as remotes, letting players interact
with the timer through physical devices. This is one such device.

## Installation

You need a microcontroller set up to run CircuitPython. See https://circuitpython.org/ for help with that.

Before running the following commands, please safe-copy the files on your microcontroller and remove all old code.

Then run the following git command from the root of your microcontroller (I assume you have git installed) where you would normally have your `code.py` file.

`git clone --separate-git-dir "C:\Path\To\Somewhere\On\Your\Computer\Where\You\Want\The\Git\Dir" --recurse-submodules https://github.com/Parakoos/sgt-cp-device-jewel .`

That will download this repos working tree files directly to you microcontroller. It will also set up a git directory to hold the git files somewhere on your computer. It is a good idea to keep these things separate since your microcontroller may be short on space.

## Change Settings

You will need to define a few settings for things to work. Copy the `/src/pixel_button/pixel_button_settings.example.py` to `/src/pixel_button/pixel_button_settings.py` and edit the file to fit your board. This file is specific for your board and is therefore listed as ignored by git. So, if you decide to fork this repo and submit a pull request, your private settings won't be included.