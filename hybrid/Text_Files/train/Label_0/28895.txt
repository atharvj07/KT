#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	cin>>s;
	if(s[1]==s[0]||s[2]==s[1]||s[3]==s[2])
	cout<<"Bad"<<endl;
	else
	cout<<"Good"<<endl;
	return 0;
}