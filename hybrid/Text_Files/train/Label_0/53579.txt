import java.util.*;
import java.io.*;
import java.math.*;

public class Main {

    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int n = input.nextInt();
        int k = input.nextInt();
        int q = input.nextInt();
        int[] deriv = new int[200002];
        int[] integBinSum = new int[200002];
        for (int i = 1; i <= n; i++) {
            deriv[input.nextInt()]++;
            deriv[input.nextInt() + 1]--;
        }
        int integ = 0;
        for (int i = 1; i <= 200000; i++) {
            integ += deriv[i];
            integBinSum[i] = integBinSum[i - 1] + (integ >= k ? 1 : 0);
        }
        for (int i = 0; i < q; i++) {
            int first = integBinSum[input.nextInt() - 1], last = integBinSum[input.nextInt()];
            System.out.println(last - first);
        }
    }
}