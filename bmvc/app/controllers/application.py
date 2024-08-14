from bottle import template, redirect

from app.controllers.datarecord import DataRecord

class Application():

    def __init__(self):
        self.pages = {
            'portal':self.portal,
        }
        self.models = DataRecord()

    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

    def helper(self):
        return template('app/views/html/helper')
    
    def validate_user(self, username, password):
        user = self.models.find_user(username)
        if user and user.password == password:
            return True
        return False    
    
    def portal(self, parameter=None):
        if not parameter:
            # Se não há parâmetro, não há dados transferidos
            return template('app/views/html/portal', transfered=False)
        else:
            info = self.models.work_with_parameter(parameter)
            
            if not info:
                # Redireciona para a página sem parâmetros
                redirect('/portal')
            else:
                # Dados foram encontrados, então eles devem ser passados
                return template('app/views/html/portal', transfered=True, data=info)
