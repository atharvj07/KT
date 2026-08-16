import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[N];
        for (int i=0;i<N;i++) {
            A[i] = sc.nextInt();
            B[i] = A[i];
        }
        Arrays.sort(B);
        int cnt = 0;
        for (int i=0;i<N;i++) {
            cnt+=Math.abs(Arrays.binarySearch(B, A[i])-i)%2;
        }
        System.out.println(cnt/2);
    }
}
