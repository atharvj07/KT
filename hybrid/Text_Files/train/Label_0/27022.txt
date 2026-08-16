#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<cstring>
using namespace std;

int w,h,c[50][50];
void island(int i,int j){
	int x,y;
	c[i][j]=0;
	for(x=-1;x<=1;x++){
		for(y=-1;y<=1;y++){
			if(0<=j+x&&j+x<w&&0<=i+y&&i+y<h&&c[i+y][j+x]==1){
				island(i+y,j+x);
			}
		}
	}

}
int main(){
	while(1){
		int sum=0,i,j,i1,j1;
		for(i=0;i<50;i++){
			for(j=0;j<50;j++){
				c[i][j]=0;
			}
		}
		cin>>w>>h;
		if(w==0&&h==0)break;
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				cin>>c[i][j];
			}
		}
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(c[i][j]==1){
					island(i,j);
					sum++;
				}
			}
		}
		cout<<sum<<endl;
	}
    return 0;
}