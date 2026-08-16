#include<iostream>
using namespace std;
int ans;
char s[10],t[10];
int main()
{
	cin>>s>>t;
	for(int i=0;i<3;++i)
		ans+=(s[i]==t[i]);
	cout<<ans<<endl;
	return 0;
}