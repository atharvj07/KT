import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner std = new Scanner(System.in);
        long w = std.nextLong();
        long h = std.nextLong();
        long x = std.nextLong();
        long y = std.nextLong();

        double sq = w * h / 2.0;
        if (w / 2.0 == x && h / 2.0 == y) {
            System.out.println(sq + " 1");
        } else {
            System.out.println(sq + " 0");
        }
    }
}
