#include<iostream>
using namespace std;
string s;
int main()
{
	cin>>s;
	for(int i=1;i<s.size();i++)
		if(s[i]==s[i-1])
			cout<<"Bad",exit(0);
	cout<<"Good";
    return 0;
}