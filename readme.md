Summary
=======

Uses the commandline/python-module javascript formatter from http://jsbeautifier.org/ to format the selected text, or the entire file if there is no selection. 

Attention: the plugin does not check to make sure the buffer has a `.js` file type, it just javascript formats the selection/file. Thus, use with caution if you are in an HTML file.

Install
-------

#### Linux
`git clone git@github.com:select/sublime-text-jsbeautifier.git ~/.config/sublime-text-2/Packages/Jsbeautify`

#### Mac
`git clone git@github.com:select/sublime-text-jsbeautifier.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Jsbeautify`

#### Windows
`git clone git@github.com:select/sublime-text-jsbeautifier.git %APPDATA%/Sublime\ Text\ 2/Packages/Jsbeautify`

Key Binding
-----------

The default key binding is `ctrl+shift+j`

This is similar to auto pep8 `ctrl+shift+8` for python

Updates
-------

- 3/7/2013 - Forked project, updated jsbeautifier, added sublime settings, changed keybinding
- 8/25/2011 - Added sublime-commands file. `Format: Javascript` now appears in the command palette
- 8/25/2011 - scrolls back to whatever line you were on prior to formatting the file (middle of screen) rather than leaving the view position at the top of the file after formatting.
