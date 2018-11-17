import cgi
form = cgi.FieldStroage()
searchterm = form.getvalue('searchbox')

Newterm = searchterm + "Is Kooooool"
