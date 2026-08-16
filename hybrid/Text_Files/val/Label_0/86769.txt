import java.util.*;

public class Main {

  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    sc.close();

    for (int i = 1; i <= 9; i++) {
      int j = i * 100 + i * 10 + i;
      if (N <= j) {
        System.out.println(j);
        break;
      }
    }

  }

}