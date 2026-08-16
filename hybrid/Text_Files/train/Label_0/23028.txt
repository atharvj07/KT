#include <iostream>
using namespace std;

int main() {
	int n,cR=0,cB=0;
	cin>>n;
	while(n--)
	{
	    char s;
	    cin>>s;
	    if(s=='R')
	    cR++;
	    else
	    cB++;
	}
	if(cR>cB)
	cout<<"Yes";
	else
	cout<<"No";
	return 0;
}