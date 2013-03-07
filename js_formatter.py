import sublime
import sublime_plugin
import jsbeautifier

# I made this: Falko Krause" <falko.krause@gmail.com>

# This plugin is based on
# https://github.com/bjouhier/sublime-text-jsbeautifier
# https://github.com/einars/js-beautify


# base_name = sublime.platform() == 'windows' and 'Jsbeautify (Windows).sublime-settings' or 'AutoPep8.sublime-settings'
base_name = 'JsBeautify.sublime-settings'


class JsbeautifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings(base_name)
        opts = jsbeautifier.default_options()
        opts.indent_char = settings.get('indent_char', None)
        opts.indent_size = settings.get('indent_size', None)
        opts.max_preserve_newlines = settings.get('max_preserve_newlines', None)
        selection = self.view.sel()[0]
        replaceRegion = selection if len(selection) > 0 else sublime.Region(0, self.view.size())
        res = jsbeautifier.beautify(self.view.substr(replaceRegion), opts)
        prePos = self.view.sel()[0]
        self.view.replace(edit, replaceRegion, res)
        self.view.show_at_center(prePos.begin())

    def is_visible(self, *args):
        return self.view.settings().get('syntax') == "Packages/JavaScript/JavaScript.tmLanguage" or self.view.settings().get('syntax') == "Packages/JavaScript/JSON.tmLanguage"
