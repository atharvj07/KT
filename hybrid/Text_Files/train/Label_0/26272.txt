//E
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char s[1000010];
int sum[1000010];
int mxn[1000010];
int mx,mi,ans,n;
void check(int mx){
	mi=0;
	int cnt=0;
	for(int i=1;i<=n;i++){
		if(s[i]=='0') cnt--;
		if(s[i]=='1') cnt++;
		if(s[i]=='?'){
			if(mxn[i]-sum[i-1]+cnt+2<=mx) cnt++;
			else cnt--;
		}
		mi=min(mi,cnt);
	}
}
int main()
{
	scanf("%s",s+1);
	n=strlen(s+1);
	for(int i=1;i<=n;i++){
		if(s[i]=='0'||s[i]=='?') sum[i]=sum[i-1]-1;
		if(s[i]=='1') sum[i]=sum[i-1]+1;
		mx=max(mx,sum[i]);
	}
	mxn[n]=sum[n];
	for(int i=n-1;i>=1;i--)
		mxn[i]=max(sum[i],mxn[i+1]);
	check(mx);
	//cout<<mx<<mi<<endl;
	ans=mx-mi;
	mx++;
	check(mx);
	//cout<<mx<<mi<<endl;
	ans=min(ans,mx-mi);
	printf("%d",ans);
}