#include <bits/stdc++.h>
using namespace std;
int power(int num)
{
    int p=1;
    for(;0<num;num--)p*=10;
    return p;
}
int main() {
    int n,m,a[3]={15,3,5};
    while(cin>>m>>n,n,m){
        string str,fb[3]={"FizzBuzz","Fizz","Buzz"};
        bool player[1000]={};
        for(int i=1,now=0,out=m;i<=n;i++,now=(now+1)%m){
			cin>>str;
			if(out>1){
				int num=0,co=-1;
				while(player[now])now=(now+1)%m;
				for(int j=0;j<3&&co<0;j++)if(i%a[j]<1)co=j;
				if(co<0)for(int j=0;j<str.size();j++)num+=(str[j]-'0')*power(str.size()-1-j);
				if(co>-1&&str!=fb[co]||co<0&&i!=num)player[now]=1;
				if(player[now])out--;
			}
		}
		for(int i=0,co=0;i<m;i++){
			if(!player[i]&&co>0)cout<<" ";
			if(!player[i]){
				cout<<i+1;
				co++;
			}
		}
		cout<<endl;
	}
}