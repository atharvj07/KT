#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;


int main()
{
	int a[4];
	for(int i=0;i<4;i++)cin>>a[i];
	sort(a,a+4);
	if(a[0]==1&&a[1]==4&&a[2]==7&&a[3]==9)cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
	return 0;
}