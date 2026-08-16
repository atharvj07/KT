#include<bits/stdc++.h>

using namespace std;
int n,f[1202020],siz[202020];
const int mod = 1e9+7;
long long sum = 0;

inline int getf(int x) {
	if (x == f[x])
		return x;
	return f[x] = getf(f[x]);
}
int m,aa,bb;
int main() {
scanf("%d",&n);
for (int i = 1;i <= n; i++) {
	scanf("%d",&aa);
	f[aa]++;
}
int fl = 0;
for (int i = 2;i <= 1000000; i++ ) {
	int sum = 0;
	for (int j = 1;j*i <= 1000000; j++)
		sum += f[i*j];
	if (sum == n) {
		printf("not coprime");
		return 0;
	}
	if (sum > 1) {
		fl = 1;
	}
}
	if (fl) {
		printf("setwise coprime");
	}
	else
		printf("pairwise coprime");
	return 0;
}
/*
5
6 14 15 7 12 16 5 4 11 9 3 10 8 2 13 1
4
1 2 3 4 5 6 7 8
*/