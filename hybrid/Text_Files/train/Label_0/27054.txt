#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=a;i<b;++i)
#define for_rev(i,a,b) for(int i=a;i>=b;--i)
#define rep(i,n) for(int i=0;i<(n);++i)
#define allof(a) a.begin(),a.end()
#define minit(a,b) memset(a,b,sizeof(a))
#define size_of(a) (int)a.size()

typedef long long lint;
typedef double Double;
typedef pair< int, int > pii;

int N, M, col[110], ans[110];

int main() {
	minit(col, 0);
	
	cin >> N >> M;
	
	for_(i,0,M) {
		int a, l;
		cin >> a >> l;
		for_(j,0,l) col[(a + j) % N] = 1;
	}
	
	minit(ans, 0);
	
	for_(i,0,N) {
		if (col[i]) {
			int len = 0, s = i, t = i + 1;
			
			while (col[s]) {
				col[s] = 0;
				++len;
				s = (s - 1 + N) % N;
			}
			
			while (col[t]) {
				col[t] = 0;
				++len;
				t = (t + 1) % N;
			}
			
			++ans[len];
		}
	}
	
	for_rev(i,105,1) if (ans[i] > 0) cout << i << " " << ans[i] << endl;
}
