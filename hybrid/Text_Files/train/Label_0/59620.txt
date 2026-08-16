
import java.util.ArrayList;
import java.util.Scanner;

public class MakeItGood {

    static boolean cal(int[] a, int i) {
        int j = a.length - 1;
        ArrayList<Integer> ar = new ArrayList<Integer>();
        while (i < j) {
            if (a[i] < a[j]) {
                ar.add(a[i]);
                ++i;
            } else {
                ar.add(a[j]);
                --j;
            }
        }
        for (int k = 0; k < ar.size() - 1; k++) {
            if (ar.get(k) > ar.get(k + 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        while (t-- > 0) {
            int n = scan.nextInt();
            int[] a = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                a[i] = scan.nextInt();
            }
            int l = 1;
            int r = n;
            int res = 0;
            while (l <= r && l >= 1 && r <= n) {
                int md = (l + r) / 2;

                boolean p = cal(a, md);
                if (p) {
                    res = md;
                    r = md - 1;
                } else {
                    l = md + 1;
                }
            }
            System.out.println(res - 1);
        }
    }

}
