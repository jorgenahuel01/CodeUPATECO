import random

ROLES = ("admin", "user")
usuarios = []
next_id = 1

NOMBRES = ["Carlos", "Ana", "Luis", "Maria", "Pedro", "Laura", "Sofia", "Diego", "Valentina", "Andres"]
APELLIDOS = ["Garcia", "Lopez", "Martinez", "Rodriguez", "Gonzalez", "Hernandez", "Perez", "Torres", "Ramirez", "Flores"]


def crear_usuario():
    print("\n--- CREAR USUARIO ---")

    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    apellido = input("Apellido: ").strip()
    if apellido == "":
        print("El apellido no puede estar vacio.")
        return

    edad_str = input("Edad: ").strip()
    if not edad_str.isdigit() or not (1 <= int(edad_str) <= 120):
        print("Edad invalida.")
        return

    print(f"Roles disponibles: {ROLES[0]} / {ROLES[1]}")
    rol = input("Rol: ").strip().lower()
    if rol not in ROLES:
        print("Rol invalido.")
        return

    usuario = f"{nombre.lower()}.{apellido.lower()}"
    for u in usuarios:
        if u["usuario"] == usuario:
            usuario = usuario + str(random.randint(10, 99))
            break

    global next_id
    usuarios.append({
        "id": next_id,
        "nombre": nombre,
        "apellido": apellido,
        "usuario": usuario,
        "edad": int(edad_str),
        "rol": rol
    })
    next_id += 1
    print(f"Usuario '{usuario}' creado.")


def listar_usuarios():
    print("\n--- LISTA DE USUARIOS ---")
    if len(usuarios) == 0:
        print("No hay usuarios.")
        return
    for u in usuarios:
        print(f"[{u['id']}] {u['nombre']} {u['apellido']} | @{u['usuario']} | Edad: {u['edad']} | Rol: {u['rol']}")


def buscar_usuario():
    print("\n--- BUSCAR USUARIO ---")
    termino = input("Nombre o usuario: ").strip().lower()
    encontrado = False
    for u in usuarios:
        if termino in u["nombre"].lower() or termino in u["usuario"].lower():
            print(f"[{u['id']}] {u['nombre']} {u['apellido']} | @{u['usuario']} | Edad: {u['edad']} | Rol: {u['rol']}")
            encontrado = True
    if not encontrado:
        print("No se encontro ningun usuario.")


def editar_usuario():
    print("\n--- EDITAR USUARIO ---")
    id_str = input("ID del usuario: ").strip()
    if not id_str.isdigit():
        print("ID invalido.")
        return

    for u in usuarios:
        if u["id"] == int(id_str):
            print(f"Editando: {u['nombre']} {u['apellido']} (Enter para mantener el valor)")

            nombre = input(f"Nombre [{u['nombre']}]: ").strip()
            if nombre != "":
                u["nombre"] = nombre

            apellido = input(f"Apellido [{u['apellido']}]: ").strip()
            if apellido != "":
                u["apellido"] = apellido

            edad_str = input(f"Edad [{u['edad']}]: ").strip()
            if edad_str != "":
                if edad_str.isdigit() and 1 <= int(edad_str) <= 120:
                    u["edad"] = int(edad_str)
                else:
                    print("Edad invalida, se mantiene la anterior.")

            rol = input(f"Rol [{u['rol']}] (admin/user): ").strip().lower()
            if rol != "":
                if rol in ROLES:
                    u["rol"] = rol
                else:
                    print("Rol invalido, se mantiene el anterior.")

            print("Usuario actualizado.")
            return

    print("Usuario no encontrado.")


def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    id_str = input("ID del usuario: ").strip()
    if not id_str.isdigit():
        print("ID invalido.")
        return

    for i in range(len(usuarios)):
        if usuarios[i]["id"] == int(id_str):
            print(f"Eliminando a '{usuarios[i]['usuario']}'...")
            usuarios.pop(i)
            print("Usuario eliminado.")
            return

    print("Usuario no encontrado.")


def generar_automatico():
    print("\n--- GENERAR USUARIO AUTOMATICO ---")
    nombre = random.choice(NOMBRES)
    apellido = random.choice(APELLIDOS)
    edad = random.randint(18, 60)
    rol = random.choice(ROLES)
    usuario = f"{nombre.lower()}.{apellido.lower()}"

    for u in usuarios:
        if u["usuario"] == usuario:
            usuario = usuario + str(random.randint(10, 99))
            break

    global next_id
    usuarios.append({
        "id": next_id,
        "nombre": nombre,
        "apellido": apellido,
        "usuario": usuario,
        "edad": edad,
        "rol": rol
    })
    next_id += 1
    print(f"Generado: @{usuario} | {nombre} {apellido} | Edad: {edad} | Rol: {rol}")


def estadisticas():
    print("\n--- ESTADISTICAS ---")
    print(f"Total de usuarios: {len(usuarios)}")
    admins = 0
    for u in usuarios:
        if u["rol"] == "admin":
            admins += 1
    print(f"Admins: {admins} | Users: {len(usuarios) - admins}")


def usuario_aleatorio():
    print("\n--- USUARIO ALEATORIO ---")
    if len(usuarios) == 0:
        print("No hay usuarios.")
        return
    u = random.choice(usuarios)
    print(f"[{u['id']}] {u['nombre']} {u['apellido']} | @{u['usuario']} | Edad: {u['edad']} | Rol: {u['rol']}")


# Programa principal
print("=== SISTEMA DE USUARIOS ===")

while True:
    print("\n1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Editar usuario")
    print("5. Eliminar usuario")
    print("6. Generar automatico")
    print("7. Estadisticas")
    print("8. Usuario aleatorio")
    print("0. Salir")

    opcion = input("\nOpcion: ").strip()

    match opcion:
        case "1":
            crear_usuario()
        case "2":
            listar_usuarios()
        case "3":
            buscar_usuario()
        case "4":
            editar_usuario()
        case "5":
            eliminar_usuario()
        case "6":
            generar_automatico()
        case "7":
            estadisticas()
        case "8":
            usuario_aleatorio()
        case "0":
            print("Hasta luego.")
            break
        case _:
            print("Opcion invalida.")
