from py3dbp import Packer, Item,Bin



def optimizar_carga(camion, items):
    packer = Packer()

    packer.add_bin(Bin(
        name=camion.placa,
        width=camion.ancho,
        height=camion.alto,
        depth=camion.largo,
        max_weight=camion.capacidad_kg
    ))


    for item in items:

        for i in range(item.cantidad):
            packer.add_item(Item(
                name=f"{item.nombre}_{i}",
                width=item.ancho,
                height=item.alto,
                depth= item.largo,
                weight= item.peso
            ))

    packer.pack()
    resultados=[]
    for item in packer.bins[0].items:
        nombre_base = item.name.rsplit("_", 1)[0]
        resultados.append({
            "nombre": nombre_base,
            "largo": item.depth,
            "ancho": item.width,
            "alto": item.height,
            "peso": item.weight,
            "cantidad": 1,  # cada registro es una instancia individual
            "pos_x": item.position[2],
            "pos_y": item.position[1],
            "pos_z": item.position[0]
        })

    no_caben = [item.name.rsplit("_", 1)[0] for item in packer.unfit_items]

    return resultados, no_caben