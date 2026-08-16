#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define rep(i,n) for(int i=0;i<int(n);++i)

int pa[10][10]={0};
int x,y,s;
char t;
int d=0,wh=0;

void foo(int x,int y){
	if(x>=0&&x<10&&y<10&&y>=0){
		pa[x][y]++;
	}
}


int main(){
	while(cin>>x>>t>>y>>t>>s){
		foo(x,y-1);
		foo(x,y+1);
		foo(x,y);
		foo(x+1,y);
		foo(x-1,y);
		if(s>1){
			foo(x+1,y+1);
			foo(x+1,y-1);
			foo(x-1,y-1);
			foo(x-1,y+1);
		}
		if(s>2){
			foo(x+2,y);
			foo(x-2,y);
			foo(x,y+2);
			foo(x,y-2);
		}
	}
	rep(i,10){
		rep(j,10){
			if(d<pa[i][j]){
				d = pa[i][j];
			}
			if(pa[i][j] ==0){
				wh++;
			}
		}
	}
	cout<<wh<<endl<<d<<endl;
	return 0;
	
}