{"changed":true,"filter":false,"title":"gauss.js","tooltip":"/scripts/gauss.js","value":"\nvar aRandomNumber = function() {\n    var result = Math.floor((Math.random() * 2000000) + 1);\n    result = (result - 1000000) / 10000;\n    return result;\n};\n\nvar omega = function() {\n    return 2 / (1 + Math.sin(2 * Math.PI / n))\n}\n\nvar dxxinv = function() {\n    var dx = (xmax - xmin) / (m - 1);\n    return 1 / (dx * dx)\n}\n\nvar dyyinv = function() {\n    var dy = (ymax - ymin) / (n - 1);\n    return 1 / (dy * dy);\n}\n\nvar dcent = function() {\n    return 1 / (2 * (dxxinv - dyyinv));\n}\n\nvar f = function(i, j) {\n    var x = xmin + i * dx ;\n    var y = ymin + j * dy;\n    return abs(x) > 0.5 || Math.abs(y) > 0.5 ? 0 : 1;\n}\n\n// Common output and error routine\nvar outputanderror = function(filename, a, sn) {\n    \n}\n\nvar Gauss = function(matrix) {\n    var i, j, ij, k;\n    var error, u[matrix.length * this.Nx], z;\n    \n    // Set initial guess to be identically zero\n    for(ij = 0; ij < this.Nx * this.Ny; ij++) {\n        u[ij] = 0;\n    }\n    outputanderror(\"gsrb out\",u,0);\n    \n    // Compute Red−Black Gauss−Seidel iteration\n    for(k = 1; k <= total.iters; k++) {\n        for(j = 1 ; j < n − 1; j++) {\n            for(i= 1 + (j & 1); i < m − 1; i+=2) {\n                16ij = i + this.Ny * j;\n                u[ij] = (f(i,j) + dxxinv * (u[ij − 1] + u[ij + 1]) + dyyinv * (u[ij − this.Ny] + u[ij + this.Ny])) * dcent;\n            }\n        }\n        for(j = 1; j < n − 1; j++) {\n            for(i = 2 − (j & 1); i < this.Ny − 1 ; i+=2) {\n                ij = i + this.Ny * j;\n                u[ij] = (f(i,j) + dxxinv * (u[ij − 1] + u[ij + 1]) + dyyinv * (u[ij − this.Ny] + u[ij + this.Ny])) * dcent;\n            }\n        }\n        // Save the result and compute error if necessary\n        outputanderror(\"gsrb out\",u,k);\n    }\n}","undoManager":{"mark":-1,"position":38,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":27,"column":5},"action":"insert","lines":["megaMatrix.prototype.Gauss = function() {","        var i, j, ij, k;","        var error, u[this.Ny * this.Nx], z;","        ","        // Set initial guess to be identically zero","        for(ij = 0; ij < this.Nx * this.Ny; ij++) {","            u[ij] = 0;","        }","        outputanderror(\"gsrb out\",u,0);","        ","        // Compute Red−Black Gauss−Seidel iteration","        for(k = 1; k <= total.iters; k++) {","            for(j = 1 ; j < n − 1; j++) {","                for(i= 1 + (j & 1); i < m − 1; i+=2) {","                    16ij = i + this.Ny * j;","                    u[ij] = (f(i,j) + dxxinv * (u[ij − 1] + u[ij + 1]) + dyyinv * (u[ij − this.Ny] + u[ij + this.Ny])) * cent;","                }","            }","            for(j = 1; j < n − 1; j++) {","                for(i = 2 − (j & 1); i < this.Ny − 1 ; i+=2) {","                    ij = i + this.Ny * j;","                    u[ij] = (f(i,j) + dxxinv * (u[ij − 1] + u[ij + 1]) + dyyinv * (u[ij − this.Ny] + u[ij + this.Ny])) * dcent;","                }","            }","            // Save the result and compute error if necessary","            outputanderror(\"gsrb out\",u,k);","        }","    }"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":34,"column":5},"action":"insert","lines":["var aRandomNumber = function() {","        var result = Math.floor((Math.random() * 2000000) + 1);","        result = (result - 1000000) / 10000;","        return result;","    };","    ","    var omega = function() {","        return 2 / (1 + Math.sin(2 * Math.PI / n))","    }","    ","    var dxxinv = function() {","        var dx = (xmax - xmin) / (m - 1);","        return 1 / (dx * dx)","    }","    ","    var dyyinv = function() {","        var dy = (ymax - ymin) / (n - 1);","        return 1 / (dy * dy);","    }","    ","    var dcent = function() {","        return 1 / (2 * (dxxinv - dyyinv));","    }","    ","    var f = function(i, j) {","        var x = xmin + i * dx ;","        var y = ymin + j * dy;","        return abs(x) > 0.5 || Math.abs(y) > 0.5 ? 0 : 1;","    }","    ","    // Common output and error routine","    var outputanderror = function(filename, a, sn) {","        ","    }"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":35,"column":0},"end":{"row":36,"column":21},"action":"remove","lines":["","megaMatrix.prototype."]},{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"remove","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"remove","lines":["    "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"remove","lines":["    "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["    "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"remove","lines":["    "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"remove","lines":["    "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"remove","lines":["    "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"remove","lines":["    "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"remove","lines":["    "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":4},"action":"remove","lines":["    "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"remove","lines":["    "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"remove","lines":["    "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"remove","lines":["    "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":51,"column":117},"end":{"row":51,"column":118},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":23},"end":{"row":36,"column":24},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"remove","lines":["y"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"remove","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"remove","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["h"]}]}]]},"ace":{"folds":[],"scrolltop":360,"scrollleft":0,"selection":{"start":{"row":34,"column":1},"end":{"row":34,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1423153256417}