#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int main(){
	int num,ac;
	multimap<int,int,greater<int> > teams;
	while(scanf("%d,%d",&num,&ac)!=EOF){
		if(num==0&&ac==0)break;
		teams.insert(multimap<int,int>::value_type(ac,num));
	}
	int rank=1,acl;
	map<int,int> ranking;
	for(multimap<int,int>::iterator it=teams.begin();it!=teams.end();++it){
		if(it==teams.begin()){
			acl=(*it).first;
			ranking[(*it).second]=rank;
		}else{
			if(acl!=(*it).first) ++rank;
			acl=(*it).first;
			ranking[(*it).second]=rank;
		}
	}
	while(cin>>num) cout<<ranking[num]<<endl;
	return 0;
}