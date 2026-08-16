#include "bits/stdc++.h"

using namespace std;

//int N,M,K,L,R,H,W;
long long int N,M,K,L,R,H,W;

//constexpr long long int MOD=1000000007;
//constexpr  int MOD=1000000007;
constexpr int MOD=998244353;
//constexpr long long int MOD=998244353;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>N;
	string s;
	cin>>s;
	vector<string>u(N);
	for(auto &i:u)cin>>i;
	int ans=0;
	for(auto i:u){
		int add=0;
		for(int l=0;l<i.size();l++){
			for(int j=1;j<i.size();j++){
				string t;
				for(int k=l;k<i.size()&&t.size()<s.size();k+=j){
					t.push_back(i[k]);
				}
				if(s==t)add|=1;
			}
		}
		ans+=add;
		//cout<<ans<<endl;
	}
	cout<<ans<<endl;
	return 0;
}
