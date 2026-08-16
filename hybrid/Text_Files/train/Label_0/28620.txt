#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
char str[210];
int v[210];
int main(){
	int T;scanf("%d",&T);
	while(T--){
		int n;
		scanf("%d%s",&n,str);
		int a=strlen(str);
		int ret=0;
		for(int i=0;i<=a;i++){
			int B=0;int G=0;
			for(int j=0;j<a;j++){
				v[j]=0;
				if(str[j]=='B')B++;
				else G++;
			}
			int at=0;
			int t=0;
			int sz=a;
			while(B&&G){
				int c=n%sz;
				if(i==t){c++;}
				if(c==0)c+=sz;
				while(1){
					if(!v[at]){c--;if(c==0)break;}
					at=(at+1)%a;
				}
				v[at]=1;
				if(str[at]=='B')B--;
				else G--;
				sz--;
				t++;
			}
			ret=max(ret,B);
		}
		printf("%d\n",ret);
	}
}