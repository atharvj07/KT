import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[]$) {
        int h = scanner.nextInt();
        int w = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        fac = new long[h + w + 1];
        inv = new long[h + w + 1];
        fac[0] = inv[0] = 1;
        for (int i = 1; i <= h + w; i++) {
            fac[i] = fac[i - 1] * i % 1000000007;
            inv[i] = powAndMod(fac[i], 1000000005);
        }

        long ans = 0;
        for (int i = b; i < w; i++) {
            ans = (ans + combination(i, h - a - 1) * combination(w - i - 1, a - 1) % 1000000007) % 1000000007;
        }
        System.out.println(ans);
    }

    static long[] fac, inv;
    static long combination(int h, int w) {
        return fac[h + w] * inv[h] % 1000000007 * inv[w] % 1000000007;
    }

    static long powAndMod(long a, long b) {
        if (b == 0)
            return 1;
        if ((b & 1) == 1)
            return a * powAndMod(a, b - 1) % 1000000007;
        return powAndMod(a * a % 1000000007, b / 2);
    }
}