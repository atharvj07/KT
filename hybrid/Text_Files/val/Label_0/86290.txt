#include<iostream>
#include<string>
using namespace std;
int main(){
string type;
int t[4]={0};
while(cin>>type){
type+=" ";
int i;
for(i=0;type[i]!=',';i++);
i++;
if(type[i]=='A'&&type[i+1]=='B'){
t[2]++;
}else if(type[i]=='A'){
t[0]++;
}else if(type[i]=='B'){
t[1]++;
}else if(type[i]=='O'){
t[3]++;
}
}
for(int i=0;i<4;i++){
cout<<t[i]<<endl;
}
}