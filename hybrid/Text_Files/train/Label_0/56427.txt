import java.util.*;
public class MyClass {
    public static void main(String args[]) {
      Scanner sc=new Scanner(System.in);
      int tc=sc.nextInt();
      int i,j,f,max,p;
      while(tc>0)
      {
          int n=sc.nextInt();
          int arr[]=new int[n];
          p=0;
          for(i=0;i<n;i++)
          {
          arr[i]=sc.nextInt();
          if(arr[i]==0)
          p=1;
          }
          f=1;
          for(j=0;j<n;j++)
          {
              if(arr[j]<0)
              {
                  f=0;
                  break;
              }
          }
          if(f==0)
          System.out.print("NO");
          else
          {
              System.out.println("YES");
              Arrays.sort(arr);
              if(p==0)
              System.out.println(arr[n-1]);
              else
              System.out.println(arr[n-1]+1);
              for(i=1;i<=arr[n-1];i++)
              System.out.print(i+" ");
              if(p==1)
              System.out.print("0");
          }
          System.out.println();
          --tc;
      }}}