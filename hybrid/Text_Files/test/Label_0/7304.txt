#include<iostream>
using namespace std;

typedef long long ll;

int main()
{
	ll a,v,b,w,t;
	cin>>a>>v>>b>>w>>t;
	ll sum=t*(v-w);
	if(sum>=(max(a,b)-min(a,b))){
		cout<<"YES"<<endl;
	}
	else {
		cout<<"NO"<<endl;
	}
	return 0;
}