from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "I Made Website With  Python + Flask + Linux + Apache2!"

@app.route("/returnsHTML")
def secondEndPoint():
    return """
<html>
	<body>
		<h1>What I learned about sed</h1>
		<p><a href="https://www.grymoire.com/Unix/Sed.html">I learned it all here!</a> 
		<h2>First thing I learned</h2>
		<p>Know more about the use of symbols</p>
		<h2>Second thing I learned</h2>
    <p>Learned to apply more commands</p>
		<h2>Third thing I learned</h2>
		<p>Learn more knowledge more skilled use of command</p>
	</body>
</html>
"""


if __name__ == "__main__":
    app.run()
