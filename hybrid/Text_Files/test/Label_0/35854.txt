import java.util.*;
import java.io.*;

public class a{

  public static void main(String [] args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int [] a=new int[n+1];
    int [] b=new int[n];
    Arrays.fill(a,0);
    for(int i=0;i<n;i++)a[sc.nextInt()]=i;
    for(int i=0;i<n;i++)b[i]=sc.nextInt();

    Map<Integer,Integer> map=new HashMap<>();
    for(int i=0;i<n;i++){
      int e=b[i];

      int d=i;
      int u=a[e];

      int leftMove=0;
      if(d<u){
        leftMove=d+(n-(u));
      }
      else{
        leftMove=d-u;
      }
      
      if(map.containsKey(leftMove)){
        map.put(leftMove,map.get(leftMove)+1);
      }
      else{
        map.put(leftMove,1);
      }
      
    }
    int max=0;

    for(Map.Entry<Integer,Integer> entry : map.entrySet()){
      max=Math.max(entry.getValue(),max);
    }

    System.out.println(max);


  }
}
