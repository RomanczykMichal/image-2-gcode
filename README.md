# image-2-gcode
This script is responsible for translation of JPG file into gcode file. This project is inspired by work of @pavlovpulus.

Enter this command to run script:
```
python3 ./main.py [arguments list]
```

Below you fill find list of available arguments:
```
options:
  -h, --help                    show this help message and exit
  -f, --file         FILE       JPG file which you want to convert to gcode.
  -s, --save         SAVE       directory to save gcode file. Default is current directory.
  -d, --dimensions   DIMENSIONS dimensions of plot ('width;height' [mm]).
```

I'm owner of Ender3 Pro 3d printer which I will use in this project. This required some modifications of extruder part.
I have prepared 2 STL files which you can find under **stl files** directory. This is handle for a pen (I have used [this one](https://www.amazon.com/STAEDTLER-LUMOCOLOR-PERM-BLACK-317-9/dp/B00211XD0A/ref=sr_1_41?crid=2PESK4SWYF090&keywords=staedtler+lumocolor&qid=1686762641&sprefix=staedtler+lumocolo%2Caps%2C190&sr=8-41)).
Assembly of elements is realy simple. Bolts used to screw things up are the same as in original 3d printer extruder.

<img src="https://github.com/RomanczykMichal/image-2-gcode/assets/80456075/60a76202-350d-48ea-bb02-4d6cc934bf1b" data-canonical-src="https://github.com/RomanczykMichal/image-2-gcode/assets/80456075/60a76202-350d-48ea-bb02-4d6cc934bf1b" width="350" height="540" />
