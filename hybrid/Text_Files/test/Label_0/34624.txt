import java.util.*;
import java .io.*;
public class Main {
    static int size;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int array[] = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int cnt[] = new int[n + 2];
        for(int i = 1;i <= n;i++){
            cnt[i] = Integer.parseInt(st.nextToken());
        }
        boolean mark[] = new boolean[n + 1];
        mark[1] = true;
        for(int i = 2;i <= n;i++)
            if(array[i] > array[i - 1])mark[i] = true;

        for(int i = n - 1;i >= 1;i--) {
            if(mark[i]){
                if(cnt[i] < array[i]){
                    System.out.print("0");
                    return;
                }
            }
            if (cnt[i] > cnt[i + 1]) {
                mark[i] = true;
                if(array[i] < cnt[i]){
                    System.out.print("0");
                    return;
                }
            }
        }
        if(mark[n] && array[n] != cnt[n]){
            System.out.print("0");
            return;
        }
        mark[n] = true;
        long ans = 1;
        int mod = 1000_000_000 + 7;
        for(int i = 1;i <= n;i++){
            if(mark[i])continue;
            ans *= Math.min(cnt[i],array[i]);
            ans %= mod;
        }
        System.out.print(ans);
    }
}