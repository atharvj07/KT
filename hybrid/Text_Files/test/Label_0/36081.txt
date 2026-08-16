import java.util.*;
import java.io.*;
import java.lang.*;
import java.math.*;
public class D {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        // Scanner scan = new Scanner(System.in);
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int[] a = new int[n];
        for(int i=0; i<n; i++) a[i] =  Integer.parseInt(st.nextToken());
        int initial_counter = 1;
        for(int i=1; i<n; i++) if(a[i] != a[i-1]) initial_counter++;
        int num_counter = 0;
        int cur_counter = 1;
        int[] compressed = new int[initial_counter];
        int[] count = new int[initial_counter];
        for(int i=1; i<n; i++) {
          if(a[i] == a[i-1]) cur_counter++;
          else {
            compressed[num_counter] = a[i-1];
            count[num_counter] = cur_counter;
            num_counter++;
            cur_counter = 1;
          }
        }
        compressed[num_counter] = a[n-1];
        count[num_counter] = cur_counter;
        num_counter++;
        cur_counter = 1;

        //out.println(Arrays.toString(compressed));
        //out.println(Arrays.toString(count));
        long sum = 0;
        for(int i=0; i<initial_counter; i++) {
          int start_counter = i;
          int end_counter = i;
          while((start_counter-1 >= 0) && bit_subset(compressed[start_counter-1], compressed[i]) && (compressed[start_counter-1] != compressed[i]))
            start_counter--;
          while((end_counter+1 < initial_counter) && bit_subset(compressed[end_counter+1], compressed[i]))
            end_counter++;
          long count_start = 0;
          for(int j=start_counter; j<i; j++) count_start += count[j];
          long count_end = 0;
          for(int j=i+1; j<=end_counter; j++) count_end += count[j];
          long total = count_start + count_end + count[i];
          long toAdd = 1L*total*(total-1)/2 - 1L*count_start*(count_start-1)/2 - 1L*count_end*(count_end-1)/2;

          sum += toAdd;
        }
        out.println((1L*n*(n-1)/2-sum));

        out.close(); System.exit(0);
    }
    public static boolean bit_subset(int v1, int v2) {
      return ((1L*v1 | 1L*v2) == 1L*v2);
    }

}
