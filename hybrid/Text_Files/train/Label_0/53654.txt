import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
  public static void main (String[] args) {
    Scanner in = new Scanner(System.in);

    while (in.hasNext()) {
      int N = in.nextInt();
      int X = in.nextInt();
      ArrayList<Integer> x = new ArrayList<Integer>();

      while ( N-- > 0) {
        x.add(in.nextInt());
      }
      
      Collections.sort(x);
      int insPoint = Collections.binarySearch(x, X);

      if (insPoint < 0) {
        insPoint = -(insPoint + 1);
        x.add(insPoint, X);
      }
      
      int gcdX = x.get(1) - x.get(0);
      for (int i = 2; i < x.size(); ++i) {
        gcdX = gcd(gcdX, x.get(i) - x.get(i - 1));
      }

      System.out.println(gcdX);
    }
  }

  private static int gcd (int a, int b) {
    return a % b == 0 ? b : gcd(b, a % b);
  }
}