#include<stdio.h>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
int d[310];
int c[510];
int v[310];
int at[30];
int n;
int tmp[30];
int sz;
set<vector<int> >S;
inline int ABS(int a){return max(a,-a);}
void solve(int a,int b){
	if(a==n){
		for(int i=0;i<n;i++)tmp[i]=at[i];
		
		std::sort(tmp,tmp+n);
		vector<int>val;
		for(int i=0;i<n;i++)val.push_back(tmp[i]);
		if(S.count(val))return;
		S.insert(val);
		for(int i=0;i<n-1;i++){
			if(i){
				printf(" ");
				printf("%d",tmp[i+1]-tmp[i]);
			}else printf("%d",tmp[1]);
		}
		printf("\n");
		return ;
	}
	for(int i=b;i>0;i--){
		if(!c[i])continue;
		for(int j=0;j<a;j++){
			if(at[j]-i>0){
				bool ok=true;
				//c[i]--;
				int t=at[j]-i;
				for(int k=0;k<a;k++){
					if(!c[ABS(t-at[k])])ok=false;
					c[ABS(t-at[k])]--;
				}
				if(ok){
					at[a]=t;
					solve(a+1,i);
				}
				//c[i]++;
				for(int k=0;k<a;k++)c[ABS(t-at[k])]++;
			}
			if(at[j]+i<d[0]){
				bool ok=true;
				//c[i]--;
				int t=at[j]+i;
				for(int k=0;k<a;k++){
					if(!c[ABS(t-at[k])])ok=false;
					c[ABS(t-at[k])]--;
				}
				if(ok){
					at[a]=t;
					solve(a+1,i);
				}
				//c[i]++;
				for(int k=0;k<a;k++)c[ABS(t-at[k])]++;
			}
		}
		break;
	}
}
int main(){
	int a;
	while(scanf("%d",&a),a){
		n=a;
		S.clear();
		sz=n*(n-1)/2;
		for(int i=0;i<a*(a-1)/2;i++)scanf("%d",d+i);
		for(int i=0;i<510;i++){
			c[i]=0;
		}
		for(int i=0;i<310;i++)v[i]=0;
		for(int i=0;i<a*(a-1)/2;i++)c[d[i]]++;
		c[d[0]]--;
		
		at[0]=d[0];
		at[1]=0;
		solve(2,d[0]-1);
		printf("-----\n");
	}
}