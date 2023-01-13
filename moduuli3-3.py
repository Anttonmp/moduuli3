sukupuoli = (input)("Mikä sinun sukupuolesi on?:  ")

mies = ("mies")
if sukupuoli == mies:
    m_hemoarvo = int(input("Syötä hemoglobiiniarvosi g/l: "))
if sukupuoli == mies and 133 <= m_hemoarvo <195:
    print("Hemoglobiinisi on normaali. ")
if  sukupuoli == mies and m_hemoarvo >196:
    print("Hemoglobiinisi on korkea. ")
if sukupuoli == mies and m_hemoarvo <133:
    print("Hemoglobiinisi on alhainen")

nainen = ("nainen")
if sukupuoli == nainen:
    n_hemoarvo = int(input("Syötä hemoglobiiniarvosi g/l: "))
if sukupuoli == nainen and 117 <= n_hemoarvo <175:
    print("Hemoglobiinisi on normaali ")
if sukupuoli == nainen and n_hemoarvo >176:
    print("Hemoglobiinisi on korkea. ")
if  sukupuoli == nainen and n_hemoarvo <116:
    print("Hemoglobiinisi on alhainen")

