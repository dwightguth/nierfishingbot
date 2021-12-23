# Nier: Automata Fishing Bot

For installation instructions, see INSTALL.md.

## To calibrate:

1. Open Nier: Automata and navigate to the pond outside the resistance camp. Stand in the water.
2. Disable music and voice volume in your settings for the game
3. Kill any other open applications that might make sounds.
4. Begin fishing by holding down the E key.
5. Alt tab to your command prompt and run `py nierfishingbot.py --threshold 1.0 --debug`
6. Wait until the script alt-tabs back.
7. If a fish was on the line at some point during step 6, proceed to step 8, otherwise return to step 5.
8. Look at the values printed on the command line, which represent the volume of sound for the 20 second period it was recording. Try to pick a calibrated value that is greater than the volume at any point during background noise, but less than the volume of the sound of the pod submerging underwater.

## To use:

1. Open Nier: Automata and navigate to a body of water you want to fish in. If possible, stand in the water.
2. Disable music and voice volume in your settings for the game
3. Kill any other open applications that might make sounds.
4. Begin fishing by holding down the E key.
5. Alt tab to your command prompt and run `py nierfishingbot.py --threshold <calibrated value>`
6. Sit back and let it fish until it's caught the fish you want.
7. Alt tab back to the command prompt and press ctrl-c to kill the bot.

## Tested Fishing Locations

The following fishing locations have been tested and the bot ought to be able to catch fish at them if it has been calibrated correctly:

* City Ruins - Streams/Waterfalls (tested in pond by Resistance Camp)
* Desert Zone - Oil Field
* Desert Zone - Oasis

Other locations may or may not work correctly.

## Troubleshooting

If the bot is failing to catch fish, this can be due to a couple of different reasons. First, you might be fishing in a body of water that isn't well supported yet. For example, the amusement park has loud fireworks in the background that interfere with the very simplistic audio processing the script currently does to detect a fish on the line. I have tested it with the desert oasis and the pond by the resistance camp, but other locations may or may not work in the current version.

Third, stereo mix might not be working correctly. As far as I can tell, Realtek Stereo Mix works by means of recording the audio sent to the back-facing speaker jack on your computer, so if you have headphones plugged into the front-facing port, it will not actually be recording any sound. The only tractable solution I have found to that problem is simply to unplug your speakers and plug your headphones into the back-facing speaker jack directly.
