# Sistema de Gestión de Préstamo de Herramientas 🛠️🏡

**Versión 1.0 — Python**

Un programa de consola desarrollado en Python diseñado para que la junta comunal gestione el inventario y el préstamo comunitario de herramientas. El sistema permite llevar un control riguroso de usuarios, stock y trazabilidad de los préstamos, eliminando la dependencia de cuadernos y llamadas telefónicas.

---

## 🧩 Problemática que resuelve

En la comunidad existe la excelente costumbre de compartir herramientas entre vecinos, pero esto genera problemas de control:
- Herramientas que no se devuelven a tiempo o se pierden.
- Desconocimiento sobre quién tiene una herramienta específica o en qué estado se encuentra.
- Intentos de préstamos de herramientas que no están en stock.
- Falta de un registro centralizado y accesible para la administración.

---

## ✨ Funcionalidades principales

- **Gestión de Herramientas:** Registro detallado (ID, nombre, categoría, stock, estado, valor) y operaciones CRUD.
- **Gestión de Usuarios:** Control de vecinos con roles definidos (Administrador y Usuario).
- **Control de Préstamos:** Verificación automática de disponibilidad, ajuste de stock al prestar y restauración al devolver.
- **Roles y Permisos:** - Administrador: Registra usuarios/herramientas (evitando suplantaciones) y aprueba solicitudes.
  - Usuario: Consulta disponibilidad, consulta solicitudes activas y crea solicitudes de préstamo.
- **Reportes Dinámicos:** Consultas de herramientas con bajo stock, préstamos activos/vencidos, historial por usuario y estadísticas de uso.
- **Auditoría de Eventos (Logs):** Registro persistente de intentos inválidos o errores para el seguimiento administrativo.

---

## 🏗️ Estructura del proyecto

```text
src/
├── G_Usuarios_Admin.py/               # Gestión de usuarios (CRUD de Usuarios)
├── G_Herramientas_Admin.py/           # Gestión de herramientas (CRUD de Usuarios)
├── G_Solicitudes_Admin.py/            # Gestión de solicitudes (Creación,listado y eliminación de Solicitudes)
├── GestionJson.py/                    # Gestión de archivos .Json (Leer, Cargar, Eliminar listas)
├── validaciones.py/                   # Validaciones y roles
├── Menu.py/                           # Menús interactivos y visualización en consola
├── Logs1 y Logs2/                     # Generación de logs (logs.json) y reportes
├── G_herramientas/                    # Lista de diccionarios con el registro de herramientas (G_herramientas.json)
├── G_solicitudes/                     # Lista de diccionarios con el registro de solicitudes (G_solicitudes.json)
├── G_usuarios/                        # Lista de diccionarios con el registro de usuarios (G_usuarios.json) 
└── Main.py                            # Punto de entrada de la aplicación principal

```
---

## 🚀 Cómo ejecutar el proyecto

1. **Clona el repositorio**
   ```bash
   https://github.com/Antony-dev-code/Sistema-de-prestamo-de-herramientas
   ```

2. **Ejecuta el proyecto en python**
   - Buscar el directorio y ejecutar en consola

3. **Ingresar la contraseña para ejecutar el progama de prestamo de herramientas como admin** (opcional)
   - En el apartado de usuario, seleccionar la opción de admin y ingresar la contraseña: 12345.

---

## 🧪 Estado actual

- El proyecto funciona con la finalidad de cumplir los caprichos del docente.
- El programa no posee ningún tipo de seguridad.
- Se está considerando implementar nuevas funciones para futuras versiones, por ejemplo funciones de ordenar usuarios por su color de piel.
