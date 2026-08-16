#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i< (n); i++)
using ll = long long;
using namespace std;

int popcount(int x){
	return __builtin_popcount(x);
}

int f(int x){
	int nop = 0;
	while (x > 0){
		x %= popcount(x);
		nop++;
	}
	return nop;
}

int main(void){
	int N;
	string X;
	cin >> N >> X;
	int a[N];
	rep(i,N) a[i] = X[i] - '0';

	int pop0 = 0;
	rep(i,N) pop0 += a[i];

	int ans[N];
	rep(i,N) ans[i] = 0;

	rep(i,2) {
		int pop;
		if (i == 1) pop = pop0 - 1;
		else pop = pop0 + 1;

		if (pop <= 0) continue;

		int mod0 = 0;

		rep(j,N){
			mod0 = (mod0*2)%pop;
			mod0 += a[j];
		}		

		int k = 1;
		for (int j = N-1; j >=0; j--) {
			if (a[j] == i){
				int x = mod0;
				if (a[j] == 1) x = (x-k+pop)%pop;
				else x = (x+k)%pop;
				ans[j] = f(x) + 1;
			}
			k = (2*k)%pop;
		}
	}

	rep(i,N) cout << ans[i] << endl;

	return 0;
}
