from flask import Flask, redirect, request
app = Flask(__name__)

urls = {}

@app.route('/generate', methods=['POST'])
def generate():
    global urls
    data = request.get_data(cache=False, as_text=True)
    i = 1
    while (i in urls):
        i += 1
    urls[i] = data
    return ("%d" % i)

@app.route('/follow/<int:urlid>')
def follow(urlid):
    if (urlid in urls):
        return redirect(urls[urlid])

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
