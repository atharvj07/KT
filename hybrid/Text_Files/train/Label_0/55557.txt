import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if (y % 2 != 0 || y < (2*x) || y > (4*x)) {
          System.out.println("No");
        } else {
          System.out.println("Yes");
        }
    }
}