    import java.util.*;
    import java.lang.*;
    import java.io.*;
    public class HelloWorld{
     
         public static void main(String []args)throws Exception{
              BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new
         FileOutputStream(java.io.FileDescriptor.out), "ASCII"), 512);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String line = br.readLine();
            int t = Integer.parseInt(line);
            for(int T=0;T<t;T++){
                line = br.readLine();
                int n = Integer.parseInt(line);
                long[] a = new long[n];
                long[] b = new long[n];
                for(int i=0;i<n;i++){
                line = br.readLine();
                String[] strs = line.trim().split("\\s+");
                a[i] = Long.parseLong(strs[0]);
                b[i] = Long.parseLong(strs[1]);
                }
                b[n-1] = Math.min(b[n-1],a[0]);
                long min = b[n-1];
                long goli = a[n-1] - b[n-1];
                for(int i=0;i<n-1;i++){ 
                    b[i] = Math.min(b[i],a[i+1]);
                    min = Math.min(min,b[i]);
                    goli += a[i] - b[i];
                }
                goli += min;
                String golis = Long. toString(goli);
                out.write(golis);
                out.write('\n');
            }
             out.flush();
         }
    }