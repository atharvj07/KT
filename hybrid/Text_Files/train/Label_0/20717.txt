#include <iostream>
#include <algorithm>
#include <string>
#include <cstdlib>
using namespace std;

const int MY_NULL = 0;
const int MAX_MEM_SIZE = 20001;
const int INF = 1<<28;

string str;
int p;
bool error_flag;
int var[27];
class Heap* heap;

class Heap {
private:
  int mem[MAX_MEM_SIZE];
  int mem_ind;
  int mem_size;
public:
  Heap(int mem_size) : mem_size(mem_size), mem_ind(1) {
    fill(mem,mem+MAX_MEM_SIZE,0);
    mem[0] = -1;
  }
  Heap() {}

  int malloc(int size) {
    if(mem_size < size) return MY_NULL;
    mem_size -= size;
    mem[mem_ind] = size;
    return mem_ind++;
  }

  int clone(int p) {
    if(p == MY_NULL) return MY_NULL;
    if(p == INF || mem[p] ==  MY_NULL) {
      error_flag = true;
      return MY_NULL;
    }
    if(mem_size < mem[p]) return MY_NULL;
    mem_size -= mem[p];
    mem[mem_ind] = mem[p];
    return mem_ind++;
  }

  void free(int p) {
    if(p == MY_NULL) return;
    if(p == INF || mem[p] == MY_NULL) {
      error_flag = true;
      return;
    }
    mem_size += mem[p];
    mem[p] = 0;
  }

  int count_leak() {
    for(int i = 1; i <= 26; ++i) {
      if(var[i] == INF || var[i] == MY_NULL) continue;
      mem[var[i]] = 0;
    }
    int cnt = 0;
    for(int i = 1; i < 20001; ++i) cnt += mem[i];
    return cnt;
  }
};


void line();
int expr();
int assign();
int my_malloc();
void my_free();
int my_clone();
int variable();
int number();


void line() {
  if(str.substr(p,4) == "free") my_free();
  else expr();
}

int expr() {
  int res = MY_NULL;
  if(str[p] == '(') {
    ++p;
    res = expr();
    ++p;
  } else if(str.substr(p,4) == "NULL") {
    p += 4;
    res = MY_NULL;
  } else if(str.substr(p,6) == "malloc") {
    res = my_malloc();
  } else if(str.substr(p,5) == "clone") {
    res = my_clone();
  } else if(p+1 < str.size() && isalpha(str[p]) && str[p+1] == '=') {
    res = assign();
  } else if(isalpha(str[p])) {
    res = variable();
  }
  return res;
}

int assign() {
  int v = variable();
  ++p;
  int e = expr();
  if(e < 0) e = var[-e];
  return var[-v] = e;
}

int my_malloc() {
  p += 7;
  int n = number();
  ++p;
  return heap->malloc(n);
}

void my_free() {
  p += 5;
  int e = expr();
  if(e < 0) e = var[-e];
  ++p;
  heap->free(e);
}

int my_clone() {
  p += 6;
  int e = expr();
  if(e < 0) e = var[-e];
  ++p;
  return heap->clone(e);
}

int variable() {
  return -(str[p++]-'A'+1);
}

int number() {
  int begin = p;
  int length = 0;
  while(p < str.size() && isdigit(str[p])) ++p;
  return atoi(str.substr(begin,p-begin).c_str());
}

int main() {
  int M;
  cin >> M;
  cin.ignore();
  heap = new Heap(M);
  fill(var,var+27,INF);
  error_flag = false;

  while(getline(cin,str)) {
    p = 0;
    line();
  }

  if(error_flag) cout << "Error" << endl;
  else cout << heap->count_leak() << endl;
  return 0;
}