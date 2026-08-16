import java.util.HashSet;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        long ice = input.nextLong();
        char c ;
        long l = 0;
        long distressed = 0;
        for (int i = 0; i < n; i++) {
            c = input.next().charAt(0);
            l = input.nextLong();
            if (c == '+') {
                ice += l;
            } else {
                if (l <= ice) {
                    ice -= l;
                } else {
                    distressed++;
                }
            }

        }
        System.out.print(ice + " " + distressed);

    }
}
