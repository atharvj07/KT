#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,sum=0;
	cin>>n;
	int f[n];
	for(int i=0;i<n;i++) {cin>>f[i];sum+=f[i]-1;}
	cout<<sum;
}