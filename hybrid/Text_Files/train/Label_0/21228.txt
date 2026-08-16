#include<bits/stdc++.h>
using namespace std;
int ans=10000000;
string s;
int main()
{
   cin>>s;
   int len=s.size();
   for(int i=1;i<len;i++)
   {
       if(s[i]!=s[i-1])
        ans=min(ans,max(i,len-i));
   }
   printf("%d",min(ans,len));
}
