import sympy
from sympy import symbols, Eq, solve


class Calc:
    def __init__(self, function):
        self.x = symbols('x')
        self.b = symbols('b')
        self.f = function
        self.f1 = None
        self.f2 = None
        self.f3 = None
        self.exponenten = None
        self.symmetrie = None
        self.y_achsenabschnitt = None
        self.null_stellen = None
        self.extrem_stellen = None
        self.extrem_punkte = None
        self.wende_stellen = None
        self.wende_punkte = None
        self.tangente = None

    def liest_funktion_ein(self, input_function):
        # bildet die Funktion indem eine liste aus dictionaries
        # durchlaufen wird und die keys und values der funktion hinzugefügt werden
        f = sum(key * self.x ** value for term in input_function for key, value in term.items() if
                value > -1 and type(value) == int)
        self.f = f
        return f

    def gebe_exponenten_zurück(self, function):
        self.exponenten = [value for term in function for value in term.values() if value != 0]
        return self.exponenten

    def bestimme_y_achsenabschnitt(self, input_funktion):
        self.y_achsenabschnitt = input_funktion.subs(self.x, 0)
        return self.y_achsenabschnitt

    def bestimme_symmetrie(self, exponenten):
        gerade_exponenten = [x for x in exponenten if x % 2 == 0]
        ungerade_exponenten = [x for x in exponenten if x % 2 != 0]
        if len(exponenten) == len(gerade_exponenten):
            return "Achsensymmetrisch zur Y-Achse"
        elif len(exponenten) == len(ungerade_exponenten):
            return "Punktsymmetrisch zum Uhrsprung"
        else:
            return "Die Symmetrie kann nicht abgelesen werden"

    def bestimme_grenwertverhalten(self, links, rechts, function):
        if function.subs(self.x, links) > 0 > function.subs(self.x, rechts):
            return "2. in 4.\n" + "x -> +∞ => f(x) -> -∞\n" + "x -> -∞ => f(x) -> +∞"
        elif function.subs(self.x, links) > 0 < function.subs(self.x, rechts):
            return "2. in 1.\n" + "x -> +∞ => f(x) -> +∞\n" + "x -> -∞ => f(x) -> +∞"
        elif function.subs(self.x, links) < 0 > function.subs(self.x, rechts):
            return "3. in 4.\n" + "x -> +∞ => f(x) -> -∞\n" + "x -> -∞ => f(x) -> -∞"
        elif function.subs(self.x, links) < 0 < function.subs(self.x, rechts):
            return "3. in 1.\n" + "x -> +∞ => f(x) -> +∞\n" + "x -> -∞ => f(x) -> -∞"

    def ermittle_nullstellen(self, function):
        # bestimmt die nullstellen von f(x)
        nullPoints = solve(Eq(function, 0))
        # fügt alle reelen nullstellen in dezimal-form in real_nullstellen
        reale_nullstellen = [{nullstelle.evalf(): 0} for nullstelle in nullPoints if nullstelle.is_real]
        self.null_stellen = reale_nullstellen
        return reale_nullstellen

    def ermittle_ableitungen(self, function):
        # etmittelt die 1. Ableitung
        self.f1 = sympy.diff(function, self.x, 1)
        # etmittelt die 2. Ableitung
        self.f2 = sympy.diff(function, self.x, 2)
        # etmittelt die 3. Ableitung
        self.f3 = sympy.diff(function, self.x, 3)
        # etmittelt die 4. Ableitung
        return self.f1, self.f2, self.f3

    def ermittle_extremstellen(self, erste_ableitung, function):
        # stellt die gleichung f'(x) = 0 auf und löst
        xe = solve(Eq(erste_ableitung, 0))
        # fügt alle reelen in dezimal-form in realxe hinzu
        self.extrem_stellen = [x.evalf() for x in xe if x.is_real]
        # bestimmt die y-werte der extremstellen
        self.extrem_punkte = [{x: function.subs(self.x, x)} for x in self.extrem_stellen]
        return self.extrem_punkte

    def prüfe_ob_hoch_oder_tief_punkt(self, x_stelle, zweite_ableitung):
        if zweite_ableitung.subs(self.x, x_stelle) > 0:
            print("Tiefpunkt")
            return "Tiefpunkt"
        else:
            print("Hochpunkt")
            return "Hochpunkt"

    def ermittle_wendestellen(self):
        # stellt die gleichung f''(x) = 0 auf und löst
        xw = solve(Eq(self.f2, 0))
        # fügt alle reelen in dezimal-form in realxe hinzu
        self.wende_stellen = [x.evalf() for x in xw if x.is_real]
        # bestimmt die y-werte der extremstellen
        self.wende_punkte = [{x: self.f.subs(self.x, x)} for x in self.wende_stellen]
        return self.wende_punkte

    def prüfe_ob_hoch_sattelpunkt(self, x_stelle):
        if self.f1.subs(self.x, x_stelle) == 0:
            print("Sattelpunkt")
        else:
            print("Wendepunkt")

    def ermittle_intervale(self, stellen, linke_grenze, rechte_grenze):
        # erstelle eine liste, mit allen werten, die für die Intervale wichtig sind
        interval_liste = [x for x in stellen]
        interval_liste.append(linke_grenze)
        interval_liste.append(rechte_grenze)
        interval_liste = sorted(interval_liste)

        # erstelle die intevale
        interval_dict = [{interval_liste[i]: interval_liste[i + 1]} for i, x in enumerate(interval_liste) if
                         len(interval_liste) > i + 1]
        # die intervale werden durchlaufen und ein mittelwert wird für jedes interval errechnet
        interval_einsetz_werte = [(key + value) / 2 for term in interval_dict for key, value in term.items()]
        # hier wird der mittelwert überprüft, ob die steigend an diesem Mittelwert größer oder kleiner 0 ist
        return interval_dict, interval_einsetz_werte

    def monotonie(self, linke_grenze, rechte_grenze):
        interval_dict, interval_einsetz_werte = self.ermittle_intervale(self.extrem_stellen, linke_grenze,
                                                                        rechte_grenze)
        monotoni = [{x: 'Steigend'} if self.f1.subs(self.x, x) > 0 else {x: 'Falend'} for x in interval_einsetz_werte]
        return interval_dict, monotoni

    def krümmung(self, linke_grenze, rechte_grenze):
        interval_dict, interval_einsetz_werte = self.ermittle_intervale(self.wende_stellen, linke_grenze, rechte_grenze)
        krümmung = [{x: 'Linkskurve'} if self.f2.subs(self.x, x) > 0 else {x: 'Rechtskurve'} for x in
                    interval_einsetz_werte]
        return interval_dict, krümmung

    def bestimme_tangente(self, x_stelle):
        # ermittle die Steigung durch einsetzen in die 1. Ableitung
        m = self.f1.subs(self.x, x_stelle)
        # ermittle die y-koordinate der x stelle
        y = self.f.subs(self.x, x_stelle)
        # löse die formel nach b auf
        b = solve(Eq(m * x_stelle + self.b, y))
        # bilde die tangente
        self.tangente = [m * self.x + x.evalf() for x in b]
        print(self.tangente)
