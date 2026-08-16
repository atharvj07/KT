#include <iostream>
#include <string>
using namespace std;
int main(){
	int H,W;
	char c,tail[101][101];
	while(cin>>H>>W&&H!=0&&W!=0){
		bool z[101][101]={0};
		int x=0,y=0,cnt=0;
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				cin>>tail[i][j];
			}
		}
		for(int i=0;i<H*W;i++){
			if(tail[x][y]=='>'){
				if(z[x][y]==1)break;
				z[x][y]=1;
				y+=1;
			}else if(tail[x][y]=='<'){
				if(z[x][y]==1)break;
				z[x][y]=1;
				y-=1;
			}else if(tail[x][y]=='^'){
				if(z[x][y]==1)break;
				z[x][y]=1;
				x-=1;
			}else if(tail[x][y]=='v'){
				if(z[x][y]==1)break;
				z[x][y]=1;
				x+=1;
			}else{
				cnt=1;
				cout<<y<<" "<<x<<endl;
				break;
			}
		}
		if(cnt==0)cout<<"LOOP"<<endl;
	}
	return 0;
}