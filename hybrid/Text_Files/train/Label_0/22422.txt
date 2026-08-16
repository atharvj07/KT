#include<bits/stdc++.h>
#define Rint register int
#define MP make_pair
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
const int N = 200003;
int n, a[N], b[N];
LL ans;
priority_queue<pii> pq;
int main(){
	scanf("%d", &n);
	for(Rint i = 1;i <= n;i ++) scanf("%d", a + i);
	for(Rint i = 1;i <= n;i ++){
		scanf("%d", b + i);
		if(a[i] != b[i]) pq.push(MP(b[i], i));
	}
	while(!pq.empty()){
		pii now = pq.top(); pq.pop();
		int i = now.se, pre = (now.se + n - 2) % n + 1, suf = now.se % n + 1, step = (b[i] - a[i]) / (b[pre] + b[suf]);
		if(!step){puts("-1"); return 0;}
		ans += step; b[i] -= step * (b[pre] + b[suf]);
		if(a[i] != b[i]) pq.push(MP(b[i], i));
	}
	printf("%lld", ans);
}