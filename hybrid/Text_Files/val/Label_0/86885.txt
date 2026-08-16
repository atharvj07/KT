import java.util.*;


import java.io.*;
public class D {
  public static void main(String[] args)throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int  n= Integer.parseInt(br.readLine());

    long[] ls = new long[n];
    long[] rs = new long[n];
    for(int i=0;i<n;++i){
      StringTokenizer st = new StringTokenizer(br.readLine());
      ls[i] = Integer.parseInt(st.nextToken());
      rs[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(ls);
    Arrays.sort(rs);
    long tot=0;
    for(int i=0;i<n;++i){
      tot+=1+Math.max(ls[i], rs[i]);
    }
    bw.write(tot+"");
    bw.flush();
  }
}
