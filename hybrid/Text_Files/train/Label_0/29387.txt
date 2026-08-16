#include<iostream>
using namespace std;
int main(){
	int N;
	bool num[10];
	for(int i=0;i<4;i++){cin>>N;num[N]=true;}
	if(num[1]&&num[9]&&num[7]&&num[4])cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
	return 0;
}