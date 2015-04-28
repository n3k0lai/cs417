{"filter":false,"title":"bisect.lua","tooltip":"/scripts/bisect.lua","undoManager":{"mark":80,"position":80,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":14,"column":55},"action":"insert","lines":["INPUT: Function f, endpoint values a, b, tolerance TOL, maximum iterations NMAX","CONDITIONS: a < b, either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0","OUTPUT: value which differs from a root of f(x)=0 by less than TOL"," ","N ← 1","While N ≤ NMAX # limit iterations to prevent infinite loop","  c ← (a + b)/2 # new midpoint","  If f(c) = 0 or (b – a)/2 < TOL then # solution found","    Output(c)","    Stop","  EndIf","  N ← N + 1 # increment step counter","  If sign(f(c)) = sign(f(a)) then a ← c else b ← c # new interval","EndWhile","Output(\"Method failed.\") # max number of steps exceeded"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"remove","lines":["←"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"remove","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["←"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["←"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":["W"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":2},"end":{"row":12,"column":4},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":2},"end":{"row":11,"column":4},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":2},"end":{"row":10,"column":4},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":2},"end":{"row":7,"column":4},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":36},"end":{"row":7,"column":40},"action":"remove","lines":["then"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":2},"end":{"row":6,"column":4},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["W"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["w"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["≤"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["<"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":[" "]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":2},"end":{"row":2,"column":2},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1430164819340,"hash":"88210c594e27890a4ae8bafa2f7e5927409d06c0"}