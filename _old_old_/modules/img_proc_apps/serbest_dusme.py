import math

def faydali_yuk_mesafe(altitude, airspeed, payload_mass_grams):
    # Gram cinsinden payload massi
    payload_mass_grams = payload_mass_grams / 1000
    
    # Yerçekimi ivmesi
    g = 9.81

    # Düşme süresini hesaplayın
    t = math.sqrt(2 * altitude / g)

    # Düşme mesafesini hesaplayın
    d = airspeed * t

    # Faydalı yükün düştüğü mesafeyi hesaplayın
    fd = d - (0.5 * g * t ** 2)

    # Sonucu döndürün
    return fd

print(faydali_yuk_mesafe(altitude=10, airspeed=10, payload_mass_grams=50))


