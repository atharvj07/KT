var s = "";
var buf = "";

s = readline().split(' ');

var n = s[0] - 0;
var m = s[1] - 0;
var k = s[2] - 0;

var row = new Array(n + 1);
for (var i = 0; i < n + 1; i++) row[i] = i;

var col = new Array(m + 1);
for (var i = 0; i < m + 1; i++) col[i] = i;

var matrix = new Array(n);
for (var i = 0; i < n; i++) { 
    matrix[i] = readline().split(' ');
}

for (var i = 0; i < k; i++) {

    s = readline().split(' ');

    var q = s[0];
    var x = s[1] - 0;
    var y = s[2] - 0;

    if (q == 'c') {
        var c = col[x]; col[x] = col[y], col[y] = c;
    } else if (q == 'r') {
        var c = row[x]; row[x] = row[y], row[y] = c;
    } else {
        buf += matrix[row[x] - 1][col[y] - 1] + '\n';
        if (i % 65536 == 0) {
            print(buf);
            buf = "";
        };
    }
}

print(buf);