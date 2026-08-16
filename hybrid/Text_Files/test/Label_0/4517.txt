    #include <bits/stdc++.h>
     
    using namespace std;
     
    typedef long long ll;
     
    int n1 = 0, n2 = 0, n = 0, s1[200], s2[200];
     
    void work(ll N) {
    	if(N == 1) return;
    	work(N >> 1);
    	s2[++n2] = ++n;
    	if(N & 1) s1[++n1] = ++n;
    }
     
    int main() {
    	ll N; scanf("%lld", &N); work(++N);
    	printf("%d\n", n << 1);
    	for(int i = 1; i <= n; i++) printf("%d ", i);
    	for(int i = n1; i >= 1; i--) printf("%d ", s1[i]);
    	for(int i = 1; i <= n2; i++) printf("%d ", s2[i]);
    	puts("");
    	return 0;
    }