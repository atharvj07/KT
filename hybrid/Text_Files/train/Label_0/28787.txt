#include <bits/stdc++.h>
using namespace std;
template <typename _T>
class vertix {
 private:
  int capacity = 0;
  _T* arr = new _T[capacity];

 public:
  vertix() {
    capacity = 000;
    delete[] arr;
    arr = new _T[capacity];
  }
  vertix(int S) {
    capacity = S;
    delete[] arr;
    arr = new _T[capacity];
  }
  _T& operator[](int index) { return arr[index]; }
  int size() { return capacity; }
  void push_back(_T type) {
    _T* newarr = new _T[capacity + 1];
    for (int i = 0; i < capacity; i++) {
      newarr[i] = arr[i];
    }
    newarr[capacity] = type;
    delete[] arr;
    arr = newarr;
    capacity++;
  }
  void push_front(_T type) {
    _T* newarr = new _T[capacity + 1];
    for (int i = 1; i < capacity + 1; i++) {
      newarr[i] = arr[i - 1];
    }
    newarr[0] = type;
    capacity++;
    delete[] arr;
    arr = newarr;
  }
  void pop_front() {
    _T* newarr = new _T[capacity - 1];
    for (int i = 0; i < capacity - 1; i++) {
      newarr[i] = arr[i + 1];
    }
    delete[] arr;
    capacity--;
    arr = newarr;
  }
  void pop_back() { capacity--; }
  _T front() { return arr[0]; }
  _T back() { return arr[capacity - 1]; }
  void clear() {
    capacity = 0;
    _T* newarr = new _T[capacity];
    delete[] arr;
    arr = newarr;
  }
  _T* begin() { return &arr[0]; }
  _T* end() { return &arr[capacity]; }
};
template <typename _T>
class AbdElrahmanTarek112 {
 private:
  int capacity;
  _T* arr = new _T[capacity];

 public:
  AbdElrahmanTarek112() {
    capacity = 0;
    arr = new _T[capacity];
  }
  AbdElrahmanTarek112(int capacity) {
    this->capacity = capacity;
    arr = new _T[capacity];
  }
  _T& operator[](int index) { return arr[index]; }
  _T& operator[](_T* arr) { this->arr = arr; }
  int size() { return capacity; }
  void push_back(_T type) {
    _T* newarr = new _T[capacity + 1];
    for (int i = 0; i < capacity; i++) {
      newarr[i] = arr[i];
    }
    newarr[capacity] = type;
    arr = newarr;
    capacity++;
  }
  void push_front(_T type) {
    capacity++;
    _T* newarr = new _T[capacity];
    for (int i = 1; i < capacity; i++) {
      newarr[i] = arr[i - 1];
    }
    newarr[0] = type;
    arr = new _T[capacity];
    arr = newarr;
  }
  bool empty() { return capacity == 0 ? true : false; }
  void pop(int index) {
    _T* newarr = new _T[capacity - 1];
    for (int i = 0; i < index; i++) {
      newarr[i] = arr[i];
    }
    for (int i = index; i < capacity - 1; i++) {
      newarr[i] = arr[i + 1];
    }
    delete[] arr;
    capacity -= 1;
    arr = newarr;
  }
  void push_in(_T type, int index) {
    _T* newarr = new _T[capacity + 1];
    for (int i = 0; i < index; i++) {
      newarr[i] = arr[i];
    }
    for (int i = index + 1; i < capacity + 1; i++) {
      if (i - 1 > capacity - 1)
        capacity++;
      else
        newarr[i] = arr[i - 1];
    }
    newarr[index] = type;
    capacity++;
    delete[] arr;
    arr = newarr;
  }
  void pop_front() {
    _T* newarr = new _T[capacity - 1];
    for (int i = 0; i < capacity - 1; i++) {
      newarr[i] = arr[i + 1];
    }
    delete[] arr;
    capacity--;
    arr = newarr;
  }
  void pop_back() { capacity--; }
  _T front() { return arr[0]; }
  _T back() { return arr[capacity - 1]; }
  void clear() {
    capacity = 0;
    _T* newarr = new _T[capacity];
    delete[] arr;
    arr = newarr;
  }
  _T* begin() { return &arr[0]; }
  _T* end() { return &arr[capacity]; }
  void print() {
    if (capacity == 0) {
      return;
    }
    for (int i = 0; i < capacity; i++) {
      cout << arr[i] << " ";
    }
  }
  void unique() {
    vector<int> G;
    int newcapacity = 0;
    int newindex = 0;
    for (int i = 0; i < capacity; i++) {
      if (i + 1 == capacity) {
        G.push_back(arr[i]);
      } else {
        if (arr[i] == arr[i + 1])
          ;
        else {
          G.push_back(arr[i]);
        }
      }
    }
    _T* newarr = new _T[G.size()];
    for (int i = 0; i < G.size(); i++) {
      newarr[i] = G[i];
    }
    arr = new _T[G.size()];
    arr = newarr;
    capacity = G.size();
  }
  void like_set() {
    set<_T> c;
    int Old_Size = 0, index = 0;
    _T* newarr = new _T[capacity];
    for (int i = 0; i < capacity; i++) {
      c.insert(arr[i]);
      if (c.size() != Old_Size) {
        Old_Size++;
        newarr[index] = arr[i];
        index++;
      }
    }
    arr = newarr;
    capacity = c.size();
  }
};
template <typename KEY, typename VALUE>
class var {
  pair<KEY, VALUE> tr[10005];

 public:
  VALUE& operator[](KEY thekey) {
    int index = 0;
    for (int i = 0; i < 10005; i++) {
      if (tr[i].first == thekey) {
        index = i;
        break;
      }
    }
    return tr[index].second;
  }
};
void cin_array_usual(int o[], int size) {
  for (int i = 0; i < size; i++) {
    cin >> o[i];
  }
}
void print_array_usual(int o[], int size) {
  for (int i = 0; i < size; i++) {
    cout << o[i] << " ";
  }
  cout << endl;
}
void print_forward_list(forward_list<int> o) {
  for (auto i = o.begin(); i != o.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}
void print_set(set<int> o) {
  for (auto i = o.begin(); i != o.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}
void print_vector(vector<int> o) {
  for (auto i = o.begin(); i != o.end(); i++) {
    cout << *i << " ";
  }
  cout << endl;
}
int main() {
  string x, y, z;
  cin >> x >> y >> z;
  if (x == y && y == z) {
    cout << '?' << endl;
  } else if (x != y && y != z && x != z) {
    cout << '?' << endl;
  } else {
    if (x == y) {
      if (x == "rock") {
        if (z == "paper") {
          cout << "S" << endl;
        } else if (z == "scissors") {
          cout << "?" << endl;
        }
      } else if (x == "paper") {
        if (z == "rock") {
          cout << "?" << endl;
        } else if (z == "scissors") {
          cout << "S" << endl;
        }
      } else if (x == "scissors") {
        if (z == "rock") {
          cout << "S" << endl;
        } else if (z == "paper") {
          cout << "?" << endl;
        }
      }
    } else if (y == z) {
      if (y == "rock") {
        if (x == "paper") {
          cout << "F" << endl;
        } else if (x == "scissors") {
          cout << "?" << endl;
        }
      } else if (y == "paper") {
        if (x == "rock") {
          cout << "?" << endl;
        } else if (x == "scissors") {
          cout << "F" << endl;
        }
      } else if (y == "scissors") {
        if (x == "rock") {
          cout << "F" << endl;
        } else if (x == "paper") {
          cout << "?" << endl;
        }
      }
    } else if (x == z) {
      if (x == "rock") {
        if (y == "paper") {
          cout << "M" << endl;
        } else if (y == "scissors") {
          cout << "?" << endl;
        }
      } else if (x == "paper") {
        if (y == "rock") {
          cout << "?" << endl;
        } else if (y == "scissors") {
          cout << "M" << endl;
        }
      } else if (x == "scissors") {
        if (y == "rock") {
          cout << "M" << endl;
        } else if (y == "paper") {
          cout << "?" << endl;
        }
      }
    }
  }
  return 0;
}
