#include <iostream> 
#include <string> 
#include <vector> 
#include <cmath> 
#include <algorithm> 
#include <cstdlib> 
#include <functional>
#include <stdio.h>
#include <sstream>

using namespace std;

int main()
{
	int n,max,min;
	string str,str2;

	cin>>n;

	for(int i=0;i<n;i++){
		cin>>str;
		str2=str;

		sort(str.begin(),str.end(),greater<int>());
		sort(str2.begin(),str2.end());

		stringstream ss,ss2;
		int min,max;

		ss<<str; ss>>max;
		ss2<<str2; ss2>>min;

		cout<<max-min<<endl;

	}


	return 0;

}