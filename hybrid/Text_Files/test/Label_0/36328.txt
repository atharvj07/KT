import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a1 = new int[n-1];
        int[] a2 = new int[n-1];
        int[] b = new int[n];
        for (int i = 0; i < n-1; i++) {
            a1[i] = scan.nextInt();
        }
        for (int i = 0; i < n-1; i++) {
            a2[i] = scan.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = scan.nextInt();
        }
        ArrayList<Integer> sums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < i; j++) {
                sum += a1[j];
            }
            sum += b[i];
            for (int j = i; j < n-1; j++) {
                sum += a2[j];
            }
            sums.add(sum);
        }
        Collections.sort(sums);
        System.out.println(sums.get(0) + sums.get(1));
    }
    
}