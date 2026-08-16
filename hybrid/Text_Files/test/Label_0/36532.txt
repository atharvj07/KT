import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by zhangrunfeng on 2/18/20
 */
public class Main {
    private int N;

    private int[] arr;
    private int[] T;
    private boolean[] v;

    private int minVal;

    public Main(Scanner sc) {
        N = sc.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);

        int VMAX = 10000 + 5;
        T = new int[VMAX];
        for (int i = 0; i < N; i++) {
            T[sortedArr[i]] = i;
        }
        minVal = sortedArr[0];

        v = new boolean[N]; // 不用初始化
        Arrays.fill(v, false);
    }

    public int minCost() {
        int sum = 0;
        for (int i = 0; i < N; i++) {
            if (v[i]) continue;

            int an = 0;
            int currSum = 0;
            int currMin = Integer.MAX_VALUE;
            int currIx = i;
            while (!v[currIx]) {
                v[currIx] = true;
                currSum += arr[currIx];
                if (arr[currIx] < currMin) {
                    currMin = arr[currIx];
                }
                an++;
                currIx = T[arr[currIx]];
            }
            if (an >= 2) {
                sum += (currSum + Math.min((an - 2) * currMin, (an + 1) * minVal + currMin));
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Main m = new Main(sc);
        int res = m.minCost();
        System.out.println(res);
    }
}
