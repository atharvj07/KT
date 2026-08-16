import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        
        while (in.hasNextLine()) {
            int N = in.nextInt();
            int M = in.nextInt();
            if (N == 0 && M == 0) break;
            
            int[] arr = new int[N];
            int max = -99;
            
            for (int m = 0; m < M; m++) {
                for (int n = 0; n < N; n++) {
                    arr[n] += in.nextInt();
                    if (m == M - 1) {
                        max = Math.max(max, arr[n]);
                    }
                }
            }
            
            System.out.println(max);
        }
    }
}

