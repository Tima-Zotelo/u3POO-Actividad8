from zope.interface import Interface
from zope.interface import implementer
from interfaces import IDirector, ITesorero

@implementer(ITesorero)
class Tesorero:
    def gastosSueldoPorEmpleado(self, cuil, lp):
        total = 0
        for a in lp:
            if a.getCuil() == cuil:
                total += a.getSueldoBase()
        return total

@implementer(IDirector)
class Director:
    def modificarBasico(self, cuil, x, lp):
        for a in lp:
            if a.getCuil() == cuil:
                a.setSueldoBasico(x)

    def modificarPorcentajePorCargo(self, cuil, x, lp):
        for a in lp:
            if a.getCuil() == cuil:
                lp.calcularSueldo(a, x)

    def modificarPorcentajePorCategoria(self, cuil, x, lp):
        for a in lp:
            if a.getCuil() == cuil:
                lp.calcularSueldo(a, x)

    def modificarImporteExtra(self, cuil, x, lp):
        for a in lp:
            if a.getCuil() == cuil:
                a.setImporte(a, x)