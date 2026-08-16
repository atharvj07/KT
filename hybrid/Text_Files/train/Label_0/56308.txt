import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int h = sc.nextInt();
    int w = sc.nextInt();
    int[][] a = new int[h][w];
    List<String> list = new ArrayList<>();
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)a[i][j]=sc.nextInt();
    for(int i=0;i<h;i++)
      for(int j=0;j<w-1;j++)
        if(a[i][j]%2==1){
          a[i][j]--;
          a[i][j+1]++;
          list.add((i+1)+" "+(j+1)+" "+(i+1)+" "+(j+2));
        }
    for(int i=0;i<h-1;i++)
      if(a[i][w-1]%2==1){
        a[i][w-1]--;
        a[i+1][w-1]++;
        list.add((i+1)+" "+w+" "+(i+2)+" "+w);
      }
    System.out.println(list.size());
    for(String s:list)System.out.println(s);
  }
}