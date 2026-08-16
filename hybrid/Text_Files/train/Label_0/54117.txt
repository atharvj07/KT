'use strict';

/*let input = `......,,,,,......  1234 1234  1234 , 1234 ...   ,   1234 ...   1234   ... ,   1234`.split('\n');
function print(output) {
	console.log(output);
}
function readline() {
	return input.shift();
}*/

//code

var inpStr = readline();
var inpArr = inpStr.trim().split('').reduce(function (acc, val, i, arr) {
	if (val !== " " || !(isNaN(parseInt(acc[acc.length - 1])) || isNaN(parseInt(arr[i + 1])))) {
		acc.push(val);
	}
	return acc;
}, []);

for (var i = 0; i < inpArr.length; i++) {
	if (inpArr[i] === ",") {
		inpArr.splice(i + 1, 0, " ");
		i++;
	} else if (inpArr[i] === "." && inpArr[i + 1] === "." && inpArr[i + 2] === ".") {
		if (inpArr[i - 1] !== " ") {
			inpArr.splice(i, 0, " ");
			i += 3;
		} else {
			i += 2;
		}
	}
}

print(inpArr.join('').trim());
