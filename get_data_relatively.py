from bs4 import BeautifulSoup
html_string = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Web Development Page</title>
		<style type="text/css">
			
			h1{
				color: white;
				background: red;
			}

			li{
				color: red;
			}

			#css-li{
				color: blue;
			}

			.green{
				color: green;
			}

		</style>
	</head>
	<body>
		<h1>Web Development</h1>
		<h1 class="green">Web</h1>
		<h3>Programming Languages</h3>

		<ol>
			<li>HTML</li>
			<li id="css-li">CSS</li>
			<li class="green">JavaScript</li>
			<li class="green bold" id="python-li">Python</li>
		</ol>

	</body>
	</html>



"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
# data = parsed_html.body
# data = parsed_html.body.contents[1]
# data = parsed_html.body.contents[1].next_sibling.next_sibling.next_sibling.next_sibling
data = parsed_html.find(id="css-li").parent.previous_sibling.previous_sibling
# data = parsed_html.find(id="css-li").find_next_sibling().find_previous_sibling()
# data = parsed_html.find(id="css-li").find_next_sibling(id="python-li")
# data = parsed_html.find(id="css-li").find_next_sibling(class_="bold")
# data = parsed_html.find(id="css-li").find_next_sibling(class_="bold").find_parent().find_parent()
# data = parsed_html.body.findChildren()[2].find_next_sibling()
print(data)















