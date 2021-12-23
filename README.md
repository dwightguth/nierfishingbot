# Nier: Automata Fishing Bot

For installation instructions, see INSTALL.md.

## To use:

1. Open Nier: Automata and navigate to a body of water you want to fish in. If possible, stand in the water.
2. Disable music and voice volume in your settings for the game
3. Kill any other open applications that might make sounds.
4. Begin fishing by holding down the E key.
4. Alt tab to your command prompt and run `py nierfishingbot.py`
5. Sit back and let it fish until it's caught the fish you want.
6. Alt tab back to the command prompt and press ctrl-c to kill the bot.

## Tested Fishing Locations

The following fishing locations have been tested and the bot ought to be able to catch fish at them if it has been calibrated correctly:

* City Ruins - Streams/Waterfalls (tested in pond by Resistance Camp)
* Desert Zone - Oil Field
* Desert Zone - Oasis

Other locations may or may not work correctly.

## Troubleshooting

If the bot is failing to catch fish, this can be due to a couple of different reasons. First, you might be fishing in a body of water that isn't well supported yet. For example, the amusement park has loud fireworks in the background that interfere with the very simplistic audio processing the script currently does to detect a fish on the line. I have tested it with the desert oasis and the pond by the resistance camp, but other locations may or may not work in the current version.

Second, the script might be poorly calibrated for your current audio setup. I have found that different audio settings can cause different values for the THRESHOLD variable to be required, and the exact value needed by your machine is probably different from mine. Eventually it would be nice for the script to be able to be automatically calibrated, but that hasn't happened yet. So you will probably need to manually modify the script to set an appropriate value. You can do this by running the script until the pod dips below the surface and plays the sound that indicates a fish is on the line, and then alt-tabbing, killing the script, and looking for a series of numbers printed to the terminal that are somewhat higher than those around them, and adjusting the threshold so it is lower than those values, but higher than the lower ones.

Third, stereo mix might not be working correctly. As far as I can tell, Realtek Stereo Mix works by means of recording the audio sent to the back-facing speaker jack on your computer, so if you have headphones plugged into the front-facing port, it will not actually be recording any sound. The only tractable solution I have found to that problem is simply to unplug your speakers and plug your headphones into the back-facing speaker jack directly.
