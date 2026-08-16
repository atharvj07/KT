import java.util.*;
public class Main{
  public static void main (String args[]){
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] hList = new int[n];
    boolean[] jList = new boolean[n]; 
    
    for (int i = 0; i < n; i++){
      hList[i] = sc.nextInt();
    }
    
    int ans = 0;
    
    for (int i = 0; i < m; i++){
      int s = sc.nextInt();
      int g = sc.nextInt();
      if (hList[s-1]>hList[g-1]){
        jList[g-1] = true;
      } else if (hList[s-1]<hList[g-1]){
        jList[s-1] = true;
      } else {
        jList[g-1] = true;
        jList[s-1] = true;
      }
    }
    
    for (int i = 0; i < n; i++){
      if(!(jList[i])){
        ans++;
      }
    }
                 
    System.out.println(ans);
    
  }
}