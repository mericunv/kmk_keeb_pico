# kmk_keeb_pico
A Handwired keyboard with Raspberry Pi Pico and KMK Firmware.

This repo is made to note my progress as I go on and to guide others that want to handwire their keyboards.

**THE SCHEMATIC:**

Here's the wiring you should be going for:


<img width="1010" height="758" alt="wiring" src="https://github.com/user-attachments/assets/a79d5dad-cdfc-4ac3-9a79-758d745a60ff" />
(4x4 matrix example)


In the example picture there are 4 columns and 4 rows so 16 switches and diodes. The diodes are neccerary to keep the current flowing in the wrong direction so that the pi pico can actually understand what key you are pressing. 

The rows and columns can be connected to the GP pins on the microcontroller.(Pins between GP20-GP28 might cause some problems since they are ADC and might be input only but I haven't tried it. So be wary.) Also try to connect consequent rows and columns to consequent pins so it doesn't get mixed up while coding. 

In the example image rows 1-4 are connected to GP0, GP2, GP4, GP6 respectively. Columns 1-4 are connected to GP1, GP3, GP5, GP7. You could also change the direction of the diodes since we specify the direction in the code anyways.


**PARTS:**

The Switches: You can use pretty much any switch you want. For my keyboard I used Holy Panda MMD V2s. Just make sure when you print the board it fits the switches.

Cables: Use copper cables that are easy to use with solder. Thicker cables might help keeping stuff organized.

Diodes: 1N4148 will do fine. They are pretty cheap. Get one for each switch and some extras as they might get burnt.



https://matt3o.com/hand-wiring-a-custom-keyboard/

https://deskthority.net/viewtopic.php?f=7&t=6050

https://geekhack.org/index.php?topic=87689.0

https://www.reddit.com/r/MechanicalKeyboards/comments/8aw5j2/invisible_hardline_keyboard_progress_update_april/

https://www.reddit.com/r/MechanicalKeyboards/comments/4l0p41/guide_detailed_guide_to_making_a_custom_keyboard/
