there may be an issue with the windows api used by your git when dealing with file names of a certain length, use: 
git config --system core.longpaths true
to combat this