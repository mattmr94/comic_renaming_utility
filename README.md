# comic_renaming_utility
This script takes json output from the Grand Comics Database and uses it to update CBZ comic file names to a consistent format.

## Requirements:

- Comic files in either CBZ or CBR format with correct issue numbers.
- Grand Comics Database JSON output

## Finding comic data

Navigate to https://www.comics.org/ and search for the run you're looking for. For example, we'll look at Nova v4 (2007-2010). The most consistent way I've found is to search the run name + publication year and that usually does the trick. So searching "Nova 2007" puts it as the second result.

Once you'd found the run, go to the Cover and Main Story Overview page. In this case, it is https://www.comics.org/series/23407/overview/. From there, scroll to the bottom and download the data as a .json. You do not need to modify the JSON to run the script, except maybe modifying the title to match what the script is looking for (table.json) and moving it into the same folder as the script.

## Running the script

From there, simply run the script. It will ask you some questions, answer those, and then it will begin renaming your files. The only requirement for the original file name is that they have a matching issue number to the new name, that way it will rename the correct file. Based on our Nova example, your output will be:

*Nova.v4.012.Inheritance.(2008).cbz*
*Nova.v4.013.On.the.Last.Day.(2008).cbz*
*Nova.v4.014.In.the.Final.Hour.(2008).cbz*

And so on. If there is not a title for the individual issue, then it would appear as:

*Nova.v4.012.(2008)*

And for runs that don't have multiple volumes, using Webspinners: Tales of Spider-Man as an example:

*Webspinners.Tales.of.Spider-Man.001.As.Dreams.Are.Made.On.Part.One.Crash.and.Burn.(1999)*

## Conclusion

This is my first project I've done outside of work, and I've only been using Python and coding in general for about 2 months. I appreciate any feedback or suggestions!
