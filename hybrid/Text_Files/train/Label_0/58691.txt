import java.util.*;
public class Main{
  public static void main(String []args){
  Scanner sc = new Scanner(System.in);

  int n = sc.nextInt();

  int[] t = new int[n];
  int[] x = new int[n];
  int[] y = new int[n];
  int[] data = new int[n];

  for (int i = 0;i<n ;i++ ) {
    t[i] = sc.nextInt();
    x[i] = sc.nextInt();
    y[i] = sc.nextInt();
    data[i] = x[i]+y[i];
  }

  for (int i = 0;i<n ;i++ ) {
    if ((t[i]%2==0&&data[i]%2==1)||(t[i]%2==1&&data[i]%2==0)) {
      System.out.println("No");
      System.exit(0);
    }
    if (t[i]<x[i]+y[i]) {
      System.out.println("No");
      System.exit(0);
    }
  }
  System.out.println("Yes");


  }
}
