from zope.interface import Interface, implementer

class ITesorero(Interface):
    def gastosSueldoPorEmpleado(dni):
        pass

class IDirector(Interface):
    def modificarBasico(dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(dni, nuevoImporteExtra):
        pass