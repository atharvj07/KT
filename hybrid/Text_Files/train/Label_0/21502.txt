#include <bits/stdc++.h>
using namespace std;
int coPrimeTest(int numerator, int denominator) {
  int counter = 0;
  for (int i = 1; i <= numerator; i++) {
    if (numerator % i == 0) {
      if (denominator % i == 0) {
        counter++;
      }
    }
  }
  if (counter > 1) {
    return false;
  } else
    return true;
}
int main() {
  int number;
  cin >> number;
  int numerator = 1;
  int denominator = number - 1;
  int coPrimeNumerator, coPrimeDenominator;
  for (int i = 0; i < number; i++) {
    if (numerator > denominator) {
      break;
    }
    if (coPrimeTest(numerator, denominator) == true) {
      coPrimeNumerator = numerator;
      coPrimeDenominator = denominator;
    }
    numerator++;
    denominator--;
  }
  cout << coPrimeNumerator << " " << coPrimeDenominator << endl;
  return 0;
}
