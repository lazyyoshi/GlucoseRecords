#!python3
import appex, ui
import os
import console
import dbcont as db
import datetime
import dialogs

type_symbols = ('BB', 'AB', 'BL', 'AL', 'BS', 'AS', 'BT', 'C', '+')

class AddBSView (ui.View):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self._result = False
		self.bounds = (0, 0, 400, 200)
		button_style = {'background_color': (0, 0, 0, 0.05), 'tint_color': 'black', 'font': ('HelveticaNeue-Light', 24), 'corner_radius': 3}
		self.number_buttons = [ui.Button(title=str(i), action=self.button_tapped, **button_style) for i in range(10)]
		self.op_buttons = [ui.Button(title=s, action=self.button_tapped, **button_style) for s in type_symbols]
		self.op_buttons[0].tint_color ='red'
		self.op_buttons[1].tint_color ='red'
		self.op_buttons[2].tint_color ='green'
		self.op_buttons[3].tint_color ='green'
		self.op_buttons[4].tint_color ='blue'
		self.op_buttons[5].tint_color ='blue'
		for b in self.number_buttons + self.op_buttons:
			self.add_subview(b)
		self.display_view = ui.View(background_color=(.54, .94, 1.0, 0.2))
		self.label = ui.Label(frame=self.display_view.bounds.inset(0,8),flex='wh',text='0', alignment=ui.ALIGN_RIGHT)
		self.label.font = ('HelveticaNeue-Light', 32)
		self.display_view.add_subview(self.label)
		self.label2 = ui.Label(frame=self.display_view.bounds.inset(0,8),flex='wh',text='朝食前', alignment=ui.ALIGN_CENTER)
		self.label2.font = ('HelveticaNeue-Light', 16)
		self.display_view.add_subview(self.label2)
		self.label3 = ui.Label(frame=self.display_view.bounds.inset(0,8),flex='wh',text='2019/03/07 13:50', alignment=ui.ALIGN_LEFT)
		self.label3.font = ('HelveticaNeue-Light', 16)
		self.display_view.add_subview(self.label3)
		self.add_subview(self.display_view)
		
	def layout(self):
		self.label3.text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
		self.label2.text = '朝食前'
		compact = self.height < 150
		bw = self.width / 10 if compact else self.width / 5
		bh = self.height / 3 if compact else self.height / 5
		for i, b in enumerate(self.number_buttons):
			if compact:
				frame = ui.Rect(((i - 1) % 10) * bw, bh, bw, bh)
			else:
				frame = ui.Rect(max(i-1, 0) % 3 * bw, 3 * bh - (i-1) // 3 * bh, bw, bh)
			b.frame = frame.inset(1, 1)
		for i, b in enumerate(self.op_buttons):
			if compact:
				if i == 8:
					frame = ui.Rect(8 * bw, 2 * bh, 2 * bw, bh)
				else:
				  frame = ui.Rect(((i-1) * bw + bw), 2 * bh, bw, bh)
			else:
				if i == 8:
					frame = ui.Rect(bw, 4 * bh, 2 * bw, bh)
				else:
				  frame = ui.Rect((3 + i % 2) * bw, (1 + i//2) * bh, bw, bh)
			b.frame = frame.inset(1, 1)

		self.display_view.frame = (0, 0, self.width, bh)

	def button_tapped(self, sender):
		t = sender.title
		bs = self.label
		tp = self.label2
		
		if t in '0123456789':
			if bs.text == '0':
				bs.text = t
			else:
				bs.text += t
		elif t == 'C':
			bs.text = '0'
		elif t == 'BB':
			tp.text = '朝食前'
		elif t == 'AB':
			tp.text = '朝食後'
		elif t == 'BL':
			tp.text = '昼食前'
		elif t == 'AL':
			tp.text = '昼食後'
		elif t == 'BS':
			tp.text = '夕食前'
		elif t == 'AS':
			tp.text = '夕食後'
		elif t == 'BT':
			tp.text = '就寝時'
		elif t == '+':
			self.mydb = db.DBCont('dbs.db')
			self.mydb.addGlucose(int(bs.text), tp.text)
			self.mydb = None
			bs.text = '0'
					
def main():
	# Optimization: Don't create a new view if the widget already shows the calculator.
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	widget_view = appex.get_widget_view()
	if widget_view is None or widget_view.name != widget_name:
		widget_view = AddBSView()
		widget_view.name = widget_name
		appex.set_widget_view(widget_view)

if __name__ == '__main__':
	main()
