#include <bits/stdc++.h>
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;

pair<int,string> v=make_pair(19191919,"1919");
string A="123456789";
char pat[114514];
int n,cnt[10][10];

int cal(string s){
    int a[3][3],x[10],y[10],sum=0;
    r(i,3){
        r(j,3){
            int p=(s[i*3+j]-'0');
            a[i][j]=p;
            x[p]=j;
            y[p]=i;
        }
    }
    r(i,10){
        r(j,10){
            int X=abs(x[i]-x[j]);
            int Y=abs(y[i]-y[j]);
            sum += (X+Y)*cnt[i][j];
        }
    }
    return sum;
}

int main(){
    scanf("%d%s",&n,pat);
    r(i,n-1){
        cnt[pat[i]-'0'][pat[i+1]-'0']++;
    }
    do{
        v=min(v,make_pair(cal(A),A));
    }while(next_permutation(A.begin(),A.end()));

    cout<<v.second.substr(0,3)<<endl;
    cout<<v.second.substr(3,3)<<endl;
    cout<<v.second.substr(6,3)<<endl;
}
