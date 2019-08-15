from flask import Flask, redirect, request, Response
app = Flask(__name__)

urls = {}

@app.route('/generate', methods=['POST'])
def generate():
    global urls
    data = request.get_data(cache=False, as_text=True)
    i = 1
    while (str(i) in urls):
        i += 1
    urls[str(i)] = data
    return ("%d" % i)

@app.route('/follow/<string:urlid>')
def follow(urlid):
    if (urlid in urls):
        return redirect(urls[urlid])
    else:
        return Response("<h1>URL "+urlid+" not found</h1>", status=404, mimetype="text/html")

