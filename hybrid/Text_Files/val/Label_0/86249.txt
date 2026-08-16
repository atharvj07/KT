#include "bits/stdc++.h"
using namespace std;

long long MOD = 1000 * 1000 * 1000 + 7;

long long p(long long a, long long b) {
	if (b == 0) return 1;
	if (b == 1) return a;
	long long ha = p(a, b/2);
	if (b % 2 == 0) return (ha * ha) % MOD;
	return (((ha * ha) % MOD) * a) % MOD;
}

int main() {
	
	long long n;
	cin >> n;
	long long ar[n];
	for (int i=0; i<n; i++) cin >> ar[i];
	
	sort(ar, ar+n);
	reverse(ar, ar+n);
	
	long long x = p(2, 2*n-2);
	long long s = 0;
	for (int i=1; i<=n; i++) {
		s += (i + 1) * (ar[i-1]);
		s %= MOD;
	}
	
	cout << (x * s) % MOD << endl;
	
	
}
