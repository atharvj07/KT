#include <bits/stdc++.h>
using namespace std;
int n;
string s;
int main()
{
	cin>>n>>s;
	for(int i=0;i<s.size();i++)
	{
		int num=s[i]-'A';
		num+=n;
		num%=26;
		s[i]=(char)num+'A';
	}
	cout<<s<<endl;
}