from py3dbp_ import Packer, Item, Bin

FACTOR = 100  # metros → centímetros

def optimizar_carga(camion, items):
    packer = Packer()

    box = Bin(
        partno=camion.placa,
        WHD=(
            int(camion.ancho * FACTOR),
            int(camion.alto * FACTOR),
            int(camion.largo * FACTOR)
        ),
        max_weight=camion.capacidad_kg,
        corner=0,
        put_type=1
    )
    packer.addBin(box)

    # Expandir cantidades y ordenar por peso DESC
    items_expandidos = []
    for item in items:
        for i in range(item.cantidad):
            items_expandidos.append({
                "partno": f"{item.nombre}_{i+1}",
                "nombre": item.nombre,
                "WHD": (
                    int(item.ancho * FACTOR),
                    int(item.alto * FACTOR),
                    int(item.largo * FACTOR)
                ),
                "peso": item.peso,
                # guardamos originales para el response
                "ancho": item.ancho,
                "alto": item.alto,
                "largo": item.largo,
            })

    items_expandidos.sort(key=lambda x: x["peso"], reverse=True)

    for it in items_expandidos:
        packer.addItem(Item(
            partno=it["partno"],
            name=it["nombre"],
            typeof='cube',
            WHD=it["WHD"],
            weight=it["peso"],
            level=1,
            loadbear=999,
            updown=True,
            color='#5b8dd9'
        ))

    packer.pack(
        bigger_first=True,
        fix_point=True,
        distribute_items=False,
        check_stable=False,
        support_surface_ratio=0.75,
        number_of_decimals=0
    )

    resultados = []
    for item in packer.bins[0].items:
        nombre_base = item.partno.rsplit("_", 1)[0]
        resultados.append({
            "nombre": nombre_base,
            "largo": item.getDimension()[2] / FACTOR,
            "ancho": item.getDimension()[0] / FACTOR,
            "alto": item.getDimension()[1] / FACTOR,
            "peso": item.weight,
            "cantidad": 1,
            "pos_x": item.position[2] / FACTOR,
            "pos_y": item.position[1] / FACTOR,
            "pos_z": item.position[0] / FACTOR,
        })

    no_caben = [item.partno.rsplit("_", 1)[0] for item in packer.bins[0].unfitted_items]

    return resultados, no_caben