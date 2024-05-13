# Currently unused
def average(raw_tr):
    tr_averages = []

    # Parses data into num of executions per microsecond
    for func_tests in raw_tr:
        temp_average = [0, 0, 0, 0, 0] # Milli, deci, centi, second, total
        
        # Sums values in all test_batches for each speed and total average
        for test_batch in func_tests:
            temp_average[0] += test_batch[0] # Millisecond test
            temp_average[1] += test_batch[1] # Decisecond test
            temp_average[2] += test_batch[2] # Centisecond test
            temp_average[3] += test_batch[3] # Second test
            temp_average[4] += sum(test_batch) / 4

        # Averages values in temp_average
        for value in range(len(temp_average)):
            temp_average[value] = temp_average[value] / len(func_tests)

        tr_averages.append(temp_average) 

    return tr_averages

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

raw_data = [[[[1192, 1000700], [12313, 10000500], [121558, 100000800], [1651727, 1000000500]], [[1252, 1000800], [12316, 10000800], [122714, 100000800], [2005788, 1000001300]], [[1374, 1001100], [13541, 10000900], [134810, 100001000], [2009277, 1000000800]], [[1386, 1000700], [13601, 10001100], [134985, 100000700], [1998773, 1000000600]], [[1349, 1000600], [13609, 10000400], [131731, 100001100], [1996100, 1000000400]], [[1386, 1000900], [13544, 10001000], [134309, 100000600], [1978278, 1000000200]], [[960, 1000500], [13052, 10000700], [129299, 100000900], [1965365, 1000000600]], [[1375, 1000700], [13493, 10140500], [128221, 100000600], [1974063, 1000000400]], [[1355, 1000700], [13650, 10000600], [134935, 100000600], [2005427, 1000000500]], [[1395, 1000900], [13504, 10000600], [134438, 100000600], [2010447, 1000000600]], [[1337, 1000500], [13498, 10000500], [135405, 100000900], [2006572, 1000000800]], [[1381, 1000800], [13627, 10000400], [133034, 100001000], [1985867, 1000000500]], [[1388, 1000600], [13620, 10000900], [135140, 100000600], [2004727, 1000000400]], [[1388, 1000900], [13503, 10000700], [135308, 100000700], [2007833, 1000000800]], [[1380, 1000900], [13558, 10001000], [135257, 100000800], [2012547, 1000000400]], [[1384, 1000600], [13621, 10000700], [135468, 100001000], [1979774, 1000000600]], [[1247, 1001200], [13596, 10000800], [135342, 100000900], [1999316, 1000000700]], [[1188, 1000600], [12713, 10000500], [134989, 100000500], [2011266, 1000000600]], [[1382, 1001100], [13512, 10000700], [131830, 100000600], [1993218, 1000000400]], [[1213, 1001000], [13447, 10000600], [135399, 100000500], [2009755, 1000000700]], [[1385, 1001000], [13640, 10000700], [135210, 100000800], [2010996, 1000000700]], [[1377, 1000700], [13652, 10000700], [135356, 100001000], [1995942, 1000000600]], [[1365, 1000800], [13612, 10000700], [133716, 100000800], [2002685, 1000000300]], [[1402, 1000800], [13668, 10000600], [136020, 100000700], [2007886, 1000000700]], [[1368, 1000600], [13429, 10000400], [133061, 100000500], [2012759, 1000000600]], [[1376, 1000600], [13517, 10000800], [134552, 100001000], [1956436, 1000000600]], [[1376, 1001000], [13584, 10055100], [134376, 100000700], [1994726, 1000000400]], [[1382, 1000900], [13618, 10000800], [134448, 100000400], [2004317, 1000000400]], [[1379, 1000700], [13589, 10000700], [122247, 100001400], [2008515, 1000000500]], [[1387, 1000700], [13603, 10000900], [132551, 100001100], [2008019, 1000000800]], [[1375, 1000400], [13525, 10001100], [135466, 100000800], [2009719, 1000000400]], [[1375, 1000700], [13595, 10000700], [134545, 100000400], [2006936, 1000000700]], [[1371, 1000700], [13496, 10000900], [135166, 100000900], [1992828, 1000000400]], [[1372, 1000900], [13597, 10000700], [134301, 100000800], [2005848, 1000000500]], [[1386, 1001000], [13618, 10000900], [132814, 100000900], [1995591, 1000000500]], [[1391, 1001000], [13441, 10001200], [134839, 100010500], [2002989, 1000000800]], [[1379, 1000500], [13611, 10000800], [135382, 100000500], [1992575, 1000000300]], [[1384, 1000500], [13652, 10000900], [135609, 100000900], [2006095, 1000000400]], [[1389, 1000500], [13613, 10001000], [134902, 100000900], [2019712, 1000000600]], [[1384, 1000500], [13656, 10000700], [134661, 100001000], [2006317, 1000000500]], [[1386, 1000400], [13467, 10001100], [135424, 100000800], [2010256, 1000000200]], [[1377, 1000800], [13590, 10001000], [135103, 100000600], [2012889, 1000000600]], [[1391, 1001000], [13594, 10000600], [133264, 100000900], [2010853, 1000000500]], [[1389, 1001000], [13641, 10000500], [135295, 100000400], [1978854, 1000000300]], [[1347, 1000600], [13575, 10000700], [135295, 100001100], [2010648, 1000000300]], [[1389, 1000900], [13540, 10000400], [135487, 100000400], [2005801, 1000000400]], [[1383, 1000900], [13610, 10000800], [135283, 100000500], [2011200, 1000000400]], [[1389, 1000500], [13520, 10000600], [134747, 100000700], [2014593, 1000000300]], [[1370, 1000800], [13593, 10000400], [134409, 100000800], [2000161, 1000000400]], [[1393, 1000400], [13621, 10000800], [134155, 100000600], [2000099, 1000000600]], [[1328, 1001100], [13353, 10000800], [133595, 100000900], [1996715, 1000000400]], [[1360, 1000500], [13557, 10000600], [135004, 100000900], [1989343, 1000000500]], [[1335, 1000500], [13495, 10000700], [134693, 100000900], [1999133, 1000000300]], [[1340, 1001100], [13420, 10000700], [134440, 100000900], [1997814, 1000000400]], [[1359, 1000800], [13601, 10000700], [134610, 100001000], [1993373, 1000000500]], [[1370, 1000600], [13457, 10001100], [134228, 100001000], [1984688, 1000000500]], [[1373, 1000700], [13454, 10000600], [134628, 100000500], [1997925, 1000000600]], [[1384, 1000600], [13524, 10000900], [134625, 100000700], [1997216, 1000000700]], [[1368, 1000800], [13527, 10000500], [134333, 100000600], [1995347, 1000000300]], [[1384, 1002400], [13496, 10000700], [134870, 100000500], [1993563, 1000000500]], [[1379, 1000800], [13588, 10000900], [134482, 100001100], [1994678, 1000000300]], [[1365, 1000600], [13602, 10000900], [135283, 100001000], [1791038, 1000000900]], [[1196, 1001200], [11738, 10000700], [116886, 100000500], [1948398, 1000000600]], [[1391, 1000900], [13534, 10000900], [135298, 100000500], [1979499, 1000000400]], [[1385, 1000800], [13585, 10000800], [135494, 100000800], [2012495, 1000000800]], [[1337, 1000400], [13526, 10000800], [135545, 100001000], [2001988, 1000000600]], [[1382, 1001000], [13675, 10000600], [135656, 100000900], [1937910, 1000000800]], [[1196, 1001100], [11735, 10000600], [119657, 100000800], [1664403, 1000000600]], [[1192, 1000800], [11778, 10001100], [115382, 100001200], [1743803, 1000000900]], [[1266, 1001100], [11576, 10000900], [117611, 100000900], [1980390, 1000000400]], [[1027, 1000600], [11711, 10000800], [132547, 100000900], [1991788, 1000000400]], [[1383, 1000800], [13571, 10000700], [133333, 100000500], [2006865, 1000000800]], [[1379, 1000400], [13476, 10000900], [135657, 100000700], [2013194, 1000000500]], [[1392, 1000700], [13688, 10000800], [134566, 100000600], [2006710, 1000000700]], [[1392, 1001000], [13576, 10000900], [133603, 100000900], [2004825, 1000000400]], [[1374, 1000900], [13601, 10000900], [135242, 100000600], [2010230, 1000000300]], [[1387, 1000500], [13585, 10000600], [131183, 100001000], [2010029, 1000000500]], [[1356, 1001000], [13523, 10000600], [135491, 100001000], [2006476, 1000000700]], [[1366, 1001100], [13574, 10000400], [134934, 100001200], [2015226, 1000000500]], [[1387, 1000500], [13661, 10001000], [136532, 100000500], [2013556, 1000000400]], [[1385, 1000900], [13586, 10000700], [134768, 100000800], [2007930, 1000000300]], [[1385, 1000900], [13542, 10000600], [134926, 100001000], [2016176, 1000000500]], [[1382, 1000600], [13545, 10000700], [135498, 100000800], [2015237, 1000001000]], [[1313, 1000800], [12245, 10000600], [132653, 100000700], [2003391, 1000000400]], [[1379, 1000700], [13648, 10000500], [135467, 100000400], [2005182, 1000000500]], [[1387, 1000600], [13627, 10000700], [135693, 100000600], [1998631, 1000000600]], [[1175, 1000800], [13578, 10000400], [135335, 100000900], [1982820, 1000000400]], [[1384, 1001000], [13561, 10000700], [135605, 100000700], [1982955, 1000000600]], [[1394, 1000900], [13698, 10002100], [135067, 100000500], [1870434, 1000000300]], [[1251, 1000800], [13095, 10000700], [135197, 100000700], [2004716, 1000000800]], [[1378, 1000900], [13560, 10000500], [135482, 100000400], [1995729, 1000000400]], [[1386, 1000500], [13606, 10000600], [135095, 100001000], [2006795, 1000000600]], [[1300, 1000500], [13625, 10000600], [135267, 100000600], [2005415, 1000000400]], [[1369, 1000700], [13617, 10000800], [134933, 100000600], [2014651, 1000000700]], [[1390, 1000500], [13771, 10001100], [136691, 100000500], [2008795, 1000000600]], [[1375, 1000500], [13546, 10000900], [135650, 100001000], [2007093, 1000000600]], [[1383, 1000600], [13658, 10000500], [135211, 100001000], [1997592, 1000000500]], [[1391, 1001100], [13550, 10000400], [135520, 100000700], [1979444, 1000000400]], [[1385, 1000600], [13523, 10001000], [133927, 100000600], [2004440, 1000000600]], [[1321, 1000500], [13578, 10000900], [135292, 100000800], [2010145, 1000000500]]], [[[1253, 1000800], [12358, 10000500], [122895, 100000900], [1797837, 1000000500]], [[1255, 1000800], [12373, 10000700], [123345, 100001000], [1798567, 1000000400]], [[1254, 1000900], [12398, 10000500], [123474, 100000800], [1798409, 1000000200]], [[1235, 1001000], [12453, 10001200], [123421, 100001000], [1798205, 1000000400]], [[1216, 1000900], [12423, 10000800], [123543, 100000800], [1797842, 1000000400]], [[1257, 1001100], [12459, 10001100], [123617, 100000900], [1799369, 1000000400]], [[1257, 1000600], [12205, 10001100], [121031, 100001200], [1784903, 1000000800]], [[1090, 1001000], [10847, 10000900], [122875, 100000400], [1801736, 1000000800]], [[1261, 1000500], [12458, 10001000], [123482, 100000700], [1805242, 1000000300]], [[1261, 1001000], [12479, 10000400], [124048, 100001100], [1802608, 1000000600]], [[1261, 1001000], [12500, 10000600], [122700, 100000800], [1798264, 1000000600]], [[1261, 1000600], [12482, 10000500], [124145, 100001000], [1805887, 1000000700]], [[1251, 1000800], [12489, 10000700], [124074, 100000900], [1804177, 1000000400]], [[1245, 1000700], [12464, 10001100], [124077, 100001200], [1797440, 1000000300]], [[1255, 1001000], [12389, 10000700], [124276, 100000600], [1805712, 1000000600]], [[1239, 1000400], [12501, 10000700], [124385, 100000600], [1802034, 1000000500]], [[1265, 1000800], [12473, 10000800], [123611, 100000600], [1805080, 1000000600]], [[1265, 1000900], [12180, 10000700], [124107, 100001000], [1794932, 1000000400]], [[1248, 1000500], [12466, 10000800], [123572, 100001100], [1800439, 1000000700]], [[1272, 1000700], [12559, 10000900], [124564, 100000500], [1783499, 1000000700]], [[1270, 1000900], [12596, 10000400], [124950, 100001000], [1811661, 1000000600]], [[1269, 1001100], [12515, 10001100], [123802, 100000900], [1809036, 1000000300]], [[1253, 1000500], [12454, 10000700], [124091, 100000500], [1802794, 1000000400]], [[1268, 1000500], [12241, 10000600], [124136, 100000700], [1806057, 1000000600]], [[1248, 1000700], [12459, 10000800], [124054, 100000800], [1799511, 1000000400]], [[1260, 1000800], [12273, 10001100], [121239, 100000600], [1805871, 1000000600]], [[1265, 1000900], [12490, 10001000], [123427, 100000400], [1712264, 1000000500]], [[1263, 1000900], [12502, 10001000], [124215, 100000900], [1802040, 1000000500]], [[1263, 1000500], [12512, 10000400], [123569, 100000600], [1804013, 1000000500]], [[1256, 1001000], [11928, 10000700], [123817, 100000900], [1801489, 1000000500]], [[1262, 1000600], [12497, 10001100], [124249, 100000600], [1803967, 1000000300]], [[1273, 1000800], [12615, 10000900], [125315, 100000500], [1802767, 1000000700]], [[1259, 1001100], [12393, 10000900], [120951, 100001000], [1705253, 1000000600]], [[1263, 1000800], [12442, 10000600], [123514, 100001000], [1803550, 1000000500]], [[1254, 1000600], [12463, 10000500], [123427, 100000500], [1796426, 1000000600]], [[1260, 1001100], [12466, 10000400], [121899, 100001000], [1799795, 1000000400]], [[1228, 1000800], [12511, 10000600], [124253, 100000600], [1800158, 1000000800]], [[1239, 1000500], [12498, 10000700], [123784, 100000800], [1799711, 1000000300]], [[1249, 1000700], [12451, 10000400], [122500, 100000600], [1808958, 1000000800]], [[1256, 1000500], [12470, 10000500], [124260, 100000600], [1791984, 1000000400]], [[1252, 1000700], [12465, 10000900], [124273, 100000500], [1801865, 1000000500]], [[1246, 1000900], [12531, 10000700], [124280, 100000900], [1800608, 1000000300]], [[1242, 1001000], [12531, 10000900], [123899, 100000900], [1806484, 1000000500]], [[1266, 1000500], [12510, 10001000], [124186, 100001000], [1784537, 1000000900]], [[1240, 1000500], [12423, 10000700], [123868, 100000800], [1798542, 1000000500]], [[1256, 1000700], [12460, 10000700], [124385, 100000500], [1788308, 1000000500]], [[1269, 1001200], [12481, 10000900], [124185, 100000900], [1803363, 1000000400]], [[1263, 1000500], [12478, 10000800], [124312, 100000900], [1806065, 1000000500]], [[1265, 1000800], [12474, 10000800], [123453, 100000500], [1801163, 1000000600]], [[1255, 1001000], [12420, 10001000], [123875, 100000900], [1801424, 1000000300]], [[1268, 1000800], [12487, 10000700], [124056, 100000700], [1802289, 1000000700]], [[1264, 1000700], [12514, 10001000], [124245, 100001000], [1775857, 1000000300]], [[1237, 1000600], [12286, 10001000], [124155, 100001200], [1796906, 1000000700]], [[1262, 1000600], [12092, 10001100], [124070, 100000500], [1806472, 1000000300]], [[1263, 1001000], [12483, 10000500], [122935, 100001100], [1803600, 1000000600]], [[1265, 1000900], [12443, 10000500], [124158, 100000800], [1803991, 1000000400]], [[1264, 1000800], [12344, 10000700], [122104, 100000400], [1805523, 1000000500]], [[1262, 1000800], [12447, 10000900], [121861, 100001100], [1799374, 1000000600]], [[1259, 1000700], [12514, 10001100], [123581, 100001100], [1797849, 1000000700]], [[1239, 1001100], [12495, 10000800], [124260, 100000600], [1800230, 1000000300]], [[1258, 1000600], [12477, 10000500], [124021, 100001000], [1805823, 1000000400]], [[1251, 1000800], [12529, 10000700], [124160, 100000400], [1801355, 1000000500]], [[1142, 1001100], [12512, 10000700], [123709, 100000500], [1801818, 1000000700]], [[1215, 1000900], [12440, 10000900], [123195, 100001100], [1794253, 1000000700]], [[1262, 1001200], [12456, 10001000], [121973, 100000700], [1796790, 1000000600]], [[1261, 1000700], [12396, 10000800], [122030, 100000600], [1798569, 1000000900]], [[1245, 1001100], [12468, 10000900], [123398, 100001000], [1787070, 1000000200]], [[1250, 1000800], [12386, 10000400], [123038, 100000500], [1802881, 1000000400]], [[1258, 1000900], [12108, 10000600], [123495, 100001000], [1787946, 1000000300]], [[1263, 1001000], [12450, 10000800], [123626, 100000600], [1798577, 1000000700]], [[1259, 1000900], [12353, 10000500], [123693, 100000600], [1783058, 1000000600]], [[1257, 1000600], [12486, 10000700], [123489, 100000500], [1800863, 1000000700]], [[1248, 1000800], [12427, 10001000], [123752, 100000600], [1802800, 1000000600]], [[1254, 1000800], [12401, 10000500], [122922, 100000500], [1799517, 1000000700]], [[1261, 1001200], [12367, 10000800], [122453, 100000400], [1800294, 1000000800]], [[1205, 1000500], [12350, 10001100], [122150, 100000800], [1724122, 1000020000]], [[796, 1001100], [10416, 10001000], [109687, 100000600], [1651072, 1000000700]], [[1199, 1001100], [12049, 10000600], [122973, 100000700], [1794880, 1000000600]], [[1257, 1000700], [11875, 10000500], [123465, 100000800], [1792301, 1000000600]], [[1254, 1000600], [12396, 10001000], [123608, 100001000], [1796615, 1000000300]], [[1256, 1001100], [12415, 10000500], [122404, 100000600], [1791029, 1000000500]], [[1226, 1000500], [12377, 10001200], [123675, 100000700], [1792449, 1000000500]], [[1252, 1000500], [12430, 10000500], [123345, 100001000], [1795409, 1000000500]], [[1256, 1001200], [12422, 10001000], [123627, 100000900], [1796051, 1000000600]], [[1230, 1000900], [12432, 10000600], [122502, 100001000], [1796600, 1000000600]], [[1258, 1000600], [12338, 10000500], [124365, 100000800], [1782515, 1000000700]], [[1263, 1000800], [12411, 10000800], [123191, 100000800], [1749321, 1000000500]], [[1256, 1000500], [12470, 10001100], [122995, 100000900], [1790138, 1000000500]], [[1236, 1000900], [12389, 10000900], [123178, 100001100], [1787158, 1000000400]], [[1258, 1000700], [12387, 10001000], [123214, 100000600], [1792131, 1000000300]], [[1257, 1000600], [12468, 10000800], [123716, 100000600], [1786306, 1000000400]], [[1255, 1001100], [12390, 10000700], [123504, 100000700], [1784872, 1000000700]], [[1254, 1000900], [12374, 10000700], [123157, 100000900], [1729267, 1000000200]], [[1256, 1000400], [12415, 10000600], [123416, 100001100], [1781126, 1000000600]], [[1259, 1000400], [12394, 10000800], [115660, 100000900], [1796134, 1000000200]], [[1259, 1001100], [12442, 10000600], [123277, 100000500], [1795947, 1000000600]], [[1248, 1000700], [12406, 10000800], [123112, 100001200], [1795215, 1000000600]], [[1257, 1001000], [12366, 10000900], [122860, 100000600], [1797441, 1000000700]], [[1256, 1001100], [12392, 10000800], [123057, 100000800], [1798144, 1000000600]], [[1257, 1000600], [12430, 10000700], [123583, 100001100], [1799293, 1000000700]]], [[[1402, 1001000], [14132, 10000600], [140705, 100002700], [2172215, 1000000300]], [[1446, 1001000], [14232, 10000800], [141766, 100000800], [2186398, 1000000500]], [[1442, 1000500], [14182, 10000800], [141524, 100000600], [2177962, 1000000400]], [[1442, 1000800], [14291, 10000700], [141427, 100000500], [2185166, 1000000500]], [[1440, 1000700], [14159, 10000500], [141396, 100000600], [2182007, 1000000400]], [[1388, 1000500], [14270, 10000500], [141456, 100000500], [2150757, 1000000500]], [[1446, 1000500], [14227, 10000400], [141526, 100000900], [2173710, 1000000700]], [[1446, 1000600], [14177, 10000500], [140377, 100001200], [2182612, 1000000300]], [[1433, 1000900], [14223, 10000700], [141648, 100000900], [2185045, 1000000500]], [[1455, 1000700], [14214, 10001000], [141344, 100000800], [2179150, 1000000600]], [[1449, 1000400], [14198, 10000600], [141668, 100000900], [2182731, 1000000400]], [[1458, 1001000], [14204, 10000400], [141498, 100001100], [2179014, 1000000500]], [[1450, 1000600], [14207, 10001000], [141848, 100001100], [2177721, 1000000500]], [[1452, 1000900], [14289, 10000400], [141504, 100000600], [2170358, 1000000600]], [[1444, 1000500], [14242, 10000400], [141240, 100000800], [2179030, 1000000400]], [[1427, 1001100], [13291, 10000600], [141131, 100000800], [2176792, 1000000500]], [[1451, 1001000], [14154, 10000800], [140930, 100000600], [2184112, 1000000500]], [[1444, 1000800], [14258, 10000900], [141135, 100000500], [2168665, 1000000400]], [[1415, 1001000], [14179, 10000500], [141636, 100001000], [2178287, 1000000300]], [[1455, 1000800], [14248, 10000700], [141152, 100000600], [2185239, 1000000300]], [[1408, 1000400], [14249, 10000400], [139552, 100000500], [2188539, 1000000300]], [[1432, 1000800], [14217, 10000900], [141347, 100000900], [2189985, 1000000400]], [[1444, 1000500], [14201, 10000500], [141885, 100000600], [2187117, 1000000400]], [[1454, 1000700], [14129, 10000800], [141755, 100000800], [2183417, 1000000600]], [[1435, 1000800], [14196, 10000900], [141127, 100000700], [2183302, 1000000400]], [[1444, 1000600], [14159, 10000700], [141089, 100000700], [2171029, 1000000500]], [[1447, 1001000], [14252, 10000700], [140972, 100000900], [2192248, 1000000400]], [[1452, 1000900], [14249, 10000600], [140576, 100001000], [2112582, 1000000700]], [[1450, 1000800], [14228, 10000500], [141572, 100000500], [2157308, 1000000700]], [[1429, 1000600], [14329, 10001000], [142611, 100000400], [2146870, 1000000400]], [[1447, 1001100], [14200, 10000800], [141332, 100000500], [2188315, 1000000500]], [[1440, 1000800], [14160, 10000500], [141628, 100000700], [2178621, 1000000500]], [[1444, 1000500], [14214, 10001000], [141901, 100000400], [2182882, 1000000500]], [[1436, 1000900], [14258, 10001000], [141021, 100000700], [2156207, 1000000400]], [[1441, 1000600], [14259, 10001000], [141534, 100000700], [2180849, 1000000600]], [[1425, 1000500], [14243, 10000800], [141584, 100000900], [2182077, 1000000400]], [[1441, 1000500], [14198, 10000400], [139922, 100001100], [2183454, 1000000400]], [[1421, 1000500], [14001, 10000800], [140878, 100000600], [2190298, 1000000500]], [[1431, 1000600], [14229, 10000700], [141606, 100000900], [2177747, 1000000600]], [[1447, 1000400], [14170, 10000800], [140895, 100000700], [2186111, 1000000300]], [[1452, 1000900], [14216, 10000900], [141880, 100000600], [2187048, 1000000400]], [[1450, 1000900], [14207, 10000400], [141856, 100000600], [2185533, 1000000300]], [[1452, 1000500], [14119, 10000600], [141606, 100000500], [2178749, 1000000300]], [[1390, 1000500], [14299, 10000900], [141674, 100000500], [2185705, 1000000600]], [[1451, 1000400], [14208, 10000500], [141285, 100000800], [2178422, 1000000500]], [[1428, 1000700], [14251, 10000600], [141743, 100001000], [2180301, 1000000300]], [[1424, 1001000], [14278, 10000500], [141642, 100000600], [2197058, 1000000600]], [[1448, 1001000], [14356, 10002500], [140751, 100000600], [2184263, 1000000700]], [[1424, 1000400], [14206, 10000800], [141802, 100000500], [2185219, 1000000400]], [[1429, 1000900], [14220, 10000600], [141754, 100000700], [2189964, 1000000500]], [[1444, 1000900], [14273, 10000500], [141914, 100000800], [2182746, 1000000400]], [[1437, 1000900], [14269, 10000500], [141876, 100000700], [2189221, 1000000400]], [[1430, 1001100], [14171, 10000900], [141988, 100000600], [2182159, 1000000600]], [[1454, 1000900], [14212, 10000700], [141885, 100000500], [2185618, 1000000600]], [[1434, 1000800], [14223, 10000900], [141506, 100001100], [2187778, 1000000500]], [[1447, 1000600], [14200, 10000800], [141926, 100001000], [2187989, 1000000400]], [[1441, 1000500], [14147, 10001000], [140741, 100001200], [2182789, 1000000200]], [[1430, 1000800], [13234, 10000700], [141462, 100000900], [2187719, 1000000400]], [[1433, 1000700], [14179, 10029100], [141370, 100000900], [2181911, 1000000700]], [[1435, 1000800], [14229, 10000600], [141697, 100000800], [2149706, 1000000500]], [[1443, 1000500], [14200, 10000600], [140660, 100001100], [2061888, 1000000300]], [[1452, 1000500], [14222, 10001000], [141366, 100000700], [2165531, 1000000500]], [[1446, 1000700], [14275, 10001000], [141710, 100000400], [2185618, 1000000300]], [[1429, 1000800], [14239, 10000900], [141221, 100000600], [2180704, 1000000500]], [[1452, 1000500], [14250, 10001000], [138744, 100000500], [2189414, 1000000500]], [[1453, 1000600], [14252, 10000700], [141908, 100000500], [2189059, 1000000500]], [[1454, 1000600], [14282, 10000900], [140740, 100000500], [2186528, 1000000600]], [[1442, 1000800], [13509, 10000500], [141237, 100000800], [2187925, 1000000400]], [[1441, 1000500], [14161, 10001000], [141445, 100000700], [2188460, 1000000600]], [[1394, 1000700], [14209, 10000700], [141291, 100001100], [2184701, 1000000600]], [[1450, 1000400], [14200, 10000800], [141809, 100000600], [2183374, 1000000300]], [[1441, 1000900], [14239, 10000500], [141784, 100000600], [2183976, 1000000400]], [[1446, 1000500], [14143, 10001000], [140176, 100000600], [2174390, 1000000500]], [[1424, 1000700], [14168, 10001000], [139909, 100000900], [2165616, 1000000500]], [[1443, 1000500], [14215, 10000900], [141644, 100000700], [2184019, 1000000400]], [[1455, 1000600], [14207, 10000900], [141549, 100000800], [2189326, 1000000400]], [[1412, 1000600], [14015, 10000600], [138130, 100000600], [2187816, 1000000300]], [[1390, 1000600], [14130, 10000700], [140422, 100000600], [2190728, 1000000700]], [[1457, 1000800], [14215, 10000800], [140627, 100000500], [2190134, 1000000500]], [[1437, 1001100], [14071, 10000500], [141773, 100000900], [2181467, 1000001300]], [[1440, 1001000], [14137, 10000900], [141709, 100000600], [2180958, 1000000200]], [[1439, 1000700], [14206, 10000500], [141787, 100001100], [2157447, 1000000700]], [[1421, 1000500], [13976, 10000400], [140308, 100000700], [2180918, 1000000600]], [[1444, 1000600], [14177, 10000600], [141727, 100001000], [2161530, 1000000500]], [[1439, 1001000], [14197, 10000800], [141610, 100001000], [2173110, 1000000400]], [[1449, 1001000], [14159, 10000900], [141799, 100000800], [2057313, 1000000800]], [[1240, 1000700], [12286, 10001100], [123175, 100001400], [2186344, 1000000300]], [[1445, 1000700], [14180, 10000800], [141452, 100000900], [2183291, 1000000200]], [[1424, 1000400], [14240, 10000900], [139148, 100000800], [2172696, 1000000600]], [[1439, 1000700], [14147, 10001000], [140984, 100000500], [2182470, 1000000400]], [[1408, 1001100], [14148, 10000900], [141663, 100000800], [2186746, 1000000600]], [[1453, 1000700], [14175, 10000900], [141148, 100001100], [2200305, 1000000200]], [[1435, 1001000], [14240, 10000500], [141592, 100000500], [2187975, 1000000500]], [[1440, 1001000], [14232, 10000800], [139862, 100000900], [2187201, 1000000300]], [[1451, 1000500], [14221, 10001000], [141758, 100001000], [2187985, 1000000400]], [[1444, 1000600], [14219, 10000800], [142017, 100000700], [2198799, 1000000600]], [[1424, 1001000], [14215, 10000500], [141290, 100000500], [2193053, 1000000800]], [[1441, 1001000], [14152, 10000700], [141988, 100000400], [2186335, 1000000300]], [[1437, 1000500], [14256, 10000900], [139569, 100000500], [2187059, 1000000700]], [[1451, 1001000], [14175, 10000500], [140669, 100000900], [2182798, 1000000800]]], [[[1267, 1001100], [13327, 10001000], [135444, 100000700], [2045510, 1000000300]], [[1296, 1000900], [13561, 10000500], [134687, 100000800], [2042582, 1000000500]], [[1380, 1001000], [13634, 10000800], [135792, 100001000], [2044876, 1000000300]], [[1382, 1000600], [13591, 10000500], [135996, 100001000], [2040306, 1000000600]], [[1373, 1000500], [13569, 10001100], [135493, 100000800], [2037933, 1000000500]], [[1390, 1000900], [13642, 10001100], [135660, 100000900], [2035283, 1000000900]], [[1359, 1000800], [13664, 10000900], [134974, 100000800], [2045214, 1000000600]], [[1364, 1000700], [13648, 10001000], [135507, 100000600], [2046928, 1000000300]], [[1368, 1000400], [13552, 10000700], [135516, 100000700], [2046884, 1000000600]], [[1365, 1000900], [13615, 10000900], [134831, 100000500], [2047849, 1000000600]], [[1375, 1000600], [13472, 10000600], [132982, 100000500], [2041626, 1000000600]], [[1363, 1000900], [13591, 10000700], [135347, 100000500], [2043259, 1000000300]], [[1362, 1000500], [13546, 10000800], [135369, 100000400], [2036762, 1000000900]], [[1347, 1001200], [13652, 10000500], [134564, 100001300], [1926279, 1000000400]], [[1387, 1001000], [12834, 10000900], [133603, 100000700], [2006190, 1000000700]], [[1387, 1000500], [13632, 10000500], [133551, 100000800], [2027229, 1000000500]], [[1369, 1000700], [13584, 10000600], [133955, 100000700], [2039243, 1000000200]], [[1384, 1001100], [13597, 10001000], [135562, 100000400], [2045299, 1000000900]], [[1379, 1000900], [13601, 10000600], [135533, 100000800], [2042640, 1000000300]], [[1360, 1000900], [13608, 10000800], [135083, 100000800], [2039300, 1000000600]], [[1382, 1000700], [13631, 10000800], [135036, 100001000], [2057370, 1000000500]], [[1389, 1000700], [13516, 10000900], [135633, 100000600], [2041198, 1000000500]], [[1380, 1000500], [13590, 10000900], [135001, 100000700], [2030883, 1000000400]], [[1387, 1000600], [13584, 10000400], [135381, 100000600], [2039243, 1000000300]], [[1384, 1000900], [13620, 10000800], [135081, 100001000], [2041771, 1000000700]], [[1327, 1000700], [13617, 10000500], [135001, 100000800], [2033294, 1000000600]], [[1381, 1000500], [13562, 10001100], [135253, 100000600], [2046295, 1000000800]], [[1393, 1000600], [13673, 10000800], [136510, 100000900], [2047322, 1000000500]], [[1376, 1000900], [13665, 10000600], [133700, 100001100], [2034581, 1000000400]], [[1360, 1000500], [13533, 10000700], [135338, 100000400], [2038288, 1000000400]], [[1374, 1000400], [13671, 10000500], [134832, 100001100], [2044792, 1000000800]], [[1382, 1000600], [13117, 10001000], [134119, 100000800], [2037950, 1000000600]], [[1370, 1001000], [13643, 10000600], [135595, 100000400], [2036304, 1000000700]], [[1321, 1000900], [13648, 10000700], [135587, 100000700], [2037446, 1000000300]], [[1367, 1000500], [13522, 10000600], [135469, 100001000], [2045611, 1000000700]], [[1386, 1000600], [13454, 10001100], [134917, 100001100], [2048790, 1000000300]], [[1391, 1000400], [12976, 10001100], [135481, 100000500], [2041850, 1000000700]], [[1386, 1000600], [13716, 10001100], [135432, 100000500], [2020271, 1000000400]], [[1373, 1000700], [13615, 10001000], [135426, 100000600], [2043838, 1000000600]], [[1385, 1000400], [13779, 10000800], [136322, 100000500], [2036077, 1000000300]], [[1365, 1000900], [13435, 10000800], [129806, 100000900], [2029574, 1000000400]], [[1383, 1001000], [13468, 10000700], [135386, 100000900], [2036415, 1000000600]], [[1386, 1000800], [13634, 10000500], [135567, 100000400], [2033256, 1000000300]], [[1373, 1001100], [13615, 10000700], [135188, 100000900], [2042121, 1000000400]], [[1377, 1000700], [13646, 10000500], [135690, 100000600], [2028376, 1000001000]], [[1385, 1000700], [13662, 10000900], [134983, 100000800], [2037852, 1000000800]], [[1380, 1000500], [13635, 10000500], [135420, 100000700], [2037641, 1000000700]], [[1368, 1000500], [13497, 10000500], [135285, 100001100], [2038705, 1000000300]], [[1378, 1000800], [13511, 10001100], [135686, 100000900], [2038654, 1000000500]], [[1375, 1000500], [13616, 10001000], [135485, 100000600], [2043603, 1000000200]], [[1367, 1001000], [13025, 10000900], [135124, 100000500], [2034184, 1000000200]], [[1385, 1000600], [12665, 10000500], [135661, 100000800], [2033253, 1000000200]], [[1359, 1000700], [13631, 10001100], [135506, 100000800], [2037593, 1000000400]], [[1383, 1000500], [13623, 10001100], [135521, 100001000], [2040439, 1000000500]], [[1340, 1000500], [13584, 10000600], [135547, 100000600], [2034443, 1000000400]], [[1367, 1000900], [13554, 10000400], [134375, 100000900], [2037964, 1000000200]], [[1375, 1000500], [13471, 10000500], [135729, 100000400], [2039013, 1000000400]], [[1370, 1000400], [13656, 10000800], [133268, 100000400], [2035971, 1000000300]], [[1380, 1000700], [13612, 10000600], [135380, 100000600], [2035844, 1000000400]], [[1340, 1000700], [13652, 10000800], [135455, 100000700], [2026453, 1000000700]], [[1336, 1001000], [13384, 10000600], [134645, 100000600], [2037531, 1000000600]], [[1386, 1000500], [13523, 10000700], [135020, 100000700], [2039035, 1000000500]], [[1313, 1001100], [13568, 10000400], [135148, 100000600], [2044004, 1000000500]], [[1393, 1001000], [13593, 10000800], [135511, 100000500], [2039842, 1000000400]], [[1378, 1000600], [13604, 10000500], [135615, 100001000], [2038436, 1000000600]], [[1382, 1000500], [13556, 10000700], [134208, 100001100], [2038381, 1000000400]], [[1346, 1000500], [13442, 10000900], [135775, 100000800], [2044793, 1000000300]], [[1357, 1000600], [13516, 10000600], [135237, 100001000], [1996523, 1000000500]], [[1376, 1000500], [13595, 10000900], [134971, 100001100], [2034291, 1000000700]], [[1379, 1000700], [13607, 10001000], [135461, 100000800], [2043820, 1000000700]], [[1383, 1000800], [13680, 10000600], [135434, 100000700], [2042106, 1000000400]], [[1373, 1001000], [13586, 10000700], [135283, 100001100], [2041131, 1000000600]], [[1390, 1000800], [13564, 10000700], [135326, 100000900], [2044301, 1000000500]], [[1362, 1000500], [13590, 10000500], [133842, 100001100], [2038839, 1000000500]], [[1349, 1001100], [13665, 10000900], [133412, 100000800], [2042605, 1000000400]], [[1367, 1001100], [13618, 10000900], [134413, 100001600], [2042077, 1000000600]], [[1384, 1000400], [13543, 10000600], [135314, 100000800], [2040359, 1000000300]], [[1394, 1000500], [13582, 10000600], [123218, 100000700], [2032651, 1000000600]], [[1378, 1000900], [13579, 10000500], [135641, 100000900], [2037260, 1000000300]], [[1361, 1001000], [13582, 10000600], [135487, 100000400], [2038554, 1000000400]], [[1379, 1000800], [13631, 10000500], [135237, 100001100], [2031022, 1000000800]], [[1377, 1001000], [13427, 10000700], [133720, 100001000], [2016119, 1000000800]], [[1378, 1000800], [13537, 10000800], [134691, 100000500], [2039632, 1000000400]], [[1389, 1000600], [13273, 10000700], [135349, 100001100], [2037009, 1000000500]], [[1392, 1001000], [13590, 10000900], [135614, 100000900], [2040466, 1000000300]], [[1375, 1000600], [13661, 10001000], [133698, 100001000], [2039763, 1000000200]], [[1384, 1000800], [13607, 10000700], [135471, 100000500], [2029854, 1000000400]], [[1380, 1000500], [13575, 10000500], [135423, 100000600], [2032373, 1000000500]], [[1379, 1000600], [13597, 10000700], [135687, 100000600], [2038937, 1000000500]], [[1383, 1000800], [13620, 10001000], [134750, 100000600], [2041250, 1000000400]], [[1315, 1000800], [13625, 10000900], [135638, 100000500], [2040723, 1000000400]], [[1388, 1000600], [13571, 10000400], [135120, 100000500], [2043852, 1000000600]], [[1384, 1000600], [13599, 10000700], [135351, 100000500], [2039293, 1000000300]], [[1347, 1000400], [13563, 10000600], [135282, 100000500], [2043027, 1000000700]], [[1378, 1001000], [13568, 10000600], [135625, 100000900], [2042901, 1000000200]], [[1369, 1001000], [13598, 10000500], [132796, 100000600], [2040515, 1000000400]], [[1380, 1000400], [13462, 10000700], [134364, 100000700], [2042792, 1000000900]], [[1375, 1000500], [13667, 10001000], [135901, 100000700], [2046071, 1000000600]], [[1383, 1001100], [13655, 10000800], [135461, 100000600], [2043714, 1000000500]], [[1368, 1001000], [13621, 10000500], [135176, 100000800], [2044475, 1000000700]]]]

def seperate_data(raw_tr):
    perlin_2D = []
    perlin_3D = []
    simplex_2D = []
    simplex_3D = []

    for test_batch in raw_tr[0]:
        for test in test_batch:
            perlin_2D.append(test)
    for test_batch in raw_tr[1]:
        for test in test_batch:
            perlin_3D.append(test)
    for test_batch in raw_tr[2]:
        for test in test_batch:
            simplex_2D.append(test)
    for test_batch in raw_tr[3]:
        for test in test_batch:
            simplex_3D.append(test)

    # Seperates into executions and time
    perlin_2D = [[test[0] for test in perlin_2D], [test[1] for test in perlin_2D]]
    perlin_3D = [[test[0] for test in perlin_3D], [test[1] for test in perlin_3D]]
    simplex_2D = [[test[0] for test in simplex_2D], [test[1] for test in simplex_2D]]
    simplex_3D = [[test[0] for test in simplex_3D], [test[1] for test in simplex_3D]]

    return perlin_2D, perlin_3D, simplex_2D, simplex_3D

perlin_2D, perlin_3D, simplex_2D, simplex_3D = seperate_data(raw_data)

fig = plt.figure(1)
plt.title("Executions over Time", fontsize="16")

# Perlin 2D
plt.scatter(perlin_2D[0], perlin_2D[1], color="red")
z = np.polyfit(perlin_2D[0], perlin_2D[1], 1) # Trendline
p = np.poly1d(z)
plt.plot(perlin_2D[0], p(perlin_2D[0]),"r-")

# Perlin 2D
plt.scatter(perlin_3D[0], perlin_3D[1], color="blue")
z = np.polyfit(perlin_3D[0], perlin_3D[1], 1) # Trendline
p = np.poly1d(z)
plt.plot(perlin_3D[0], p(perlin_3D[0]),"b-")

# Simplex 2D
plt.scatter(simplex_2D[0], simplex_2D[1], color="green")
z = np.polyfit(simplex_2D[0], simplex_2D[1], 1) # Trendline
p = np.poly1d(z)
plt.plot(simplex_2D[0], p(simplex_2D[0]),"g-")

# Simplex 3D
plt.scatter(simplex_3D[0], simplex_3D[1], color="black")
z = np.polyfit(simplex_3D[0], simplex_3D[1], 1) # Trendline
p = np.poly1d(z)
plt.plot(simplex_3D[0], p(simplex_3D[0]),"k-")

#"P2D Red\nP3D Blue\nS2D Yellow\nS3D Green"
plt.legend(["P2D Red", "P3D Blue", "S2D Green", "S3D Black"])

plt.xlabel("Time",fontsize="13")
plt.ylabel("Executions",fontsize="13")
plt.savefig("fig_1_(400 exec's per func).svg")
plt.grid()
plt.show()