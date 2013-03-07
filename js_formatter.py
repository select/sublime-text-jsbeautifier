import sublime
import sublime_plugin
import jsbeautifier
import sys

__version__      = '1.0'
__core_version__ = '1.0'
__authors__      = ['"Falko Krause" <falko.krause@gmail.com>']

# This plugin is based on
# https://github.com/bjouhier/sublime-text-jsbeautifier
# https://github.com/einars/js-beautify

is_python3 = sys.version_info[0] > 2
# Settings
settings = None


def init():
    "Init plugin"
    # load settings
    # globals()['user_settings'] = sublime.load_settings('Preferences.sublime-settings')
    globals()['settings'] = sublime.load_settings('JsFormat.sublime-settings')


class JsbeautifyCommand(sublime_plugin.TextCommand):
    # FIME not sure if I need to parse user settings
    # def __init__(self, settings=None):
    # FIXME need to init base class here
    #     if settings is None:
    #         # settings = {}
    #         for k in ['indent_char', 'indent_size', 'max_preserve_newlines']:
    #             if user_settings.has(k):
    #                 settings[k] = user_settings.get(k, None)

    def run(self, edit):
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


##################
# Init plugin
if not is_python3:
    init()
