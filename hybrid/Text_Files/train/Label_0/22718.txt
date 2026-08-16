#pragma GCC optimize(2)
#pragma GCC optimize(3)
#pragma GCC optimize("Ofast")
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 200010
using namespace std;
namespace ywy{
	inline int get(){
		int n=0;char c;while((c=getchar())||23333)if(c>='0'&&c<='9')break;
		n=c-'0';while((c=getchar())||23333){
			if(c>='0'&&c<='9')n=n*10+c-'0';else return n;
		}
	}
	struct node{
		int r,c;
		friend bool operator <(const node &a,const node &b){
			return a.r<b.r;
		}
	}memchi[N];
	int solve_0(int r,int c){
		if(r==c)
			return(r-1);
		return (r-c)/2;
	}
	int solve_1(int r,int c){
		return (r-c+1)/2;	
	}
	void ywymain(){
		int t=get();
		memchi[0].r=memchi[0].c=1;
		while(t){
			t--;
			int n=get(),ans=0;
			for(int i=1;i<=n;i++)
				memchi[i].r=get();
			for(int i=1;i<=n;i++)
				memchi[i].c=get();
			sort(memchi+1,memchi+1+n);
			for(int i=(memchi[1].r==1&&memchi[1].c==1);i<n;i++){
				if((memchi[i].r+memchi[i].c)&1)
					ans+=solve_1(memchi[i+1].r-memchi[i].r+1,memchi[i+1].c-memchi[i].c+1);
				else
					ans+=solve_0(memchi[i+1].r-memchi[i].r+1,memchi[i+1].c-memchi[i].c+1);
			}
			printf("%d\n",ans);
		}
	}
}
int main(){
	ywy::ywymain();
	return 0;	
}