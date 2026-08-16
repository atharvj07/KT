import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int N = scan.nextInt();
    String A = scan.next();
    int ans = 1;
    for (int i = 0 ; i < N - 1 ; i++) {
      if (!A.substring(i, i+1).equals(A.substring(i+1, i+2))){
        ans += 1;
      }
    }
    System.out.println(ans);
    scan.close();
  }
}