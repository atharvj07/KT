import java.util.Scanner;

public class Fraction{
    
public static int gcd(int a, int b) {
  return b == 0 ? a : gcd(b, a % b);
}

public static void main(String[] args) {
  Scanner kbd = new Scanner(System.in);
  int n = kbd.nextInt();

  double max = 0.0;
  int numerator = 1;

  for (int i = 1; i <= n / 2; ++i)
  {
	int a = i;
	int b = n - i;

	if (gcd(a, b) == 1)
	{
	  if (a > b * max)
	  {
		max = a / b;
		numerator = i;
	  }
	}
  }

  System.out.print(numerator);
  System.out.print(" ");
  System.out.print(n - numerator);
  System.out.print("\n");
 }
}