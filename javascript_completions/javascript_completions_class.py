import json

JC_SETTINGS_FOLDER_NAME = "javascript_completions"
JC_SETTINGS_FOLDER = os.path.join(PACKAGE_PATH, JC_SETTINGS_FOLDER_NAME)

class JavaScriptCompletions():
  def init(self):
    self.api = {}
    self.API_Setup = sublime.load_settings('JavaScript-Completions.sublime-settings').get('completion_active_list')
    sublime.set_timeout_async(self.load_api)

  def load_api(self):
    # Caching completions
    if self.API_Setup:
      for API_Keyword in self.API_Setup:
        self.api[API_Keyword] = sublime.load_settings( API_Keyword + '.sublime-settings' )
        if self.api[API_Keyword].get("scope") == None :
          path_to_json = os.path.join(PACKAGE_PATH, "sublime-completions", API_Keyword + '.sublime-settings' )
          if os.path.isfile(path_to_json):
            with open(path_to_json) as json_file:
              self.api[API_Keyword] = json.load(json_file)

  def get(self, key):
    return sublime.load_settings('JavaScript-Completions.sublime-settings').get(key)