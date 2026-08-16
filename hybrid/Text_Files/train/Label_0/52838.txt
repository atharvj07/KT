
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = n % 10;
        int b = n / 100;
        if (a == b) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }

}