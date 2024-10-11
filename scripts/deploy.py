import os 
from djgit.deploy import deploy
target_folder = os.path.join('src', 'dev', 'trial')

deploy(target_folder)