default: gui/ui_case_lights.py

FORCE:

gui/ui_case_lights.py: gui/compile_gui.py gui/case_lights.ui
	python $<
