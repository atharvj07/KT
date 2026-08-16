#include<cstdio>
#include<queue>
#include<iostream>
#include<cstring>
#include<stack>
#include<list>
#include<set>
#include<map>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
typedef long long ll;
const int maxn = 1e6 + 8;
const int mod = 1e9+7;
char str[maxn],str1[maxn],ans[maxn];
set<string> se;
int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--){
		int n,k;scanf("%d%d",&n,&k);
		scanf("%s",str+1);
		se.clear();
		int m=1,val=n-k+1;
		while(m<=k && (1<<m)<val+1) m++;
		m = min(m,k);
		int t = 0;
		for(int i=1;i<=k;i++){
			if(str[i]=='1') str1[i]='0';
			else str1[i]='1';
			if(str[i]=='0'&&i<=k-m) t--;
		}
		if(t==0) se.insert(str1+(k-m+1));
		for(int i=k+1;i<=n;i++){
			if(str[i]=='1') str1[i]='0';
			else str1[i]='1';
			if(str[i-m]=='0') t--;
			if(str[i-k]=='0') t++;
			if(t==0) se.insert(str1+(i-m+1));
		}
//		for(auto i=se.begin();i!=se.end();i++){
//			cout<<*i<<endl;
//		}
		for(int i=1;i<=n;i++) str1[i]='\0';
		ans[m+1]='\0';
		int flag = 0;
		for(int i=0;i<(1<<m);i++){
			for(int j=0;j<m;j++){
				if(i&(1<<j)) ans[m-j]='1';
				else ans[m-j]='0';
			} 
//			printf("%d:%s\n",i,ans+1);
			if(se.find(ans+1)==se.end()){
				flag = 1;
				break;	
			}
		}
		if(flag==1){
			printf("YES\n");
			for(int i=1;i<=k-m;i++) printf("0");
			for(int i=1;i<=m;i++) printf("%c",ans[i]);
			printf("\n");
		}
		else printf("NO\n");
	} 
}
