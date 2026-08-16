import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    new Main().run();
  }

  private Scanner sc = new Scanner(System.in);

  private void run() {
    long N = sc.nextLong();
    long A = sc.nextLong();
    long B = sc.nextLong();

    long aSet = N / (A + B) * A;
    long mod = N % (A + B);

    System.out.println(aSet + Math.min(mod, A));
  }
}
