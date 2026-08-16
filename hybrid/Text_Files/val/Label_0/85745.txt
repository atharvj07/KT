#include<bits/stdc++.h>
#define ff(x,a,b) for(int x=a;x<=b;x++)
#define fff(x,a,b) for(int x=a;x>=b;x--)
#define void inline void
using namespace std;
typedef long long ll;
int n,a[200005],b[200005],t;
int main()
{
	cin>>n;
	ff(i,1,n) scanf("%d",a+i);
	fff(i,n,1)
	{
		if(i*2>n) b[i]=a[i];else
		{
			int sum=0;
			for (int j=i<<1;j<=n;j+=i) sum=(sum+b[j])&1;
			b[i]=sum^a[i];
		}
	}
	ff(i,1,n) t+=b[i];
	cout<<t<<endl;
	ff(i,1,n) if(b[i]) printf("%d ",i);
}