{"changed":true,"filter":false,"title":"jacobi.py","tooltip":"/scripts/jacobi.py","value":"import helpers as hp\nimport numpy as np\nfrom sys import argv\n\nscript, filename = argv\n\ntxt = open(filename)\n\nheader = txt.readline().split()\ninputArray = map(float, txt.readline().split())\ntxt.close()\n\ninputMat = np.mat(inputArray)\ninputMat.reshape(int(header[0]), int(header[1]))\ninputMat.shape()\n\n#takes q3data as input\ndef jacobi(A,b,N=25,x=None):\n    \n    # Create an initial guess if needed\n    if x is None:\n        x = np.zeros(len(A[0]))\n\n    # Create a vector of the diagonal elements of A\n    # and subtract them from A\n    D = np.diag(A)\n    R = A - np.diagflat(D)\n\n    # Iterate for N times\n    for i in range(N):\n        x = (b - np.dot(R,x)) / D\n    return x\n\nb = np.array([11.0,13.0])\nguess = np.array([1.0,1.0])\n\nprint(jacobi(inputMat,b,N=25,x=guess))","undoManager":{"mark":-27,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["y"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":14},"end":{"row":0,"column":20},"action":"insert","lines":[" as hp"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":9},"end":{"row":27,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":3},"end":{"row":28,"column":4},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["S"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":8},"end":{"row":28,"column":9},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":9},"end":{"row":28,"column":10},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":10},"end":{"row":28,"column":11},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":11},"end":{"row":28,"column":12},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["j"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":16},"end":{"row":28,"column":17},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["k"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["q"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":1,"column":18},"action":"remove","lines":["import numpy as np"]},{"start":{"row":1,"column":0},"end":{"row":14,"column":16},"action":"insert","lines":["import numpy as np","from sys import argv","","script, filename = argv","","txt = open(filename)","","header = txt.readline().split()","inputArray = map(float, txt.readline().split())","txt.close()","","inputMat = np.mat(inputArray)","inputMat.reshape(int(header[0]), int(header[1]))","inputMat.shape()"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":28},"end":{"row":18,"column":67},"action":"remove","lines":["","    \"\"\"Solves the equation Ax=b via the Jacobi iterative method.\"\"\""]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":28},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":0},"end":{"row":42,"column":20},"action":"remove","lines":["","hp.runSolver(jacobi)"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":9},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"remove","lines":["A"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"insert","lines":["M"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":13},"end":{"row":37,"column":19},"action":"remove","lines":["inputM"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":21},"action":"insert","lines":["inputMat"]}]}],[{"group":"doc","deltas":[{"start":{"row":32,"column":0},"end":{"row":33,"column":35},"action":"remove","lines":["","A = np.array([[2.0,1.0],[5.0,7.0]])"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["A"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["M"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"remove","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":0},"end":{"row":45,"column":11},"action":"remove","lines":["","print \"A:\"","pprint(inputMat)","","print \"b:\"","pprint(b)","","print \"x:\"","pprint(sol)"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":38},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}]}]]},"ace":{"folds":[],"scrolltop":60,"scrollleft":0,"selection":{"start":{"row":36,"column":38},"end":{"row":36,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1430210325000}