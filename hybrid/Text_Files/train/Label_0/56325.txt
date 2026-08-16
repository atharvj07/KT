public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
/*answer*/
    int n;
    int[] a;
    int i;

    a = new int[31];
    a[1] = 1; a[2] = 2; a[3] = 4;
    for(i = 4;i < 31;i++)a[i] = a[i - 1] + a[i - 2] + a[i - 3];

    for(;;){
      n = sc.nextInt();
      if(n == 0)break;
      else if(a[n] % 3650 == 0)out.println(a[n] / 3650);
      else out.println(a[n] / 3650 + 1);
    }

    sc.close();
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }
}