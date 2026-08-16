#include<bits/stdc++.h>
using namespace std;
int fr1[150];
int fr2[130];
int main()
{
   string s,t;
   cin>>s>>t;int y=1;
   map<char,int> mp;
   for(int i=0;i<s.size();i++)
   {
       fr1[s[i]]++;
       fr2[t[i]]++;
       if(fr1[s[i]]!=fr2[t[i]])
       {
           y=0;
           break;
       }
   }
   if(y==0)
    cout<<"No\n";
    else
        cout<<"Yes\n";

}

