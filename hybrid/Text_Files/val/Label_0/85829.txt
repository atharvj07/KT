#include <bits/stdc++.h>
volatile bool isLocalTestEnabled = 0;
bool g_isLocalPrintEnabled = (bool)(0);
template <typename T>
void UpdateMin(T& a, const T b) {
  a = std::min(a, b);
}
template <typename T>
void UpdateMax(T& a, const T b) {
  a = std::max(a, b);
}
const long double Pi = std::atan(1.0L) * 4.0L;
static const long double Eps = 1.0e-09;
template <typename T>
bool IsEqual(const T a, const T b) {
  return std::abs(a - b) < Eps;
}
template <typename T>
bool IsGreater(const T a, const T b) {
  return a > b + Eps;
}
template <typename T>
bool IsLess(const T a, const T b) {
  return a + Eps < b;
}
template <typename T>
bool IsGreaterEqual(const T a, const T b) {
  return !IsLess(a, b);
}
template <typename T>
bool IsLessEqual(const T a, const T b) {
  return !IsGreater(a, b);
}
template <typename T>
std::string ToStr(const T& val) {
  std::ostringstream ostr;
  ostr << val;
  return ostr.str();
}
template <typename T>
bool FromStr(const std::string& str, T& val) {
  std::istringstream istr(str);
  istr >> val;
  return !!istr;
}
template <typename T>
std::istream& operator>>(std::istream& ist, std::vector<T>& data) {
  ;
  for (size_t i = 0; i < data.size(); i++) {
    ist >> data[i];
  }
  return ist;
}
template <typename T>
T Read(std::istream& ist) {
  ;
  T val;
  ist >> val;
  return val;
}
template <typename T>
std::ostream& operator<<(std::ostream& ost, const std::vector<T>& data) {
  for (size_t i = 0; i < data.size(); i++) {
    if (i != 0) {
      ost << ' ';
    }
    ost << data[i];
  }
  return ost;
}
template <size_t id>
class StopWatch {};
void GetDiffs(const std::string& s1, const std::string& s2, const size_t limit,
              std::vector<size_t>& d) {
  d.clear();
  for (size_t i = 0; i < s1.size(); i++) {
    if (s1[i] != s2[i]) d.push_back(i);
    if (d.size() >= limit) return;
  }
}
bool Can(const std::string& s, const std::set<std::string>& v) {
  std::vector<size_t> diffs;
  for (const std::string& vi : v) {
    if (s == vi) {
      char c[26] = {
          0,
      };
      bool hasTwo = false;
      for (char si : s) {
        c[si - 'a'] += 1;
        if (c[si - 'a'] == 2) {
          hasTwo = true;
          break;
        }
      }
      if (!hasTwo) return false;
      continue;
    }
    GetDiffs(s, vi, 3, diffs);
    if (diffs.size() != 2) return false;
    const size_t p1 = diffs[0];
    const size_t p2 = diffs[1];
    if (s[p1] != vi[p2]) return false;
    if (s[p2] != vi[p1]) return false;
  }
  return true;
}
std::string GetAns(const std::vector<std::string>& s) {
  std::set<std::string> v(s.begin(), s.end());
  if (v.size() == 1) {
    std::string t = *v.begin();
    std::swap(t[0], t[1]);
    return t;
  }
  std::set<std::string> checked;
  std::vector<size_t> d;
  for (std::set<std::string>::const_iterator v1 = v.begin(); v1 != v.end();
       ++v1) {
    const std::string& s1 = *v1;
    std::string t = s1;
    std::set<std::string>::const_iterator v2 = v1;
    ++v2;
    for (; v2 != v.end(); ++v2) {
      const std::string& s2 = *v2;
      GetDiffs(s1, s2, 5, d);
      if (d.size() > 4) return "-1";
      for (size_t i = 0; i < d.size(); i++) {
        for (size_t j = i + 1; j < d.size(); j++) {
          std::swap(t[d[i]], t[d[j]]);
          if (checked.count(t) == 0) {
            if (Can(t, v)) return t;
            checked.insert(t);
          }
          std::swap(t[d[i]], t[d[j]]);
        }
      }
    }
  }
  return "-1";
}
bool Solve(std::istream& ist, std::ostream& ost, const bool multipleTestMode) {
  StopWatch<1> sw;
  (void)sw;
  size_t k, n;
  ist >> k >> n;
  if (multipleTestMode && !ist) return false;
  if (!g_isLocalPrintEnabled) {
  } else
    std::cerr << std::endl << "Next test" << std::endl;
  std::vector<std::string> s(k);
  ist >> s;
  std::string ans = GetAns(s);
  ost << ans << std::endl;
  return multipleTestMode;
}
void RunSolve(std::istream& ist, std::ostream& ost) { Solve(ist, ost, false); }
int main(int argc, const char* argv[]) {
  std::ios_base::sync_with_stdio(false);
  if (argc > 1) {
    std::ifstream ifs(argv[1]);
    if (!ifs) {
      std::cout << "File not found: " << argv[1] << std::endl;
      return 1;
    }
    RunSolve(ifs, std::cout);
    return 0;
  }
  RunSolve(std::cin, std::cout);
}
