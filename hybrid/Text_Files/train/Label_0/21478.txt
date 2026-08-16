#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n)for(int i=0;i<n;i++)
using namespace std;
typedef long long ll;

int a[100000];
ll fact[100000];
ll bit[100001];
int n;

void add(int i, int x) {
	while (i <= n) {
		bit[i] += x;
		i += i&-i;
	}
}
int sum(int i) {
	int s = 0;
	while (i > 0) {
		s += bit[i];
		i -= i&-i;
	}
	return s;
}
int main() {
	while (scanf("%d", &n), n) {
		int r; scanf("%d", &r);
		rep(i, n) {
			a[i] = i;
			add(i + 1, 1);
		}
		rep(i, r) {
			int s, t; scanf("%d%d", &s, &t); s--; t--;
			swap(a[s], a[t]);
		}
		fact[0] = 1;
		for (int i = 1; i < n; i++)fact[i] = (fact[i - 1] * i) % MOD;
		ll cnt = 0;
		rep(i, n) {
			int d = sum(a[i]);
			cnt = (cnt + fact[n - i - 1] * d) % MOD;
			add(a[i] + 1, -1);
		}
		printf("%lld\n", cnt);
	}
}