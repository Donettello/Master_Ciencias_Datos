# Listas iniciales
p_starts = [1, 3, 6]
p_peaks = [0, 4, 8]
p_ends = [2, 5, 7]

# Combina y reorganiza los índices
values = sorted(p_starts + p_peaks + p_ends)
p_starts_sorted = values[0::3]  # Toma los valores en las posiciones 0, 3, 6, ...
p_peaks_sorted = values[1::3]  # Toma los valores en las posiciones 1, 4, 7, ...
p_ends_sorted = values[2::3]   # Toma los valores en las posiciones 2, 5, 8, ...

print("p_starts:", p_starts_sorted)
print("p_peaks:", p_peaks_sorted)
print("p_ends:", p_ends_sorted)