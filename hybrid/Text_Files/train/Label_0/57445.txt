import java.util.*;
import java.math.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int sum = 0;
    for (int i = 0; i < 3; i++) sum += sc.nextInt();
    if (sum >= 22) System.out.println("bust");
    else System.out.println("win");
  }
}
