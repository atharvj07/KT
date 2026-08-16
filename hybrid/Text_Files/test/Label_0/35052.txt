import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    long a = scanner.nextLong();
    long b = scanner.nextLong();
    long x = scanner.nextLong();
    b = b / x;
    a = a > 0 ? (a - 1) / x : -1;
    System.out.println(b - a);
  }
}
