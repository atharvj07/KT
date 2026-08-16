#include<iostream>
#include<map>
using namespace std;
long long a[200005],s[200005];
map<long long,long long> mod;
int main()
{
	long long n,k,sum=0;
	scanf("%lld%lld",&n,&k);
	for(int i=1;i<=n;i++)scanf("%lld",&a[i]);
	for(int i=1;i<=n;i++)s[i]=s[i-1]+a[i];
	s[0]=0;a[0]=0;
	for(int i=1;i<=n;i++)
	{
		mod[(s[i-1]-i+1)%k]++;
		if(i>=k)mod[(s[i-k]-(i-k))%k]--;
		sum+=mod[(s[i]-i)%k];
	}
	printf("%lld\n",sum);
}