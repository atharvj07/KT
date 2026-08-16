import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ab = sc.nextInt();
        int bc = sc.nextInt();
        bc = bc / 2;
        sc.close();

        System.out.println(ab + bc);
    }
}