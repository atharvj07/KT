#include <cstdio>
#include <algorithm>

#define rep(i, n) for(int i = 0; i < (n); ++i)

using namespace std;

int n, m;
int x[10000];

int main(){
	while(scanf("%d%d", &n, &m), n){
		rep(i, n){
			rep(j, m){
				int p;
				scanf("%d", &p);
				x[j] |= p << i;
			}
		}
		int ans = 0;
		rep(i, 1 << n){
			int t = 0;
			rep(j, m){
				int a = x[j] ^ i;
				int k = 0;
				while(a){
					a &= a - 1;
					++k;
				}
				t += max(k, n - k);
			}
			ans = max(t, ans);
		}
		printf("%d\n", ans);

		fill_n(x, m, 0);
	}
	return 0;
}