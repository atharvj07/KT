import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int A = in.nextInt();
    int B = in.nextInt();
    if (A <= 8 && B <= 8) {
      System.out.println("Yay!");
    } else {
      System.out.println(":(");
    }
  }
}
