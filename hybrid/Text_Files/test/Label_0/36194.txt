import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        String[] ips = br.readLine().split(" ");
        int len = ips.length;
        int[] cnta = new int[100005];
        int[] cntb = new int[100005];
        int mxa = 0;
        int mxb = 0;
        int mxa2 = 0;
        int mxb2 = 0;
        int besta = -1;
        int bestb = -1;
        
        for(int i = 0; i < len; i+=2){
            int curr = Integer.parseInt(ips[i]);
            cnta[curr]++;
            if(cnta[curr] > mxa){
                mxa = cnta[curr];
                besta = curr;
            }
        }
        
        for(int i = 1; i < len; i+=2){
            int curr = Integer.parseInt(ips[i]);
            cntb[curr]++;
            if(cntb[curr] > mxb){
                mxb = cntb[curr];
                bestb = curr;
            }
        }
        
        for(int i = 0; i < 100005; ++i){
            int f = cnta[i];
            int f2 = cntb[i];
            if(f <= mxa && i!=besta)
                mxa2 = Math.max(mxa2, f);
            if(f2 <= mxb && i!=bestb)
                mxb2 = Math.max(mxb2, f2);
        }
        
        int res = 0;
        if(besta != bestb){
            System.out.println(len-mxa-mxb);
            return;
        }
        res = Math.min(len-mxa2-mxb, len-mxa-mxb2);
        System.out.println(res);
    }
}