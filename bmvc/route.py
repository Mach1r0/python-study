from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response, hashlib


app = Bottle()
ctl = Application()

#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper():
    return ctl.render('helper')

#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/portal', method=['GET', 'POST'])
def portal():
    response.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')

    if request.query.logout:
        response.delete_cookie("session_id")
        response.delete_cookie("username")
        redirect('/portal')

    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')

        if ctl.validate_user(username, password):
            session_id = hashlib.sha256(f"{username}{password}".encode()).hexdigest()
            response.set_cookie("session_id", session_id, secret='your_secret_key')
            response.set_cookie("username", username, secret='your_secret_key')
            redirect(f'/pagina/{username}')
        else:
            return ctl.render('portal')
    else:
        return ctl.render('portal')

@app.route('/pagina/<username>', method='GET')
def user_page(username):
    response.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')

    session_id = request.get_cookie("session_id", secret='your_secret_key')
    logged_in_user = request.get_cookie("username", secret='your_secret_key')

    if not session_id or logged_in_user != username:
        redirect('/portal')
    
    user = ctl.models.find_user(username)
    if user:
        return template('app/views/html/user_page', data=user)
    else:
        redirect('/portal')

#-----------------------------------------------------------------------------

if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
