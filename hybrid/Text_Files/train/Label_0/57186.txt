//JDope
import java.util.*;
import java.io.*;
import java.math.*;
public class F{
public static void main(String[] omkar) throws Exception
{
   BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
   StringTokenizer st = new StringTokenizer(in.readLine());
   StringBuilder sb = new StringBuilder();
   int n = Integer.parseInt(st.nextToken());
   int[] nums = new int[n+1];
   int[] bumps = new int[n];
   int count = 0;
   st = new StringTokenizer(in.readLine());
   String s = st.nextToken();
   long total = 0;
   long prev = 0;
   for(int i = 0; i < n; i++)
   {
      if(s.charAt(i) == '0')
      {
         nums[0] = nums[0]+1;
         count = 0;
      }
      else
      {
         count = count+1;
         nums[count] += nums[count-1];
         prev += (long)(nums[count-1]);
         if(count > 1)
         {
            nums[count-1] = 1;
            prev = prev + (long)(count-1);
         } 
         else
         {
            nums[0] = 0;
            nums[1]++;
            prev = prev + (long)(1);
         }
      }
      total += prev;
   }  
   System.out.println(total);
        }
 public static long computeSum(int[] arr, int l, int r)
 {
   long ret = 0;
   if(r == l+1)
   {
      return (long)(arr[l])*(long)(l);
   }
   return computeSum(arr, l, (l+r)/2)+computeSum(arr, (l+r)/2, r);
 }
 public static int[] readArr(int N, BufferedReader in, StringTokenizer st) throws Exception
      {
         int[] arr = new int[N];
         st = new StringTokenizer(in.readLine());
         for(int i=0; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken());
         return arr;
      }


}