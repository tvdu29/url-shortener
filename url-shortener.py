from flask import Flask, redirect, request, Response
import csv
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    urls = {}
    data = request.get_data(cache=False, as_text=True)
    with open("/data/urls.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        for k, v in reader:
            urls[k] = v
        file.close()
        i = 1
        while (str(i) in urls):
            i += 1
        urls[str(i)] = data
        with open("/data/urls.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([str(i), data])
            file.close()
            return ("%d" % i)

@app.route('/follow/<string:urlid>')
def follow(urlid):
    urls = {}
    with open("/data/urls.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        for k, v in reader:
            urls[k] = v
        file.close()
    if (urlid in urls):
        return redirect(urls[urlid])
    else:
        return Response("<h1>URL "+urlid+" not found</h1>", status=404, mimetype="text/html")

