#include<bits/stdc++.h> 
using namespace std;
int main()
{
	string s;
	long long n;
	cin>>n;
  	while(n--)
	{
  		s=char(96+n%26+1)+s;
    	n/=26;
  	}
  	cout<<s;
}