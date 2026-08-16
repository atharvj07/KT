import java.util.*;

public class Main {
    Scanner in = new Scanner(System.in);

    public void run() {
        int a = in.nextInt(), b = in.nextInt();
        String s = in.next();

        boolean ok = true;
        for (int i = 0; i <= a + b; i++) {
            if (i == a) {
                ok &= s.charAt(i) == '-';
            } else {
                ok &= Character.isDigit(s.charAt(i));
            }
        }
        System.out.println(ok ? "Yes" : "No");
    }


    public static void main(String[] args) {
        new Main().run();
    }
}
