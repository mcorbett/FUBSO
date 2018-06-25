from flask import Flask, render_template, redirect, url_for
import os, subprocess, docker

app = Flask(__name__)

ld='/data/zurich'

@app.route('/')
def main():
    return redirect(url_for('index'))

@app.route('/FUBSO/')
def index():
   return render_template('index.html')

@app.route('/FUBSO/bcl2fastq/')
def bcl():
   dm="Starting docker container using "+ld+" as input"
   dc="docker run --rm --privileged -i -v "+ld+":/data illumina/bcl2fastq-v2.19.0.316 bcl2fastq  -l TRACE --runfolder-dir  /data/$opt --output-dir /data/150924_ML-P2-12_0014_H003FY_PoolW_TSCA/Samples/Fastq &"
   ad=listdirs(ld)
   o=os.popen('echo "you selected BCL2FASTQ\n"').read()
   client = docker.from_env()
   dict=client.images.list()
   ac=client.containers.list()
   acnn=isacNull(ac) # Check that there available containers(ac) is not null.
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
   il=d.split()
   return render_template('WorldCup.html', 
   analysis_name="BCL2FASTQ",
   programmer="Matt Corbett", 
   available_directories=ad,
   listed_directory=ld,
   docker_command=dc,
   docker_message=dm,
   available_containers=ac,
   image_list=il
   )

def isacNull(l):
    if l:
        return l
    else:
        return 'No Containers are running now'

@app.route('/FUBSO/RNA-SEQ/')
def rnaseq():
   dm="Starting docker container using "+ld+" as input"
   dc="docker run --rm --privileged -i -v "+ld+":/data -v /data/genomes_bssh_rnaSeqAlignment_1.1.0:/genomes illumina/isis-rna-seq-2.6.25.18 /opt/illumina/Isis/2.6.25.18/Isis -r /data/$opt &"
   ad=listdirs(ld)
   o=os.popen('echo "you selected RNA-SEQ\n"').read()
   client = docker.from_env()
   dict=client.images.list()
   ac=client.containers.list()
   acnn=isacNull(ac) # Check that there available containers(ac) is not null.
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
   il=d.split()
   return render_template('WorldCup.html', 
   analysis_name="RNA-SEQ",
   programmer="Matt Corbett", 
   available_images=d,
   available_directories=ad,
   listed_directory=ld,
   docker_command=dc,
   docker_message=dm,
   available_containers=acnn,
   image_list=il
   )

@app.route('/FUBSO/TruSeqAmp/')
def truseqamp():
   dm="Starting docker container using "+ld+" as input"
   dc="docker run --rm --privileged -i -v "+ld+":/runs -v /data/genomes_bssh_truseqAmplicon_2.0.0:/genomes illumina/truseqamplicon-2.0.0.0  mono /opt/illumina/Isis/2.6.21.7.TruSeqAmplicon/Isis.exe -r /runs/$opt -c 2 -a /runs/$opt/Samples &"
   ad=listdirs(ld)
   o=os.popen('echo "you selected TruSeqAmp\n"').read()
   client = docker.from_env()
   dict=client.images.list()
   ac=client.containers.list()
   acnn=isacNull(ac) # Check that there available containers(ac) is not null.
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
   il=d.split()
   return render_template('WorldCup.html', 
   analysis_name="TruSeqAmp",
   programmer="Matt Corbett", 
   available_images=d,
   available_directories=ad,
   listed_directory=ld,
   docker_command=dc,
   docker_message=dm,
   available_containers=acnn,
   image_list=il
   )

@app.route('/FUBSO/Enrichment_30')
def Enrichment_30():
   dm="Starting docker container using "+ld+" as input"
   dc="sudo docker run --privileged --rm -v "+ld+":/data -v /data/genomes_bssh_enrichment_3.0.0:/genomes illumina/enrichment-3.0.0 mono /opt/illumina/Isas/2.10.12/Isas.exe -r /data/$opt"
   ad=listdirs(ld)
   o=os.popen('echo "you selected Enrichment 3.0\n"').read()
   client = docker.from_env()
   dict=client.images.list()
   ac=client.containers.list()
   acnn=isacNull(ac) # Check that there available containers(ac) is not null.
   d=" " 
   for x in range(len(dict)):
      d=d+(" "+str(dict[x])[9:].replace("'>",'')+"\n")
   il=d.split()
   return render_template('WorldCup.html', 
   analysis_name="Enrichment 3.0",
   programmer="Matt Corbett", 
   available_images=d,
   available_directories=ad,
   listed_directory=ld,
   docker_command=dc,
   docker_message=dm,
   available_containers=acnn,
   image_list=il
   )

@app.route('/msc')
def f():
    cmd = "ls"
    returned_output = subprocess.check_output(cmd)
    return returned_output

def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]

if __name__ == '__main__':
    app.run(debug=True)