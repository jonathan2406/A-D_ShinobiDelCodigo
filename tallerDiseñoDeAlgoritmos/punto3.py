# punto 3
# pasa casi todas las pruebas pero al ser recursivo las pruebas que son muy grandes se muere
# este codigo se realizo cogiendo la idea de varias soluciones de comentarios de la pagina e implementandolo recursivamente

class Solution:
    def minDifference(self,nums, n):
        total = sum(nums)
        return self.candela(nums, n - 1, total, total, 0)
    
    def candela(self, nums, idx, suma_izquierda, suma_derecha, diferencia):
        if idx < 0:
            return abs(suma_izquierda - suma_derecha)
        
        diferencia1 = self.candela(nums, idx - 1, suma_izquierda - nums[idx], suma_derecha, diferencia)
        diferencia2 = self.candela(nums, idx - 1, suma_izquierda, suma_derecha - nums[idx], diferencia)
        
        return min(diferencia1, diferencia2)