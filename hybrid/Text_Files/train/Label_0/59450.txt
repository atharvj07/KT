import java.util.*;

public class Main {

    public static void main(String args[]) {

        // 入力
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int a = Integer.parseInt(sc.next());
        int b = Integer.parseInt(sc.next());
        String s = sc.next();
        sc.close();

        // 主処理
        String[] arr = new String[n];
        int countA = 0;
        int countB = 0;
        for (int i = 0; i < n; i++) {
            int count = countA + countB;
            if (s.charAt(i) == 'a') {
                if (count < a + b) {
                    arr[i] = "Yes";
                    countA++;
                } else {
                    arr[i] = "No";
                }
            } else if (s.charAt(i) == 'b') {
                if (count < a + b && countB < b) {
                    arr[i] = "Yes";
                    countB++;
                } else {
                    arr[i] = "No";
                }
            } else {
                arr[i] = "No";
            }
        }

        String result = String.join("\n", arr);

        // 出力
        System.out.println(result);
    }
}
