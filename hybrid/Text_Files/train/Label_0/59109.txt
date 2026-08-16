import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        List<String> ansList = new ArrayList<>();

        // 2^30 = 1073741824
        // 2^31 = 2147483648
        long target = n;
        for (int i = 1; i <= 32; i++) {
//            System.out.println(target);
            if (Math.abs(target) % pow(2, i) != 0) {
                ansList.add("1");
                target -= pow(-2, i - 1);
            } else {
                ansList.add("0");
            }
        }

//        System.out.println(ansList);

        String ans = "";
        boolean flag = false;
        for (int i = ansList.size() - 1; i >= 0; i--) {
            if (ansList.get(i).equals("1")) {
                flag = true;
            }
            if (flag) {
                ans += ansList.get(i);
            }
        }

        if (ans.equals("")) {
            ans = "0";
        }
        System.out.println(ans);
    }

    // baseのn乗を計算を返す
    static long pow(int base, int n) {
        long ret = 1;
        for (int i = 0; i < n; i++) {
            ret *= base;
        }
        return ret;
    }
}
