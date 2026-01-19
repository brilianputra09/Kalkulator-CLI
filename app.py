from flask import Flask, render_template, request
from math_ops import tambah, kurang, kali, bagi
from strings_ops import huruf_besar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        a = float(request.form["angka1"])
        b = float(request.form["angka2"])
        operasi = request.form["operasi"]

        if operasi == "tambah":
            hasil = tambah(a, b)
        elif operasi == "kurang":
            hasil = kurang(a, b)
        elif operasi == "kali":
            hasil = kali(a, b)
        elif operasi == "bagi":
            hasil = bagi(a, b)

    return render_template(
        "index.html",
        judul=huruf_besar("kalkulator flask"),
        hasil=hasil
    )

if __name__ == "__main__":
    app.run(debug=True)
