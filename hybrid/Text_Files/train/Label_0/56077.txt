import java.util.Scanner;

public class Main {

  public static void main(final String[] args) {
    final var scanner = new Scanner(System.in);
    final int a = scanner.nextInt();

    System.out.println(a + a * a + a * a * a);
  }
}
