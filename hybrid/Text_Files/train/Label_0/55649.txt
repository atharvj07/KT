import java.io.*;

import java.util.*;


public class Solution {


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = scanner.nextInt();
        }

        int max = 0;
        int sum = 0;


        for (int i = 1; i < arr.length; i++) {
            if(arr[i] > arr[i-1]){
                max = Math.max(sum,max);
                sum= calLeft(arr,i);
            }else{
                  sum++;
            }
         }
        max = Math.max(sum,max);
        System.out.println(++max);
    }

    private static int calLeft(int[] arr, int i) {
        int sum = 0;
        for (int j = i; j > 0; j--) {
            if(arr[j] >= arr[j-1])
            sum++;
            else
                break;
        }
        return sum;
    }
}
