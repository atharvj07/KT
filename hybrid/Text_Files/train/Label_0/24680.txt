#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long n,s=2,i;
    cin>>n;
    for(i=1;i<=n;i++)
    { 
		s=(s+1)*2;
    } 
    cout<<s<<endl;
    return 0; 
}