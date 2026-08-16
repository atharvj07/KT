import java.io.*;
import java.util.*;

public class TheBits {
    public static void main(String[] args) throws Exception {
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(buffer.readLine());
        char []  a = buffer.readLine().toCharArray();
        char [] b = buffer.readLine().toCharArray();
        long zeroZero = 0, zeroOne = 0, oneZero = 0, oneOne = 0;
        for (int pos = 0; pos < n; pos++) {
            if (a[pos]=='0')
                if (b[pos]=='1')zeroOne++;
                else zeroZero++;
            else
                if (b[pos]=='1')oneOne++;
                else oneZero++;
        }
        long ans = zeroOne*oneZero+zeroZero*(oneOne+oneZero);
        System.out.println(ans);
    }
}
