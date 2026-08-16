#include <bits/stdc++.h>
using namespace std;
int N, bit[200010]; 
long long K; 
void add(int a, int b){
	int x = a; 
	while(x <= N+1){
		bit[x] += b; x += x & -x; 
	}
}
int sum(int a){
	int res = 0; 
	int x = a; 
	while(x > 0){
		res += bit[x]; x -= x & -x;
	}
	return res; 
}
int main(){
	cin >> N >> K; 
	long long A[200010] = {}; 
	long long S[200010] = {}; 
	int Z[200010] = {}; 
	set<long long> T; map<long long, int> M; 
	T.insert(0LL); 
	for(int i = 1; i <= N; i++){
		cin >> A[i]; A[i] -= K; 
		S[i] = S[i-1] + A[i]; T.insert(S[i]); 
	}
	int now = 0; 
	for(auto it = T.begin(); it != T.end(); it++){
		M[*it] = ++now; 
	}
	for(int i = 0; i <= N; i++) Z[i] = M[S[i]]; 
	long long ans = 0; 
	for(int i = 0; i <= N; i++){
		ans += (long long) sum(Z[i]);
		add(Z[i], 1);
	}
	cout << ans << endl; 
}