#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int a[4];
	for(int i=0;i<4;i++)
		cin>>a[i];
	sort(a,a+4);
	if(a[0]==1&&a[1]==4&&a[2]==7&&a[3]==9)
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
	return 0;
}