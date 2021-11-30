from AstarSearch import *
import matplotlib.pyplot as plt
from matplotlib import image

data = image.imread('map.jpg')

ed = [
    ((1177, 630), (1285, 852)),
    ((1285, 852), (1347, 982)),
    ((1285, 852), (1224, 881)),
    ((1285, 852), (1423, 784)),
    ((1423, 784), (1454, 848)),
    ((1423, 784), (1469, 750)),
    ((1469, 750), (1487, 710)),
    ((1487, 710), (1552, 707)),
    ((1487, 710), (1499, 610)),
    ((1499, 610), (1502, 537)),
    ((1499, 610), (1784, 601)),
    ((1955, 665), (1784, 601)),
    ((1955, 665), (1995, 758)),
    ((1224, 881), (1160, 939)),
    ((1160, 939), (1027, 1004)),
    ((1027, 1004), (1055,1066)),
    ((1055, 1066), (1077,1128)),
    ((1077, 1128), (1083, 1147)),
    ((1083, 1147), (1129, 1180)),
    ((1129, 1180), (1181, 1192)),
    ((1181, 1192), (1233, 1201)),
    ((1233, 1201), (1275, 1244)),
    ((1275, 1244), (1289, 1273)),
    ((1289, 1273), (1311, 1343)),
    ((1027, 1004), (970, 888)),
    ((970, 888), (909, 759)),
    ((909, 759), (868, 679)),
    ((868, 679), (812, 562)),
    ((812, 562), (812, 528)),
    ((812, 528), (868, 489)),
    ((868, 489), (844, 453)),
    ((1027, 1004), (963, 1036)),
    ((963, 1036), (905, 1063)),
    ((905, 1063), (856,1087)),
    ((856,1087), (771, 1138)),
    ((771, 1138), (696,1160)),
    ((696,1160), (620,1189)),
    ((771,1138), (790, 1183)),
    ((790, 1183), (812, 1229)),
    ((856, 1087), (822, 1016)),
    ((822,1016), (776, 925)),
    ((868,679), (710, 767)),
    ((710, 767), (674,712)),
    ((674,712), (590, 755)),
    ((674,712), (643, 661)),
    ((643, 661), (642, 630)),
    ((642, 630), (640, 610)),
    ((640, 610), (662, 597)),
    ((640, 610), (598, 572)),
    ((598, 572), (535, 555)),
    ((535, 555), (512, 529)),
    ((512, 529), (527, 452)),
    ((512, 529), (487, 507)),
    ((487, 507), (384, 533)),
    ((384, 533), (387, 576)),
    ((387, 576), (305, 612)),
    ((305, 612), (254, 616)),
    ((620, 1189), (486, 1252)),
    ((486, 1252), (379, 1257)),
    ((379, 1257), (280, 1207)),
    ((280, 1207), (218, 1110)),
    ((218, 1110), (328, 1050)),
    ((218, 1110), (130, 1149)),
    ((130, 1149), (90, 1187)),
    ((90, 1187), (79, 1286)),
    ((79, 1286), (69,1402)),
    ((130, 1149), (92, 1089)),
    ((92, 1089), (90, 961)),
    ((90, 961), (91, 801)),
    ((91, 801), (98, 770)),
    ((98, 770), (188, 725)),
    ((188, 725), (210,747)),
    ((188, 725), (174,706)),
    ((174,706), (127, 725)),
    ((98, 770), (101, 690)),
    ((101, 690), (134, 652)),
    ((134, 652), (196, 628)),
    ((196,628), (254, 616))
    ]

graph = AstarSearch(ed)

s = (130, 1149)
e = (1469, 750)
ans = graph.searchPath(s, e)
print(ans)
for i in range(1, len(ans)):
    x = [ans[i - 1][0], ans[i][0]]
    y = [ans[i - 1][1], ans[i][1]]
    plt.plot(x, y, color='blue', linewidth=2.0)


plt.imshow(data)
plt.show()






