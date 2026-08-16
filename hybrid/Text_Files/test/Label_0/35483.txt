import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        String c = in.next();
        int min = 2;
        if (a.equals(b) && b.equals(c)) {
            min = 0;
        }
        if (a.charAt(1) == b.charAt(1) && b.charAt(1) == c.charAt(1)) {
            int[] arr = new int[]{a.charAt(0) - '0', b.charAt(0) - '0', c.charAt(0) - '0'};
            Arrays.sort(arr);
            if (arr[0] + 1 == arr[1] && arr[1] + 1 == arr[2]) {
                min = 0;
            }
        }
        if (a.equals(b) || b.equals(c) || a.equals(c)) {
            min = Math.min(min, 1);
        }
        int A = a.charAt(0) - '0';
        int B = b.charAt(0) - '0';
        int C = c.charAt(0) - '0';
        if (a.charAt(1) == b.charAt(1) && Math.abs(A - B) <= 2) {
            min = Math.min(min, 1);
        }
        if (a.charAt(1) == c.charAt(1) && Math.abs(A - C) <= 2) {
            min = Math.min(min, 1);
        }
        if (b.charAt(1) == c.charAt(1) && Math.abs(B - C) <= 2) {
            min = Math.min(min, 1);
        }
        System.out.println(min);
    }
}