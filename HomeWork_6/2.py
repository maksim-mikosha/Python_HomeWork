# Самая далекая планета

def find_farthest_orbit(arr): 
    return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])][0]

def calc_square(arr):
    i = 0
    result = 3.14
    while i < len(arr):
        result *= arr[i]
        i += 1
    return result

def main():
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    square = calc_square(find_farthest_orbit(orbits))
    print(f'Самая далекая планета {find_farthest_orbit(orbits)} с площадью {square}')


if __name__ == "__main__":
    main()