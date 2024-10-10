import shutil,os
# mkdir .repodeploy
shutil.rmtree('.repo_deploy', ignore_errors=True)
# mkdir .repo_deploy
os.mkdir('.repo_deploy')
# copy src/* to .repo_deploy/name of the repo

stream = os.popen('git remote -v')
output = stream.read()
repo   = output.split("\n")[0].split("\t")[1].split(" ")[0]

# clone the repo 
os.system('git clone ' + repo + ' .repo_deploy/' + repo.split("/")[-1])