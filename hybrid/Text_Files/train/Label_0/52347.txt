'use strict'
 
const g = (v, k) => { let r = 0;  while (v && v % k === 0) { v = v / k; r++; } return r; }
const n = parseInt(readline());
const m = Array(n).fill().map(() => readline().split(' ').map(Number))
 
const f = k => {
    const b = Array(n).fill().map(() => []);
    for(let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            b[i][j] = g(m[i][j], k);
        }
    }
    for(let i = 1; i < n; i++) {
        b[i][0] += b[i-1][0];
        b[0][i] += b[0][i-1];
    }
    for(let i = 1; i < n; i++) {
        for (let j = 1; j < n; j++) {
            b[i][j] += Math.min(b[i-1][j], b[i][j-1]);
        }
    }
    let p = '', i = n-1, j = n-1;
    while (i+j) {
        if (i === 0) { p += 'R'.repeat(j); break; }
        if (j === 0) { p += 'D'.repeat(i); break; }
        
        if (b[i][j-1] < b[i-1][j]) { j--; p += 'R'; }
        else { i--; p += 'D'; }
    }
            
    return [ b[n-1][n-1], p ];
}
 
const main = () => {
    const r = ((a, b) => a[0] < b[0] ? a : b)(f(2), f(5));
    if (r[0] > 1) {
        for(let i = 1; i < n; i++) {
            for (let j = 1; j < n; j++) {
                if(m[i][j] === 0) {
                    return '1\n' + 'D'.repeat(i) + 'R'.repeat(n-1) + 'D'.repeat(n-1-i);
                }
            }
        }
    }
    return r[0] + '\n' + r[1].split('').reverse().join('');
}
write(main());