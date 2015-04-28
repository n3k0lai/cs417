{"changed":true,"filter":false,"title":"helpers.lua","tooltip":"/scripts/helpers.lua","value":"local alg = require \"sci.alg\"\n\nfunction takeInput(fileLocation)\n    local headers = {}\n    local inputMatrix\n    local lines = 0\n    for key, line in io.lines(fileLocation) do\n        if key == 0 then\n            for w in line:gmatch(\"%w+\") do\n\n            end\n            lines = lines + 1\n        else\n            local row = {}\n            for n in line:gmatch(\"%w+\") do table.insert(row, n) end\n        \ttable.insert(inputMatrix, row)\n        end\n    end\n    local outputObj = {}\n    outputObj[\"headers\"] = headers\n    outputObj[\"mat\"] = alg.toMat(inputMatrix)\n    return outputObj\nend\n\nfunction logError(errorArg)\n    local errorVal = 2norm(b(comp) - b(act)) / 2norm(b(act)\nend\n\n-- Set grid size and number of iterations\nsaveIters = 20\ntotalIters = 200\nerrorEvery = 2\nm = 33\nn = 33\nmin = −1\nxmax = 1\nymin = −1\nymax = 1\n\n--  Compute useful constants\ndx = (xmax − xmin) / (nX − 1)\ndy = (ymax − ymin) / (ny − 1)\ndxxinv = 1 / (dx * dx)\ndyyinv = 1 / (dy * dy)\ndcent = 1 / (2 * (dxxinv + dyyinv))\n\n-- Input function\nfunction f(i, j)\n    x = xmin + i * dx\n    y = ymin + j * dy\n    return math.abs(x) > 0.5 or abs(y) > 0.5 ? 0 : 1;\nend\n\nfunction performOutput(solvedMatrix)\n    sf = string.format\n    print(sf(\"The file had %d menus out of %d lines.\", menus, lines))\n    local ouf = assert(io.open(\"junk251.jnk\", \"w\"))\n    for i=1, 20 do\n    \touf:write(tostring(1000 + i))\n    \touf:write(\"\\n\")\n    end\n    io.close(ouf)\nend","undoManager":{"mark":21,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":0},"end":{"row":38,"column":1},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":0},"end":{"row":38,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":1},"end":{"row":38,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":0},"end":{"row":46,"column":3},"action":"remove","lines":["def"]},{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":1},"end":{"row":46,"column":2},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":2},"end":{"row":46,"column":3},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":3},"end":{"row":46,"column":4},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":3},"end":{"row":51,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":28},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":[" "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":16},"action":"remove","lines":["                "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"remove","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":37},"end":{"row":25,"column":38},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":38},"end":{"row":25,"column":39},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":39},"end":{"row":25,"column":40},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":44},"end":{"row":25,"column":45},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":45},"end":{"row":25,"column":46},"action":"insert","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":46},"end":{"row":25,"column":47},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":47},"end":{"row":25,"column":48},"action":"insert","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":48},"end":{"row":25,"column":49},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":49},"end":{"row":25,"column":50},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":50},"end":{"row":25,"column":51},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":51},"end":{"row":25,"column":52},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":52},"end":{"row":25,"column":53},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":53},"end":{"row":25,"column":54},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":54},"end":{"row":25,"column":55},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":55},"end":{"row":25,"column":56},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":56},"end":{"row":25,"column":57},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":57},"end":{"row":25,"column":58},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":58},"end":{"row":25,"column":59},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":12},"end":{"row":50,"column":13},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":13},"end":{"row":50,"column":14},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":14},"end":{"row":50,"column":15},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":15},"end":{"row":50,"column":16},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":30},"end":{"row":50,"column":31},"action":"remove","lines":["|"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"remove","lines":["|"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":50,"column":30},"end":{"row":50,"column":31},"action":"insert","lines":["r"]}]}]]},"ace":{"folds":[],"scrolltop":3,"scrollleft":0,"selection":{"start":{"row":50,"column":31},"end":{"row":50,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1430163143365}