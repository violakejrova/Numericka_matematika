
## Diskretizace funkce

- rozdělení intervalu (0,1) na N podintervalů
- Thomasův algoritmus (LU rozklad pro tridiagonální matice, bez explicitního ukládání L a U)
- forward eliminace:
  - redukce dolní diagonály na nulu
  - úprava hlavní diagonály a pravé strany, aby mohla následovat zpětná substituce
- zpětná substituce:
  - poslední prvek je `d[-1] / hlav_diag[-1]`
  - ostatní dopočítá přes horní diagonálu a modifikovanou hlavní diagonálu
- nakonec se do řešení přidají okrajové podmínky

## Iterační metody

Pro velké a řídké matice:

- **Jacobiho metoda**
  - používá pouze hodnoty z předchozí iterace

$$
u_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} u_j^{(k)} \right)
$$

- **Gauss-Seidelova metoda**
  - okamžitě využívá již spočítané hodnoty

$$
u_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} u_j^{(k+1)} - \sum_{j > i} a_{ij} u_j^{(k)} \right)
$$

Díky tomu Gauss-Seidel konverguje **rychleji** než Jacobi při stejné matici.

## Vlastní čísla

- Používají se (v tomto repozitáři) při:
  
    - Výpočtu spektrálního poloměru  $$(ρ(A) = max |λ_i|)$$
    - Výpočtu 2-normy matice  $$(||A||_2 = sqrt(λ_max(A^T A)))$$
### QR metoda

 1. Provede se QR rozklad matice: A_k = Q_k R_k.
 2. Vytvoří se nová matice: A_{k+1} = R_k Q_k.
 3. Opakuje se iterace, dokud se matice nestane horní trojúhelníkovou.
 4. Vlastní čísla matice A se získají z diagonály výsledné matice


## Normy
### Vektorové normy

- 1-norma: součet absolutních hodnot složek vektoru.
- 2-norma: odmocnina ze součtu čtverců složek vektoru (Eukleidovská norma).
- ∞-norma: největší absolutní hodnota ze složek vektoru.

### Maticové normy

- 1-norma matice: největší součet absolutních hodnot ve sloupcích.
- ∞-norma matice: největší součet absolutních hodnot v řádcích.
- 2-norma matice: spektrální norma je založena na největším vlastním čísle matice (A^T * A).

> V úloze QR_elipsoid se normy využily k výpočtu ...

## Doplňkové kódy

- Newtonova metoda
  - pro výpočet kořenu funkce
