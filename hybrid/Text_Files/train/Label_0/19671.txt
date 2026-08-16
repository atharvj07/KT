#include<iostream>
using namespace std;

typedef unsigned long long ull;
typedef unsigned __int128  ui128;

signed main(){
	ui128 ans = 0, b = 0;
	ull N, k;
	cin>>N>>k;
	
	for(ui128 i = 1; i < N; i++){
		ans = (k*b+k-1)/(k-1);
		// cout<<i<<" "<<ans<<endl;
		b = ans;
	}
	cout<<(ull)ans<<endl;
	
	return 0;
}
