import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[] ar = new int[n];
        int[] cnt = new int[n];
        for (int i = 0; i < n; i++) {
            ar[i] = sc.nextInt();
            cnt[i] = 0;
        }
        for (int i = n - 1; i >= 0; i--) {
            int ans_cnt;
            ans_cnt = 0;
            for (int j = i + 1; j < n; j++) {
                ans_cnt += cnt[j] * (j - i + 1);
            }
            cnt[i] = ar[i] - ans_cnt;
        }
        
        StringBuilder ans = new StringBuilder();
        String a, b;
        a = "a";
        b = "b";
        
        boolean is_a = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < cnt[i]; j++) {
                for (int x = 0; x < i + 1; x++) {
                    if (is_a) ans.append(a);
                    else ans.append(b);
                }
                is_a = !is_a;
            }
        }
        System.out.println(ans);
    }
}