#include<string>
#include<iostream>
using namespace std;
int main()
{
	string a,b;
	cin>>a>>b;
	b.erase(b.length()-1);
	if(a==b)
		cout<<"Yes";
	else
		cout<<"No";
}
