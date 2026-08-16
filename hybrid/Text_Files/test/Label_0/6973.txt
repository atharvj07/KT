#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
int main(void){
  int n,k,i,bi,hs=0,max;
  string s;
  vector<int> w;
  cin >> n >> k >> s;
  if (s[0]=='0') w.push_back(0);
  i=0;
  while (i<n){
    bi=i;
    while (i<n && s[i+1]==s[i]) i++;
    w.push_back(i-bi+1);
    i++;
  }
  if (s[n-1]=='0') w.push_back(0);
  if (w.size()<=k*2+1){
    cout << n << endl;
    return 0;
  }
  for (i=0;i<k*2+1;i++) hs+=w[i];
  max=hs;
  for (i=0;i+k*2+2<w.size();i+=2){
    hs+=w[i+k*2+1]+w[i+k*2+2]-w[i]-w[i+1];
    if (max<hs) max=hs;
  }
  cout << max << endl;
  return 0;
}