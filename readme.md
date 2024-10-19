# J2ME reversing github repo

## Tools
1. [QuiltMC Enigma Swing](https://maven.quiltmc.org/repository/release/org/quiltmc/enigma-swing/) ([Github Repo](https://github.com/QuiltMC/enigma)) - Used for demangling the .jar names
2. [KEmulator nnmod](https://nnp.nnchan.ru/kem/) ([Github](https://github.com/shinovon/KEmulator)) - Used for emulating the games
<!--May be worth looking into: https://github.com/Storyyeller/Krakatau & https://dirty-joe.com/-->

## File structure
OriginalDumps/ - You can put any dumps of J2ME games you have here and they will not be published to github when you make changes.
Games/$game_name/$version_name/ - Games are stored under $game_name and $version name.
    src/ - A plce to temporarily store the exported decompilation, not published to github.
    contents/ - A place to store the extracted contents of the .jar, not published to github.
    mappings.mappings - A file which contains the mappings which you can import into Enigma.

## Style guidelines.
* Classes - PascalCase
* Methods - camelCase
* Variables - snake_case
* Constants - UPPER_SNAKE_CASE