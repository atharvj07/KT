#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,i;
	string s;
	char a;
	cin>>n>>s;
	a=n;
	for(i=0;i<s.size();i++) 
	{
		s[i]+=a;
		if(s[i]>'Z')s[i]-=26;
	}
	cout<<s;
	return 0;
}