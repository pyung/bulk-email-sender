import csv
import itertools

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

results = []
with open("py_slack.csv") as csvfile:
    files = csv.reader(csvfile)
    for o in files:
        if len(o) > 2:
            if o[2] != "Deactivated":
                results.append(o[1])
                # print(o[1])
for x, o in enumerate(grouper(200,results)):
    print(",".join([i for i in o if i]))
    print(x)
    # print(grouper(20,results))
# with open("eggs.csv", "w", newline="") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=",")
#     for r in results:
#         spamwriter.writerow(r)
