import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong();
        long b = in.nextLong();
        long n = in.nextLong();
        long x = Math.min(b-1, n);
        long diff = (long)Math.floor(a * x / (double)b) - a * (long)Math.floor(x / (double)b);
        System.out.println(diff);
    }
}
