import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
      	String message = "";
        if (a < 1200) {
            message = "ABC";
        } else {
            message = "ARC";
        }
      System.out.println(message);
    }
}