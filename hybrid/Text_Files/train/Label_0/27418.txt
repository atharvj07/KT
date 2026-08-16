#include<bits/stdc++.h>
using namespace std;
const int pi=3.1415926535897932384626433832795;
const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};
#define ll long long
#define inf int(1e9+7)
#define pb push_back
#define mp make_pair
int n;
char ch[100005];
bool a[100005];
int main()
{
	scanf("%d%s",&n,&ch);
	for(int i=0;i<2;i++)
		for(int j=0;j<2;j++)
		{
			a[0]=i;
			a[1]=j;
			for(int k=1;k<n-1;k++)
				a[k+1]=a[k-1]^a[k]^(ch[k]=='x');
			if(ch[n-1]=='x'==a[n-2]^a[n-1]^a[0]&&ch[0]=='x'==a[n-1]^a[0]^a[1])
			{
				for(int k=0;k<n;k++)
					printf(a[k]?"W":"S");
				return 0;
			}
		}
	puts("-1");
	return 0;
}