from flask import Flask, render_template, redirect, url_for
import os, subprocess, docker

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('index'))

@app.route('/FUBSO/')
def index():
   return render_template('index.html')

@app.route('/FUBSO/bcl2fastq/')
def bcl():
   # os.chdir("/Users/mcorbett1")
   o=os.popen('echo "you selected BCL2FASTQ\n"').read()
   client = docker.from_env()
   dict=client.images.list()
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
   print(d)
   return render_template('WorldCup.html',analysis_name="BCL2FASTQ",programmer="Matt Corbett")
   
@app.route('/FUBSO/RNA-SEQ/')
def rnaseq():
   os.chdir("/Users/mcorbett1")
   client = docker.from_env()
   dict=client.images.list()
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
      return render_template('WorldCup.html',analysis_name="RNA-SEQ",programmer="Matt Corbett")

@app.route('/FUBSO/TruSeqAmp/')
def truseqamp():
   os.chdir("/Users/mcorbett1")
   client = docker.from_env()
   dict=client.images.list()
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
      return render_template('WorldCup.html',analysis_name="TruSeqAmp",programmer="Matt Corbett")

@app.route('/FUBSO/Enrichment_30')
def Enrichment_30():
   os.chdir("/Users/mcorbett1")
   client = docker.from_env()
   dict=client.images.list()
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
      return render_template('WorldCup.html',analysis_name="Enrichment 3.0",programmer="Matt Corbett")

@app.route('/msc')
def f():
    cmd = "ls"
    returned_output = subprocess.check_output(cmd)
    return returned_output


if __name__ == '__main__':
    app.run(debug=True)
