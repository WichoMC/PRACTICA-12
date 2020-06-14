#include<stdio.h>
#include "ejercicio.h"
#include <string.h>

int main(){
    LIST *lista;
    INFO info;
    strcpy(info.nombre, "nombre1");
    strcpy(info.apellido, "apellido11 apellido12");

    lista = crear_lista();
    insertar(info,lista);
    imprimir(lista);
    eliminar(lista);
    return 0;
}
