#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(void){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int N,ans = 0;
	cin >> N;
	string s[N];
	rep(i,N)cin >> s[i];
	for(int k=0;k<N;k++){ //(0,k)番目の要素を*とする
		bool ok = 1;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if((i+k)%N==j)continue;
				if(s[i][(j-k+N)%N]==s[j][(i-k+N)%N]){
				}else {
					ok = 0;
					break;
				}
			}
			if(!ok)break;
		}
		if(ok)ans++;
	}
	cout << ans*N << endl;
}