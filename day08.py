from day01 import read_input
from day06 import product
import numpy as np
import itertools

def generate_boxes(lines):
    for i in range(len(lines)):
        lines[i] = tuple(map(int, lines[i].split(",")))
    return lines

def distance(c1,c2):
    return np.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

def main():
    lines = read_input('08')[:-1]
    box_coords = generate_boxes(lines)
    pairs = itertools.combinations(box_coords, 2)
    distance_map = dict()
    for p in pairs:
        distance_map[p] = distance(p[0], p[1])
    distance_map = {k: v for k, v in sorted(distance_map.items(), key = lambda item: item[1])}
    circuits = [{i} for i in box_coords]
    count = 0
    print(len(circuits))
    for pair in distance_map.keys():
        count+=1
        circuits_to_merge = []
        for circuit in circuits:
            if pair[0] in circuit or pair[1] in circuit:
                circuits_to_merge.append(circuit)
        new_circuit = set(pair).union(*circuits_to_merge)
        for circuit in circuits_to_merge:
            circuits.remove(circuit)
        circuits.append(new_circuit)
        if count == 1000:
            sorted_circuits = sorted(circuits, key=len, reverse=True)
            print(product([len(l) for l in sorted_circuits[:3]]))
        if len(circuits) == 1:
            print(pair[0][0]*pair[1][0])
            break



if __name__ == '__main__':
    main()
