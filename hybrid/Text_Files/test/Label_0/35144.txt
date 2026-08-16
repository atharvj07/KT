/*
 * Author: pranay.agra
 * Time: 2020-04-26 10:36:17
*/

import java.io.*;
import java.util.*;

public class d {
    public static void main(String[] args) throws IOException {
        Scanner std = new Scanner(System.in);
        BufferedWriter log = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder strBu = new StringBuilder();        

        int n = std.nextInt();
        int k = std.nextInt();
        int[] arrSize = new int[n];
        int[] maxKVals = new int[k + 1];
        int[] freq = new int[k + 1];
        for (int i = 0; i < n; i++) {
            arrSize[i] = std.nextInt();
            freq[arrSize[i]]++;
        }

        for (int i = 0; i < k; i++) {
            maxKVals[i + 1] = std.nextInt();
        }

        int testcases = Integer.MIN_VALUE;
        long freqSum = 0;

        for (int i = k; i >= 1; i--) {
            freqSum += freq[i];
            int tc = (int) ( Math.ceil(freqSum / (double)maxKVals[i]) );
            testcases = Math.max(tc, testcases);
        }

        log.write(testcases + "\n");
        //6*10^5 so far

        MergeSort ob = new MergeSort();
        ob.sort(arrSize, 0, arrSize.length-1);
        int elem = 0;

        ArrayList<Integer>[] ans = new ArrayList[testcases];
        for (int i = 0; i < testcases; i++) {
            ans[i] = new ArrayList<Integer>(n / testcases + 1);
        }

        for (int i = 0; i < n; i++) {
            ans[elem].add(arrSize[i]);
            elem++;
            elem %= testcases;
        }


        for (int i = 0; i < testcases; i++) {
            log.write(ans[i].size() + " ");
            for (int j = 0; j < ans[i].size(); j++) {
                if (ans[i].get(j) == 0) break;
                log.write(ans[i].get(j) + " ");
            }
            log.write("\n");
        }

        log.flush();
    }

    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(InputStream system) {
            br = new BufferedReader(new InputStreamReader(system));
        }

        public Scanner(String file) throws Exception {
            br = new BufferedReader(new FileReader(file));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public char nextChar() throws IOException {
            return next().charAt(0);
        }

        public Long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public int[] nextArrInt(int n) throws IOException {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        public long[] nextArrLong(int n) throws IOException {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }

        public boolean ready() throws IOException {
            return br.ready();
        }

        public void waitForInput() throws InterruptedException {
            Thread.sleep(3000);
        }
    }

    static class MergeSort {
        // Merges two subarrays of arr[].
        // First subarray is arr[l..m]
        // Second subarray is arr[m+1..r]
        void merge(int arr[], int l, int m, int r) {
            // Find sizes of two subarrays to be merged
            int n1 = m - l + 1;
            int n2 = r - m;

            /* Create temp arrays */
            int L[] = new int[n1];
            int R[] = new int[n2];

            /*Copy data to temp arrays*/
            for (int i = 0; i < n1; ++i)
                L[i] = arr[l + i];
            for (int j = 0; j < n2; ++j)
                R[j] = arr[m + 1 + j];


            /* Merge the temp arrays */

            // Initial indexes of first and second subarrays
            int i = 0, j = 0;

            // Initial index of merged subarry array
            int k = l;
            while (i < n1 && j < n2) {
                if (L[i] <= R[j]) {
                    arr[k] = L[i];
                    i++;
                } else {
                    arr[k] = R[j];
                    j++;
                }
                k++;
            }

            /* Copy remaining elements of L[] if any */
            while (i < n1) {
                arr[k] = L[i];
                i++;
                k++;
            }

            /* Copy remaining elements of R[] if any */
            while (j < n2) {
                arr[k] = R[j];
                j++;
                k++;
            }
        }

        // Main function that sorts arr[l..r] using
        // merge()
        void sort(int arr[], int l, int r) {
            if (l < r) {
                // Find the middle point
                int m = (l + r) / 2;

                // Sort first and second halves
                sort(arr, l, m);
                sort(arr, m + 1, r);

                // Merge the sorted halves
                merge(arr, l, m, r);
            }
        }
    }
}

/**
Remember to check for overflow (long)
Does number need to be greater than a lower bound?
**/

