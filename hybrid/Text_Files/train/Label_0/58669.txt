import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    double m = 0.d;
    for (int i = 0; i < N; i++) {
      int a = scanner.nextInt();
      m += 1.d / a;
    }

    System.out.println(1.d / m);
  }
}
