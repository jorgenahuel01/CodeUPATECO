import random

ROLES = ("admin", "user")

usuarios = []
contador_id = 1

NOMBRES = ["Carlos", "Ana", "Luis", "María", "Pedro", "Laura", "Sofía", "Diego", "Valentina", "Andrés"]
APELLIDOS = ["García", "López", "Martínez", "Rodríguez", "González", "Hernández", "Pérez", "Torres", "Ramírez", "Flores"]


def generar_id():
    global contador_id
    nuevo_id = contador_id
    contador_id += 1
    return nuevo_id


def usuario_existe(nombre_usuario):
    for u in usuarios:
        if u["usuario"] == nombre_usuario:
            return True
    return False


def validar_edad(edad_str):
    if not edad_str.isdigit():
        return None
    edad = int(edad_str)
    if edad < 1 or edad > 120:
        return None
    return edad


def validar_rol(rol_str):
    rol = rol_str.strip().lower()
    if rol in ROLES:
        return rol
    return None


def validar_nombre(texto):
    nombre = texto.strip()
    if len(nombre) == 0:
        return None
    for c in nombre:
        if not (c.isalpha() or c == " "):
            return None
    return nombre


def crear_usuario():
    print("\n--- CREAR USUARIO ---")

    while True:
        nombre = input("Nombre: ").strip()
        resultado = validar_nombre(nombre)
        if resultado:
            nombre = resultado
            break
        print("  Nombre inválido. Solo letras y no puede estar vacío.")

    while True:
        apellido = input("Apellido: ").strip()
        resultado = validar_nombre(apellido)
        if resultado:
            apellido = resultado
            break
        print("  Apellido inválido. Solo letras y no puede estar vacío.")

    nombre_usuario_base = f"{nombre.lower().replace(' ', '')}.{apellido.lower().replace(' ', '')}"
    nombre_usuario = nombre_usuario_base
    sufijo = 1
    while usuario_existe(nombre_usuario):
        nombre_usuario = f"{nombre_usuario_base}{sufijo}"
        sufijo += 1

    while True:
        edad_str = input("Edad: ").strip()
        edad = validar_edad(edad_str)
        if edad:
            break
        print("  Edad inválida. Debe ser un número entre 1 y 120.")

    print(f"Roles disponibles: {', '.join(ROLES)}")
    while True:
        rol_str = input("Rol: ").strip()
        rol = validar_rol(rol_str)
        if rol:
            break
        print(f"  Rol inválido. Debe ser: {' o '.join(ROLES)}")

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "apellido": apellido,
        "usuario": nombre_usuario,
        "edad": edad,
        "rol": rol
    }
    usuarios.append(nuevo)
    print(f"\n  Usuario '{nombre_usuario}' creado con ID {nuevo['id']}.")


def listar_usuarios():
    print("\n--- LISTA DE USUARIOS ---")
    if len(usuarios) == 0:
        print("  No hay usuarios registrados.")
        return

    print(f"{'ID':<5} {'Nombre':<15} {'Apellido':<15} {'Usuario':<25} {'Edad':<6} {'Rol'}")
    print("-" * 75)
    for u in usuarios:
        print(f"{u['id']:<5} {u['nombre']:<15} {u['apellido']:<15} {u['usuario']:<25} {u['edad']:<6} {u['rol']}")


def buscar_usuario():
    print("\n--- BUSCAR USUARIO ---")
    if len(usuarios) == 0:
        print("  No hay usuarios registrados.")
        return

    termino = input("Buscar por nombre, apellido o usuario: ").strip().lower()
    if termino == "":
        print("  Término de búsqueda vacío.")
        return

    encontrados = []
    for u in usuarios:
        if (termino in u["nombre"].lower() or
                termino in u["apellido"].lower() or
                termino in u["usuario"].lower()):
            encontrados.append(u)

    if len(encontrados) == 0:
        print("  No se encontraron usuarios.")
        return

    print(f"\n  Se encontraron {len(encontrados)} resultado(s):\n")
    for u in encontrados:
        print(f"  ID: {u['id']} | {u['nombre']} {u['apellido']} | @{u['usuario']} | Edad: {u['edad']} | Rol: {u['rol']}")


def editar_usuario():
    print("\n--- EDITAR USUARIO ---")
    if len(usuarios) == 0:
        print("  No hay usuarios registrados.")
        return

    id_str = input("ID del usuario a editar: ").strip()
    if not id_str.isdigit():
        print("  ID inválido.")
        return

    id_buscar = int(id_str)
    usuario_encontrado = None
    for u in usuarios:
        if u["id"] == id_buscar:
            usuario_encontrado = u
            break

    if not usuario_encontrado:
        print(f"  No existe usuario con ID {id_buscar}.")
        return

    print(f"\n  Editando: {usuario_encontrado['nombre']} {usuario_encontrado['apellido']} (@{usuario_encontrado['usuario']})")
    print("  (Presiona Enter para mantener el valor actual)\n")

    campos = ["nombre", "apellido", "edad", "rol"]
    for campo in campos:
        valor_actual = usuario_encontrado[campo]
        entrada = input(f"  {campo.capitalize()} [{valor_actual}]: ").strip()

        if entrada == "":
            continue

        if campo == "nombre" or campo == "apellido":
            resultado = validar_nombre(entrada)
            if resultado:
                usuario_encontrado[campo] = resultado
            else:
                print(f"  Valor inválido para {campo}, se mantiene el anterior.")
                continue

        elif campo == "edad":
            edad = validar_edad(entrada)
            if edad:
                usuario_encontrado[campo] = edad
            else:
                print("  Edad inválida, se mantiene la anterior.")
                continue

        elif campo == "rol":
            rol = validar_rol(entrada)
            if rol:
                usuario_encontrado[campo] = rol
            else:
                print(f"  Rol inválido. Debe ser {' o '.join(ROLES)}, se mantiene el anterior.")
                continue

    nombre_nuevo = f"{usuario_encontrado['nombre'].lower().replace(' ', '')}.{usuario_encontrado['apellido'].lower().replace(' ', '')}"
    if nombre_nuevo != usuario_encontrado["usuario"]:
        candidato = nombre_nuevo
        sufijo = 1
        while usuario_existe(candidato) and candidato != usuario_encontrado["usuario"]:
            candidato = f"{nombre_nuevo}{sufijo}"
            sufijo += 1
        usuario_encontrado["usuario"] = candidato

    print(f"\n  Usuario actualizado: @{usuario_encontrado['usuario']}")


def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    if len(usuarios) == 0:
        print("  No hay usuarios registrados.")
        return

    id_str = input("ID del usuario a eliminar: ").strip()
    if not id_str.isdigit():
        print("  ID inválido.")
        return

    id_buscar = int(id_str)
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == id_buscar:
            eliminado = usuarios[i]
            confirmacion = input(f"  ¿Eliminar a '{eliminado['usuario']}'? (s/n): ").strip().lower()
            if confirmacion == "s":
                usuarios.pop(i)
                print(f"  Usuario '{eliminado['usuario']}' eliminado.")
            else:
                print("  Operación cancelada.")
            return

    print(f"  No existe usuario con ID {id_buscar}.")


def generar_usuario_automatico():
    print("\n--- GENERAR USUARIO AUTOMÁTICO ---")

    nombre = random.choice(NOMBRES)
    apellido = random.choice(APELLIDOS)
    edad = random.randint(18, 60)
    rol = random.choice(ROLES)

    nombre_usuario_base = f"{nombre.lower()}.{apellido.lower()}"
    nombre_usuario = nombre_usuario_base
    sufijo = 1
    while usuario_existe(nombre_usuario):
        nombre_usuario = f"{nombre_usuario_base}{sufijo}"
        sufijo += 1

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "apellido": apellido,
        "usuario": nombre_usuario,
        "edad": edad,
        "rol": rol
    }
    usuarios.append(nuevo)
    print(f"  Usuario generado: @{nombre_usuario} | {nombre} {apellido} | Edad: {edad} | Rol: {rol}")


def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS ---")
    total = len(usuarios)
    print(f"  Total de usuarios: {total}")

    if total == 0:
        return

    conteo_roles = {}
    for rol in ROLES:
        conteo_roles[rol] = 0

    suma_edades = 0
    for u in usuarios:
        if u["rol"] in conteo_roles:
            conteo_roles[u["rol"]] += 1
        suma_edades += u["edad"]

    print(f"  Promedio de edad:  {suma_edades // total} años")
    for rol, cantidad in conteo_roles.items():
        print(f"  {rol.capitalize():<10}: {cantidad} usuario(s)")


def seleccionar_usuario_aleatorio():
    print("\n--- USUARIO ALEATORIO ---")
    if len(usuarios) == 0:
        print("  No hay usuarios registrados.")
        return

    elegido = random.choice(usuarios)
    print(f"  Usuario seleccionado:")
    print(f"  ID: {elegido['id']} | {elegido['nombre']} {elegido['apellido']} | @{elegido['usuario']} | Edad: {elegido['edad']} | Rol: {elegido['rol']}")


def mostrar_menu():
    print("\n=============================")
    print("  SISTEMA DE USUARIOS")
    print("=============================")
    print("  1. Crear usuario")
    print("  2. Listar usuarios")
    print("  3. Buscar usuario")
    print("  4. Editar usuario")
    print("  5. Eliminar usuario")
    print("  6. Generar usuario automático")
    print("  7. Estadísticas")
    print("  8. Usuario aleatorio")
    print("  0. Salir")
    print("-----------------------------")


def main():
    print("Bienvenido al Sistema de Administración de Usuarios")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "":
            continue

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
                generar_usuario_automatico()
            case "7":
                mostrar_estadisticas()
            case "8":
                seleccionar_usuario_aleatorio()
            case "0":
                print("\n  Cerrando sistema. Hasta luego.")
                break
            case _:
                print("  Opción inválida. Intenta de nuevo.")


main()
