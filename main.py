from flask import Flask, render_template
app = Flask(__name__)
app.template_folder = 'template'

@app.route('/')
def dasboard():
    return render_template('dasboard.html')

@app.route('/statistik_desa')
def statistik_desa():
    return render_template ('statistik_desa.html')

@app.route('/kegiatan_desa')
def kegiatan_desa():
    return render_template ('kegiatan_desa.html')

@app.route('/pengaduan')
def pengaduan():
    return render_template ('pengaduan.html')

if __name__ == "__main__":
    app.run(debug=True)



