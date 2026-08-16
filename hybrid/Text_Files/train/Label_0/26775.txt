#include<iostream>
using namespace std;
int main(){
	long long n,sum=0;
	cin>>n;
	long long arr[n+1];
	for(long long i=1;i<=n;i++){
		cin>>arr[i];
		if(i%2!=0&&arr[i]%2!=0){
			sum++;
		}
	}
	cout<<sum;
}