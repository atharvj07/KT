#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
  map<string, vector<int> > in;

  string goku;
  int id;
  while( cin >> goku >> id ){
    in[goku].push_back(id);
  }
    for( map < string, vector<int> >::iterator it = in.begin() ; it != in.end() ; it++ ){

      cout << (*it).first << endl;
    vector <int>& go = (*it).second;
    sort(go.begin(),go.end());
    for(vector <int>::iterator  it_p = go.begin() ; it_p != go.end() ; it_p++ ){
      cout << (*it_p);
      if(it_p+1 != go.end() )cout << " ";
    }
    cout << endl;
    }

  return 0;
}