import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * @project: CodeforcesEduc90
 * @author: izhanatuly
 * @date: 25/06/2020
 */
public class D {
    static Scanner scanner;

    public static void main(String[] args) {
        scanner = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int cases = scanner.nextInt();
        for (int t = 0; t < cases; t++) {
            runTestCase();
        }
    }

    public static void runTestCase() {
        int n = scanner.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        long var1 = cadane(nums, true);
        long var2 = cadane(nums, false);
        System.out.println(Math.max(var1, var2));
    }

    static long cadane(int[] nums, boolean cmpBack) {
        int n = nums.length;
        // calc sum on evens
        long sumEvens = 0;
        for(int i=0; i<n; i++) {
            if(i%2==0) sumEvens += nums[i];
        }
        // calc diff on odds with cadane
        long currSum = 0;
        long bestSum = 0;
        for(int i=1; i<n; i+=2) {
            long diff;
            if(cmpBack) {
                diff = nums[i] - nums[i-1];
            } else {
                if(i<n-1) {
                    diff = nums[i] - nums[i+1];
                } else {
                    diff = 0;
                }
            }
            if(currSum+diff < diff) {
                currSum = diff;
            } else {
                currSum += diff;
            }
            if(currSum > bestSum) {
                bestSum = currSum;
            }
        }
        // return best cadane + sum on evens
        return bestSum + sumEvens;
    }
}
