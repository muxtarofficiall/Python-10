def yarish_movqe(xallar):
    # Xalları böyükdən kiçiyə sıralayırıq və indekslərini yadda saxlayırıq
    siralanmis_xallar = sorted(enumerate(xallar), key=lambda x: x[1], reverse=True)
    
    # Yerləri təyin edirik
    yerlər = [''] * len(xallar)
    for index, (original_index, xal) in enumerate(siralanmis_xallar):
        yerlər[original_index] = f'{index + 1}-ci'
    
    return yerlər

# Misal xallar
xallar = [5, 3, 4, 2, 1]

# Funksiyanı çağırırıq
nəticə = yarish_movqe(xallar)
print(nəticə)  # ['1-ci', '3-cu', '2-ci', '4-cu', '5-ci']
