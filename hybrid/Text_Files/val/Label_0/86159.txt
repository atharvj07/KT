#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int sum,n;
	while(1)
	{
		cin>>sum;
		if(sum==0)
			break;
		for(int i=0;i<9;i++)
		{
			cin>>n;
			sum-=n;
		}
		cout<<sum<<endl;
	}
	return 0;
}
