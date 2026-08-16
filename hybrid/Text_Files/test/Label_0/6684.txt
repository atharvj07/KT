#define	_USE_MATH_DEFINES
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <set>
using namespace std;
int main(){
	
	map<double,string> s;
	vector<double> t1(8);
	vector<double> t2(8);
	vector<double> t3(8);
	vector<double> t4;
	for(int i=0;i<8;i++){
		string a;
		cin>>a>>t1[i];
		s[t1[i]]=a;
	}
	for(int i=0;i<8;i++){
		string a;
		cin>>a>>t2[i];
		s[t2[i]]=a;
	}
	for(int i=0;i<8;i++){
		string a;
		cin>>a>>t3[i];
		s[t3[i]]=a;
	}
	
	
	sort(t1.begin(),t1.end());
	sort(t2.begin(),t2.end());
	sort(t3.begin(),t3.end());
	
	for(int i=2;i<8;i++){
		t4.push_back(t1[i]);
		t4.push_back(t2[i]);
		t4.push_back(t3[i]);
	}
	sort(t4.begin(),t4.end());
	
	
	cout<<s[t1[0]]<<" "<<t1[0]<<endl;
	cout<<s[t1[1]]<<" "<<t1[1]<<endl;
	cout<<s[t2[0]]<<" "<<t2[0]<<endl;
	cout<<s[t2[1]]<<" "<<t2[1]<<endl;
	cout<<s[t3[0]]<<" "<<t3[0]<<endl;
	cout<<s[t3[1]]<<" "<<t3[1]<<endl; 
	cout<<s[t4[0]]<<" "<<t4[0]<<endl;
	cout<<s[t4[1]]<<" "<<t4[1]<<endl;
	
	
	
	
}