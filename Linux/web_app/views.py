from django.http import HttpResponse
import subprocess as sub
import commands
from threading import Thread
import subprocess
from django.conf import settings

base_url = settings.BASE_PATH

def test(request):
    return HttpResponse("OK", mimetype='application/json')

def execute_cache_build():
    command = "java -jar " + base_url + "selenium-server-standalone-2.40.0.jar -htmlSuite \"*firefox\" \""+settings.ROOT_DOMAIN+"\" \""+base_url+"build_cache_suit.html\" \""+base_url +"clear_cache_output.html\""
    subprocess.call(command, shell=True)

def execute_clear_cache():
    command = "java -jar " + base_url + "selenium-server-standalone-2.40.0.jar -htmlSuite \"*firefox\" \""+settings.ROOT_DOMAIN+"\" \""+base_url+"clear_cache_suit.html\" \""+base_url +"clear_cache_output.html\""
    subprocess.call(command, shell=True)
    execute_cache_build()


def clear_cache(request):
    thread = Thread(target = execute_clear_cache)
    thread.start()
    return HttpResponse("Script Started", mimetype='application/json')







    
