#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int n,m,x;
	cin>>n>>m;
	while(m--)
	{
		cin>>x;
		n-=x;
	}
	if(n<0)	cout<<"-1"<<endl;
	else	cout<<n<<endl;
 } 