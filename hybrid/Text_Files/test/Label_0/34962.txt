import java.util.*;

public class Main {

  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);

    int A = sc.nextInt();
    int B = sc.nextInt();

    sc.close();

    int count = 0;

    for (int i = A; i <= B; i++) {
      
      String i_ = String.valueOf(i);
      String[] I = i_.split("");

      if (I[0].equals(I[4]) && I[1].equals(I[3])) {
        count++;
      }

    }

    System.out.println(count);

  }

}