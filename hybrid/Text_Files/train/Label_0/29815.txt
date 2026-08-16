#include<bits/stdc++.h>
#define ll  long long int 
using namespace std;

int main()
{
	ll n,a,b;
	cin>>n>>a>>b;
	ll dif=b-a;
	ll ans;
	if(dif%2==0)
		ans=dif/2;
	else 
	{
		ans=min(a+(b-a-1)/2,n-b+1+(b-a-1)/2);
	}
	cout<<ans<<endl;
}