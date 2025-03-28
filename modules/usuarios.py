class Usuario:
    def __init__(self, cedula,user,correo,rol,contraseña):
        self.cedula=cedula
        self.user=user
        self.correo=correo
        self.rol=rol
        self.contraseña=contraseña
        

    def UsuarioDBCollection(self):
        return{
            "cedula":self.cedula,
            "user":self.user,
            "correo":self.correo,
            "rol": self.rol, 
            "contraseña":self.contraseña,
            
        }