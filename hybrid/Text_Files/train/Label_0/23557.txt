#include<bits/stdc++.h>
using namespace std;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

void solve(){
	int n,m;	cin>>n>>m;
	bool flag[16] = {0};

	while(n){
		int rem = n%m;
		if(flag[rem]) { cout<<"NO\n"; return; }
		flag[rem] = 1;
		n /= m;
	}
	cout<<"YES\n";
}

int main(){

	int t=1;	//cin>>t;
	while(t--)		solve();

}