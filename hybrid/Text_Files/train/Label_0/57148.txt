import java.io.*;
import java.util.*;

public class Matrix {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(f.readLine());
        String str = f.readLine();
        int[] prefix = new int[str.length()+1];
        prefix[0] = 0;
        for (int i = 1; i <= str.length(); i++)
            prefix[i] = prefix[i-1] + str.charAt(i-1)-'0';
        long[] count = new long[40000];
        for (int i = 0; i < prefix.length; i++)
            for (int j = i+1; j < prefix.length; j++)
                count[prefix[j]-prefix[i]]++;
        if (a == 0) {
            System.out.println(count[0]*str.length()*(str.length()+1)-count[0]*count[0]);
            return;
        }
        long sum = 0;
        for (int i = 1; i < count.length; i++)
            if (a % i == 0 && a/i < count.length)
                sum += count[i]*count[a/i];
        System.out.println(sum);
    }
}