'use strict';

const n = Number(readline());
const a = readline().split(' ').map(Number);
let votes = 0;
let max_a = 0;

for (let i = 0; i < n; i++) {
    max_a = Math.max(max_a, a[i]);
    votes += a[i];
}

print(Math.max(Math.ceil((2 * votes + 1) / n), max_a));