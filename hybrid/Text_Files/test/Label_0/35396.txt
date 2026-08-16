import java.util.*;
import java.io.*;
import java.math.*;
public class A{
    public static void main(String[] args)throws IOException{
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder("");
        int nb = n-k;
        nb /= 2;
        int r = 0;
        if(k<=2){
            for(int i=0;i<k;i++) out.print("0");
            for(int i=k;i<n;i++) out.print("1");
            out.println("");
        }else{
            while(r<n){
                sb.append("0");
                r++;
                if(r>=n) break;
                for(int d=0;d<nb;d++){
                    sb.append("1");
                    r++;
                    if(r>=n) break;
                }
            }
            out.println(sb.toString());
        }
        out.flush();
   }
}
