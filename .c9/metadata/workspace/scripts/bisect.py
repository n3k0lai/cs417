{"filter":false,"title":"bisect.py","tooltip":"/scripts/bisect.py","undoManager":{"mark":100,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":13},"action":"remove","lines":["ion"]}]}],[{"group":"doc","deltas":[{"start":{"row":54,"column":8},"end":{"row":54,"column":11},"action":"remove","lines":["ion"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":31},"end":{"row":8,"column":38},"action":"insert","lines":["=1.0e-4"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":0},"end":{"row":53,"column":0},"action":"remove","lines":["","def bisection(f, lower, upper, error_tolerance=1.0e-4):","    fu = f(upper)","    if fu == 0.0:  ","        return upper","    fl = f(lower)","    if fl == 0.0:  ","        return lower","    if fu*fl > 0.0:  #if the product of the function values at the two bounds is positive, then they do not bracket a root","        return None","    else:","        mid = (lower + upper) / 2","        error = (upper - lower) / 2","        while(error>error_tolerance): #the loop executes till the desired level of accuracy is attainedfm=function(mid)","            fu = f(upper)","            fl = f(lower)","","            #if the middle value is indeed the root, it is returned as the root","            if fm == 0.0: ","                return mid","","            #if the actual root lies between upper bound and the middle value, the lower bound is set to be the middle value","            elif fu * fm < 0.0:","                lower_bound = mid","","            ##if the actual root lies between lower bound and the middle value, the upper bound is set to be the middle value","            elif fl * fm < 0.0:","                upper_bound = mid","","            mid = (lower_bound + upper_bound) / 2","            error = (upper_bound - lower_bound) / 2","        return mid","","",""]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["c"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":9},"end":{"row":5,"column":16},"action":"remove","lines":["       "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["5"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["7"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":35},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["S"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["S"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":[" "]}]}]]},"ace":{"folds":[],"scrolltop":27.09089422225952,"scrollleft":0,"selection":{"start":{"row":13,"column":24},"end":{"row":13,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1430215506000,"hash":"fbcc12f3376e85e681da897a5b09c06cc8d0e315"}