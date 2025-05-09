G3_ud_edgelist = [  # for rooted tree example
    (0, 2),
    (1, 2),
    (2, 8),
    (3, 6),
    (4, 5),
    (4, 7),
    (4, 11),
    (4, 12),
    (5, 10),
    (6, 7),
    (6, 8),
    (7, 9),
]

G1_ud_edgelist = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
    (6, 5),
    (6, 7),
    (5, 8),
    (7, 8),
    (4, 9),
    (9, 11),
    (5, 10),
    (10, 13),
    (11, 12),
    (11, 13),
    (13, 14),
    (12, 15),
    (15, 18),
    (18, 16),
    (14, 17),
    (17, 18),
    (18, 19),
    (19, 20),
    (20, 21),
    (21, 22),
    (21, 23),
    (22, 23),
]

G2_d_edgelist = [
    (1, 3),
    (1, 5),
    (2, 1),
    (3, 2),
    (3, 4),
    (4, 2),
    (5, 7),
    (6, 5),
    (6, 10),
    (7, 8),
    (8, 6),
    (9, 12),
    (10, 16),
    (11, 13),
    (12, 11),
    (13, 15),
    (14, 12),
    (14, 13),
    (15, 14),
    (15, 21),
    (16, 17),
    (17, 18),
    (18, 17),
    (18, 15),
    (19, 20),
    (20, 21),
    (21, 19),
    (21, 22),
    (22, 23),
    (23, 21),
]


G1_sp = [
    (0, 1, 4),
    (0, 2, 4),
    (0, 3, 6),
    (0, 4, 6),
    (1, 2, 2),
    (2, 3, 8),
    (3, 4, 9),
]

G2_sp = [
    ('a', 'b', 4),
    ('a', 'h', 8),
    ('b', 'c', 8),
    ('b', 'h', 11),
    ('c', 'd', 7),
    ('c', 'f', 4),
    ('c', 'i', 2),
    ('d', 'e', 9),
    ('d', 'f', 14),
    ('e', 'f', 10),
    ('f', 'g', 2),
    ('g', 'i', 6),
    ('h', 'i', 7),
]

T_ud_edgelist = [
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 7),
    (2, 5),
    (3, 6),
    (4, 8),
    (5, 9),
    (5, 10),
    (7, 11),
    (7, 12),
    (8, 13),
    (9, 14),
    (9, 15),
    (11, 16),
    (12, 17),
    (12, 18),
    (14, 19),
    (15, 20),
    (15, 21),
    (16, 22),
    (16, 23),
    (19, 24),
    (19, 25),
    (22, 26),
    (23, 27),
    (23, 28),
    (24, 29),
    (25, 30),
    (27, 31),
]

T_ud_centroid_el = [
    (0, 1),
    (1, 3),
    (1, 4),
    (1, 6),
    (2, 9),
    (3, 8),
    (3, 10),
    (5, 9),
    (6, 7),
    (8, 9),
]

G_d_flow1_el = [
    # (fro, to, cap)
    (0, 1, 10),
    (0, 2, 5),
    (1, 2, 6),
    (1, 3, 5),
    (2, 3, 8)
]

G_d_flow2_el = [
    # (fro, to, cap)
    (0, 1, 10**1000),
    (0, 2, 10**1000),
    (1, 2, 1),
    (1, 3, 10**1000),
    (2, 3, 10**1000)
]

G_d_flow3_el = [
    # (fro, to, cap)
    (0, 1, 10),
    (0, 2, 3),
    (1, 2, 2),
    (1, 3, 4),
    (2, 3, 8)
]

G_d_flow4_el = [
    # CLRS 4th ed, p. 671
    # 0: Vancouver
    # 1: Edmonton
    # 2: Calgary
    # 3: Saskatoon
    # 4: Regina
    # 5: Winnipeg
    (0, 1, 16),
    (0, 2, 13),
    (1, 3, 12),
    (2, 1, 4),
    (2, 4, 14),
    (3, 2, 9),
    (3, 5, 20),
    (4, 3, 7),
    (4, 5, 4),
]

G_ud_matching = (10, [
    (0, 5),
    (0, 6),
    (0, 7),
    (1, 6),
    (2, 8),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 9),
    (4, 6),
    (4, 8),
    (4, 9),
])

G_ud_matching_2 = (10, [
    (0, 5),
    (0, 6),
    (0, 7),
    (2, 6),
    (2, 7),
    (3, 8),
    (3, 9),
    (4, 6),
    (4, 7),
    (4, 9)
])

G_ud_matching_3of4 = (8, [
    (0, 5),
    (1, 5),
    (2, 7),
    (3, 4),
    (3, 6)
])
