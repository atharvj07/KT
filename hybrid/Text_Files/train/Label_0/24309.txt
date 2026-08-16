#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
int a,b,c;
cin>>a>>b>>c;
int i=0;
int k;
cin>>k;

while(b<=a)
{
	b=b*2;
	k--;
}
while(c<=b)
{
	c*=2;
	k--;
}
if(k>=0) cout<<"Yes"<<endl;
else cout<<"No"<<endl;
}