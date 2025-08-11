# kmk_keeb_pico
A Handwired keyboard with Raspberry Pi Pico and KMK Firmware.

This repo is made to note my progress as I go on and to guide others that want to handwire their keyboards.

# **THE SCHEMATIC:**

Here's the wiring you should be going for:


<img width="1010" height="758" alt="wiring" src="https://github.com/user-attachments/assets/a79d5dad-cdfc-4ac3-9a79-758d745a60ff" />
(4x4 matrix example)


In the example picture there are 4 columns and 4 rows so 16 switches and diodes. The diodes are neccerary to keep the current flowing in the wrong direction so that the pi pico can actually understand what key you are pressing. 

The rows and columns can be connected to the GP pins on the microcontroller.(Pins between GP20-GP28 might cause some problems since they are ADC and might be input only but I haven't tried it. So be wary.) Also try to connect consequent rows and columns to consequent pins so it doesn't get mixed up while coding. 

In the example image rows 1-4 are connected to GP0, GP2, GP4, GP6 respectively. Columns 1-4 are connected to GP1, GP3, GP5, GP7. You could also change the direction of the diodes since we specify the direction in the code anyways.


# **PARTS:**

## The Switches: You can use pretty much any switch you want. For my keyboard I used Holy Panda MMD V2s. Just make sure when you print the board it fits the switches. If you don't know what to buy get cherry or gateron switches.

## Cables: Use copper cables that are easy to use with solder. Thicker cables might help keeping stuff organized.

## Diodes: 1N4148s will do fine. They are pretty cheap. Get one for each switch and some extras as they might get burnt.

## Keycaps: You can buy keycap sets from amazon or aliexpress. If you are going to add leds to your build make sure you get transparent ones.(rgb or leds won't be mentioned in this guide)

## Stabilizers: You need these for your longer keys ie. spacebar shift etc. Decide what type of stabilizer you're going to buy before designing the plate so that they fit.

## Soldering Equipment: You don't really need much, A soldering iron, some soler(leaded prefferably), flux(optional but helps a lot), and a holder for the iron is all you need.

## The Case: 3D printing the case is your best bet. You could also get a metal or a wooden case but it might get too expensive.

## The plate: This is where things get a little more complicated. First go to https://www.keyboard-layout-editor.com. The website is pretty intuitive. You don't need to label the keys as this is only for the layout. Build the layout you want and it should give you a .svg file. Once you have the file go to builder.swillkb.com. Choose raw file. 
Switch Type: MX 

Stabilizer Type : “Cherry + Costar” 

Case Type: “Sandwich” 

Mount Holes: 8 (unless you want more/less), 2.1mm diameter

Width Padding: 6 mm (Sets the border of the keyboard, 6 mm is a safe bet but you could go more if you want)

Height Padding: 6 mm

Plate Corners: 2 mm (Rounds the corners)

Kerf: 0.15mm

After you enter these settings you click CAD output and choose .svg file. You should be able to upload this to a metal cutting service and have it delivered. I would recommend aluminum as it durable and lightweight.



https://matt3o.com/hand-wiring-a-custom-keyboard/

https://deskthority.net/viewtopic.php?f=7&t=6050

https://geekhack.org/index.php?topic=87689.0

https://www.reddit.com/r/MechanicalKeyboards/comments/8aw5j2/invisible_hardline_keyboard_progress_update_april/

https://www.reddit.com/r/MechanicalKeyboards/comments/4l0p41/guide_detailed_guide_to_making_a_custom_keyboard/
