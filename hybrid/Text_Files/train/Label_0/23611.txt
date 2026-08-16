#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const int MOD = 998244353;
int add(int x, int y) {
	x += y;
	if (x >= MOD) return x - MOD;
	return x;
}
int sub(int x, int y) {
	x -= y;
	if (x < 0) return x + MOD;
	return x;
}
int mult(int x, int y) {
	return ((ll)x * y) % MOD;
}

const int N = 4010;
int n;
int a[N];
int b[N];
int c[N];
int m, L1, L2;
char s[N];
int p2[N];

void reduce() {
	//cerr << "REDUCE" << endl;
	while(true) {
		//cerr << L1 << " " << L2 << endl;
		if (L1 > L2) {
			swap(a, b);
			swap(L1, L2);
		}
		for (int i = 0; i < L1; i++)
			b[L2 - L1 + i] ^= a[i];
		while(L2 > 0 && b[L2 - 1] == 0) L2--;
		if (L2 == 0) break;
	}
}

int solve() {
	if (L1 > m) return 0;
	for (int i = 0; i < m; i++)
		b[i] = 0;
	int ans = 0;
	for (int i = m - 1; i >= L1 - 1; i--) {
		if (c[i] == 1) ans = add(ans, p2[1 + i - L1]);
		if (b[i] != c[i]) {
			for (int j = 0; j < L1; j++)
				b[i - L1 + 1 + j] ^= a[j];
		}
	}
	int p = L1 - 1;
	while(p >= 0 && b[p] == c[p]) p--;
	if (p < 0 || b[p] < c[p]) ans = add(ans, 1);
	return ans;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	p2[0] = 1;
	for (int i = 1; i < N; i++)
		p2[i] = add(p2[i - 1], p2[i - 1]);

	scanf("%d", &n);
	scanf("%s", s);
	m = strlen(s);
	for (int i = 0; i < m; i++)
		c[i] = s[m - 1 - i] - '0';
	scanf("%s", s);
	L1 = strlen(s);
	for (int i = 0; i < L1; i++)
		a[i] = s[L1 - 1 - i] - '0';
	n--;
	while(n--) {
		scanf("%s", s);
		L2 = strlen(s);
		for (int i = 0; i < L2; i++)
			b[i] = s[L2 - 1 - i] - '0';
		reduce();
	}
	/*
	printf("%d ", L1);
	for (int i = 0; i < L1; i++)
		printf("%d", a[i]);
	printf("\n");
	*/
	printf("%d\n", solve());

	return 0;
}
