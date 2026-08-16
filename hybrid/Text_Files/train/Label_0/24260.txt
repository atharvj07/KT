#include<iostream>
using namespace std;
int main(){
	int H,W;
	int i,j;
	while(1){
		cin>>H>>W;
		if(H==0&&W==0)break;
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if(i%2==0&&j%2==0||i%2==1&&j%2==1)cout<<"#";
				else cout<<".";
			}
			cout<<endl;
		}
		cout<<endl;
	}
	return 0;
}