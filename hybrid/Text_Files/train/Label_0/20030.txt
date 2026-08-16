#include<iostream>
using namespace std;
int main(){
	int n,a,b;
	cin>>n>>a>>b;
	cout<<(((a-b)%2==0)?"Alice":"Borys")<<endl;
}