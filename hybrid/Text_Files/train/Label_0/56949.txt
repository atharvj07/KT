import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        long nn = 0;
        for (int i = 0; i < n; i++) {
            nn += sc.nextInt();
        }
        long mm = 0;
        for (int i = 0; i < m; i++) {
            mm += sc.nextInt();
        }
        System.out.println(nn * mm);
    }
}
