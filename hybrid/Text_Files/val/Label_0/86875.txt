import java.util.Scanner;
import java.util.HashMap;

public class Main {
    private static final int MAXN = 2 * (int)10e5, MAXA = (int)10e9;
    private static int[] data = new int[3];
    private final static String[] str = {"A", "B", "C"};

    private static String calc(int i, int j, String next, String comp) {
        if (data[i] == 0 && data[j] == 0) {
            return "";
        }

        if (data[i] == 0) {
            ++data[i];
            --data[j];
            return str[i];
        } else if(data[j] == 0){
            --data[i];
            ++data[j];
            return str[j];
        } else {
            if(data[i] == 1 && data[j] == 1) {
                if (next.equals(comp)) {
                    --data[i];
                    ++data[j];
                    return str[j];
                } else {
                    ++data[i];
                    --data[j];
                    return str[i];
                }
            } else if (data[i] > data[j]) {
                --data[i];
                ++data[j];
                return str[j];
            } else {
                ++data[i];
                --data[j];
                return str[i];
            }
        }
    }

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = scanner.nextInt();

        for (int i = 0; i < 3; ++i) {
            data[i] = scanner.nextInt();
        }

        var strs = new String[n];
        for (int i = 0; i < n; ++i) {
            strs[i] = scanner.next();
        }

        boolean ans = true;
        var rets = new String[n];
        for (int i = 0; i < n; ++i) {
            String next = "";
            if (i + 1 < n) {
                next = strs[i + 1];
            }

            if (strs[i].equals("AB")) {
                rets[i] = calc(0, 1, next, "BC");
                if (rets[i].equals("")) {
                    ans = false;
                    break;
                }
            }
            if (strs[i].equals("BC")) {
                rets[i] = calc(1, 2, next, "AC");
                if (rets[i].equals("")) {
                    ans = false;
                    break;
                }
            }
            if (strs[i].equals("AC")) {
                rets[i] = calc(0, 2, next, "BC");
                if (rets[i].equals("")) {
                    ans = false;
                    break;
                }
            }
        }

        if (ans) {
            System.out.println("Yes");
            for (int i = 0; i < n; ++i) {
                System.out.println(rets[i]);
            }
        } else {
            System.out.println("No");
        }
    }
}
