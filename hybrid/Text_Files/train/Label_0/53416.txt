import java.io.*;
import java.util.*;
public class xenia {
 public static void main(String[]args)throws java.lang.Exception{
    BufferedReader bf  = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());
    int n= Integer.parseInt(st.nextToken());
    int m =Integer.parseInt(st.nextToken());
    String [] s= bf.readLine().split(" ");
    long time =Integer.parseInt(s[0])-1;
    for(int i = 0; i<m-1 ;i++){
      int prev = Integer.parseInt(s[i]);
      int cur = Integer.parseInt(s[i+1]);
      if(cur>prev && n>= cur)
        time+= cur - prev;
      else if(cur < prev)
             time+= n-prev+cur;

    }

    System.out.println(time);
  }
}