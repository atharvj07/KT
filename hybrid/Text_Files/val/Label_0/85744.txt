#include<iostream>
#include<cstdio>
using namespace std;
int n,cnt,a[200010],b[200010];
int main()
{
	cin>>n;
	for(register int i=1;i<=n;++i)
		scanf("%d",&a[i]);
	for(register int i=n;i>=1;--i)
	{
		int sum=0;
		for(register int j=i*2;j<=n;j+=i)
			sum+=b[j];
		if(sum%2!=a[i])
			b[i]=1,++cnt;
	}
	cout<<cnt<<endl;
	for(register int i=1;i<=n;++i)
		if(b[i])
			printf("%d ",i);
	return 0;
}