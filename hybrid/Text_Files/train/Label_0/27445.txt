#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)

int main(){
	int N, K; cin>>N>>K;
	vector<int> A(N); rep(i, N) cin>>A[i];
	int ng = 0, ok = 1e9; // (ng,ok] = (l,r]
	while(ok - ng > 1){
		auto f = [&](int m){
			int c = 0;
			rep(i, N) c += (A[i] - 1) / m;
			return c <= K;
		};
		if(int m=(ok+ng)/2; f(m)) ok = m; else ng = m;
	}
	cout<< ok <<endl;
}
