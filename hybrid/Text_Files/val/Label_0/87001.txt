import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.TreeMap;




public class Main {
    
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new PrintWriter(System.out));
        
       String[] in = br.readLine().split(" ");
       
       double a = Double.parseDouble(in[0]);
       double b = Double.parseDouble(in[1]);
       double c = Double.parseDouble(in[2]);
       
       double den = 2*a;
       
       double det = b*b - 4*a*c;
       det = Math.pow(det, 0.5);
       
       double ans[] = new double[2];
       
       double ans1 = -b+det;
       ans1/=den;
       ans[0] = ans1;
       
       double ans2 = -b-det;
       ans2/=den;
       
       ans[1] = ans2;
       
       Arrays.sort(ans);
       
       String val1 = String.format("%.12f", ans[1]);
       String val2 = String.format("%.12f", ans[0]);
       
       bw.append(val1+"\n");
       bw.append(val2+"\n");
        bw.close();
    }

   //tmp = String.format("%.6f %.6f", mm, 0.0);

    
    
    
}