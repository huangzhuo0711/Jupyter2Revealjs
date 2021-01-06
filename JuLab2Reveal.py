# Wrapper and adjustment for jupyterlab workfolw converte to Reveal.js slides;
# Zhuo Huang 2020.12.15; 
def headwrapper():
	return r'''<meta name="apple-mobile-web-app-capable" content="yes">
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/mystyle.css" id="theme">'''

def backgroundwrapper(img = "./pictures/background2.png"):
	return r'''<script>$("section:last").attr("data-background" ,"{}");$("section:last").attr("data-background-size" ,"98%")</script>'''.format(img)

def positionadjust(obj = ".text_cell_render:last", position = "top: 10%; left:10% ; width: 80%"):
	return r'''<script>$("{0}").attr("style","position:fixed; {1}")</script>'''.format(obj, position)

def tailwrapper():
	return '''<script> $(document).ready(function(){$('.input, .prompt, .output_stderr, .output_error').hide()})</script>'''
