# Comic Renaming Utility
This script takes json output from the Grand Comics Database and uses it to update CBZ comic file names to a consistent format.

## TODO List
- [] Add a script to automatically handle various non-CBZ or CBR collections of comics before renaming.
  - For example, if everything is just JPGs or PNGs in a folder, it needs to be Zipped and then changed to CBZ/CBR. Or if it's a PDF, some sort of conversion would need to happen.
- [] Create script to automatically pull GCB JSON files.
  - Not sure yet how I'd implement this. It would require some work since they don't appear to have an API, and I'm not sure yet what details it would need to accurately find the run wanted.
- [] Offer the user different options in terms of formatting the file name. For example, allowing them to use underscores or, God forbid, spaces.
