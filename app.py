from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    password = []
    # Agrega al menos un carácter de cada tipo seleccionado
    if use_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        characters += string.digits
        password.append(random.choice(string.digits))
    if use_special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))
    # Genera el resto de la contraseña
    while len(password) < length:
        password.append(random.choice(characters))
    # Mezcla los caracteres para evitar patrones predecibles
    random.shuffle(password)
    # Convierte la lista de caracteres en una cadena
    password = ''.join(password)

    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    #Se inicializa la contraseña y las variables de los checkbox
    password = ''
    use_uppercase = use_numbers = True
    use_special = False
    #Se verifica si se ha enviado un formulario
    if request.method == 'POST':
        length = int(request.form['length'])#Se obtiene la longitud de la contraseña
        #Se verifica si se han seleccionado los checkbox
        use_uppercase = 'uppercase' in request.form
        use_numbers = 'numbers' in request.form
        use_special = 'special' in request.form
        #Se llama a la función que genera la contraseña
        password = generate_password(length, use_uppercase, use_numbers, use_special)

    return render_template('index.html', password=password, use_uppercase=use_uppercase, use_numbers=use_numbers,use_special=use_special)#Se renderiza index.html con la contraseña generada

if __name__ == '__main__':
    app.run()