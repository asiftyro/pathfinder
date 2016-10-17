import sublime, sublime_plugin, os

class PathfinderCopyPathCommand(sublime_plugin.TextCommand):

	def run(self, edit):
			try:
				self.copied_path = self.view.file_name()
				sublime.set_clipboard(self.copied_path)
			except Exception as e:
				sublime.error_message(str(e).capitalize())


class PathfinderPasteRelativePathCommand(sublime_plugin.TextCommand):

	def run(self, edit):
			try:
				# Get remote file full path from clipboard
				self.remote_file_path = sublime.get_clipboard();
				# Get the path of file where this command is executed
				self.local_file_path = self.view.file_name()
				# If both of above are in same level of dir, just take the remote file name
				# Else determine relative path
				if (os.path.dirname(self.local_file_path) == os.path.dirname(self.remote_file_path)):
					self.rel_path = os.path.basename(self.remote_file_path)
				else:
					self.rel_path = os.path.relpath(sublime.get_clipboard(), os.path.dirname(self.view.file_name()))
					# covert to unix/linux path
					self.rel_path = self.rel_path.replace('\\','/')
				# Reference to selection where to insert relative path
				selections = self.view.sel()
				for selection in selections:
					# Erase selected text
					self.view.erase(edit, selection)
					# Insert at current cursor position
					self.view.insert(edit, selection.begin(), self.rel_path)
					# End edit
					self.view.end_edit(edit)
			except Exception as e:
				sublime.error_message(str(e).capitalize())

class PathfinderPasteThisFileLocationCommand(sublime_plugin.TextCommand):

	def run(self, edit):
			try:
				# get filename and covert to unix/linux path
				self.local_file_path = self.view.file_name().replace('\\','/');
				# Reference to selection where to insert relative path
				selections = self.view.sel()
				for selection in selections:
					# Erase selected text
					self.view.erase(edit, selection)
					# Insert at current cursor position
					self.view.insert(edit, selection.begin(), self.local_file_path)
					# End edit
					self.view.end_edit(edit)
			except Exception as e:
				sublime.error_message(str(e).capitalize())

