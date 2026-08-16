#include<iostream>
using namespace std;
int main(){
	int a;
	cin>>a;
	if(a%10==3)
	cout<<"bon"<<endl;
	else if(a%10==0||a%10==1||a%10==6||a%10==8)
	cout<<"pon"<<endl;
	else cout<<"hon"<<endl;
}