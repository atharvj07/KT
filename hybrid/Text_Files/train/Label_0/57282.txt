import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long y = sc.nextLong();

        sc.close();

        int cnt = 0;

        while (true) {
            if (x > y) {
                break;
            }
            cnt++;
            x *= 2;
        }

        System.out.println(cnt);

    }

}