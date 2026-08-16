#include<bits/stdc++.h>
using namespace std;

int N, Q, s[1000000];
vector< int > Student;
multiset< int > Leader;

char Query[10];
int a;

int main()
{
  scanf("%d %d", &N, &Q);
  Student.resize(N);
  for(int i = 0; i < N; ++i) {
    scanf("%d", &Student[i]);
    s[i] = Student[i];
  }
  sort(Student.begin(), Student.end());
  while(Q--) {
    scanf("%s %d", &Query, &a);
    if(Query[0] == 'A') { // "ADD"
      Leader.insert(s[--a]);
    } else if(Query[0] == 'R') { // "REMOVE"
      Leader.erase(Leader.find(s[--a]));
    } else { // "CHECK"
      int Lower = 0, Upper = 1 << 30;
      while(Lower < Upper) {
        int Mid = Lower + Upper >> 1, Lost = 0;
        vector< int >::iterator last = Student.begin();
        for(multiset< int >::iterator it = Leader.begin(); it != Leader.end() && last != Student.end(); ++it) {
          Lost += lower_bound(last, Student.end(), *it - Mid) - last;
          last = upper_bound(last, Student.end(), *it);
        }
        Lost += Student.end() - last;
        if(Lost <= a) Upper = Mid;
        else Lower = Mid + 1;
      }
      if(Lower == 1 << 30) cout << "NA" << endl;
      else cout << Lower << endl;
    }
  }
}