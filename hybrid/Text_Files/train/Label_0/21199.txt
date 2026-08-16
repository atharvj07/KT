#include<bits/stdc++.h>
#define int long long
#define N 200000
#define P 1000000007
using namespace std;
int T,n,f[N+1],pf,g[N+1],pg;
string s[3];
bool pd(string s1,string s2){
	int n0=0,n1=0,n2=0,n3=0;
	for(int i=0;i<2*n;i++)if(s1[i]=='0')n0++;else n1++;
	for(int i=0;i<2*n;i++)if(s2[i]=='0')n2++;else n3++;
	int nfl=0;
	if(n3>=n2&&n1>=n0)swap(n0,n1),swap(n2,n3),nfl=1;
	if(n0>=n1&&n2>=n3){
		int np=0;
		for(int i=0;i<2*n;i++)f[i]=-1;
		for(int i=0;i<2*n;i++){
			if((s1[i]-'0')==nfl){
				while(np<2*n&&s2[np]-'0'!=nfl)np++;
				if(np<2*n)f[i]=np,np++;
			}
		}int li=0;
		for(int i=0;i<2*n;i++){
			if(f[i]==-1)printf("%c",s1[i]);
			else{
				for(int j=(i?f[li]:(-1))+1;j<f[i];j++)printf("%c",s2[j]);
				printf("%c",s1[i]);li=i;
			}
		}
		for(int i=f[li]+1;i<2*n;i++)printf("%c",s2[i]);
		return 1;
	}else return 0;
}
signed main(){
//	freopen("1.in","r",stdin);
//	freopen("a.out","w",stdout);
	cin>>T;
	while(T--){
		cin>>n;
		cin>>s[0]>>s[1]>>s[2];
		if(pd(s[0],s[1])||pd(s[0],s[2])||pd(s[1],s[2]));printf("\n");
	}
	return 0;
}
/*

*/