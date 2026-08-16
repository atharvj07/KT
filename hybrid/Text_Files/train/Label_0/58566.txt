
/**
 * 
1 quicksort(A, p, r)
2   if p < r
3     q = partition(A, p, r)
4     quickSort(A, p, q-1)
5     quickSort(A, q+1, r)
 *
 */

import java.util.*;
import java.io.*;

/**
 * C
 */
public class Main {

    void run() throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String[] A = new String[n+1];
        String[] A_copy = new String[n+1];

        for(int i=0; i<n; i++) {
            A[i] = br.readLine();
            A_copy[i] = A[i];
        }

        mergeSort(A_copy, 0, n);
        quickSort(A, 0, n-1);
        System.out.println(Arrays.equals(A, A_copy) ? "Stable" : "Not stable");
        show(A, n);

        br.close();

    }

    
    void quickSort(String[] A, int p, int r) {
        
        if(p<r) {
            
            int q = partition(A, p, r);
            quickSort(A, p, q-1);
            quickSort(A, q+1, r);
            
        }
    }
    
    int partition(String[] A, int p, int r) {
        
        int x = Integer.parseInt(A[r].substring(2));
        int i = p - 1;
        for (int j=p; j<r; j++) {
            if (Integer.parseInt(A[j].substring(2))<=x) {
                i++;
                String tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
        
        String tmp = A[i+1];
        A[i+1] = A[r];
        A[r] = tmp;
        
        return i+1;
        
    }

    /*
    void bubbleSort(String[] c, int n) {
        for(int i=0; i<n-1; i++) {
            for(int j=n-1; j>i; j--) {
                if(c[j].charAt(2)<c[j-1].charAt(2)) {
                    String tmp = c[j];
                    c[j] = c[j-1];
                    c[j-1] = tmp;
                }   
            }
        }
    }
    */

    void mergeSort(String[] A, int l, int r) {

        if(l+1<r) {
            int m = (l+r)/2;
            mergeSort(A, l, m);
            mergeSort(A, m, r);
            merge(A, l, m, r);
        }

    }

    void merge(String[] A, int l, int m, int r) {
        
        int n1 = m-l;
        int n2 = r-m;

        String[] L = new String[n1+1];
        String[] R = new String[n2+1];

        for(int i=0; i<n1; i++) {
            L[i] = A[l+i];
        }

        for(int i=0; i<n2; i++) {
            R[i] = A[m+i];
        }

        L[n1] = R[n2] = "I 1000000001";

        int i = 0;
        int j = 0;

        for(int k=l; k<r; k++) {

            if(Integer.parseInt(L[i].substring(2))<=Integer.parseInt(R[j].substring(2))) {
                A[k] = L[i];
                i++;
            } else {
                A[k] = R[j];
                j++;
            }

        }

    }
    
    void show(String[] c, int n) {
        
        for(int i=0; i<n; i++) {
            System.out.println(c[i]);
        }

    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }

}
