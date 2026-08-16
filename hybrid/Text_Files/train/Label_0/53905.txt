public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
    int a, b, count, t = 0;;

    for(;;){
      a = sc.nextInt(); b = sc.nextInt();
      if(a == 0 && b == 0)break;
      if(t++ != 0)out.println();
      for(count = 0;a <= b;a++)if(isleapyear(a)){
        out.println(a); count++;
      }
      if(count == 0)out.println("NA");
    }

    sc.close();
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }
  private static boolean isleapyear(int a){
    if(a % 400 == 0)return true;
    if(a % 100 == 0)return false;
    if(a % 4 == 0)return true;
    return false;
  }
}